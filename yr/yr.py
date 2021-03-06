import urllib2
import urllib
import xml.etree.ElementTree as et
import xml.etree.cElementTree as et
#import lxml.etree as et


# Public: A class that gets the weather data from yr.no based on a geoname
#
# geoname - the geoname string separated with "/". e.g.
#			"Finland/Western_Finland/Turku"
#
# Examples
#
# 	weather = yr("Finland/Western_Finland/Turku")
class yr:

	def __init__(self, geoname,fetch=True):
		yr_base_url = "http://www.yr.no/place/"
		yr_end_url  = "/forecast_hour_by_hour.xml" # alt /forecast.xml

		if fetch:
			self.weather = self.get_weather(yr_base_url+urllib.quote(geoname)+yr_end_url)


	# Private: Fetches the weather data for the given geoname
	#
	# url - the url to fetch the weather from, generated by __init__
	#
	# Examples
	#
	#	self.get_weather("http://www.yr.no/place/Finland/Western_Finland/Turku/forecast.xml")
	#
	# Returns an array of weather maps
	def get_weather(self, url):
		try:
			p = urllib2.urlopen(url).read()
			return self.parse_xml(p)
		except urllib2.HTTPError, err:
			if err.code == 404:
				raise NameError("The requested area was not found")
	  		elif err.code == 500:
				raise IOError("Server returned error 500")
			else:
				raise


	# Private: Parses url data to a structure
	def parse_xml(self, data):
		tree = et.fromstring(data)
		forecasts_xml = tree.find("forecast")[0]
		weather = [
			{
				'time': forecast.attrib,
				'weather': forecast.find("symbol").attrib,
			 	'precipitation': forecast.find("precipitation").attrib,
			 	'wind': {
			 		'direction': forecast.find("windDirection").attrib,
			 		'speed': forecast.find("windSpeed").attrib
			 	},
			 	'temperature': forecast.find("temperature").attrib,
			 	'pressure': forecast.find("pressure").attrib
			} for forecast in forecasts_xml]
		return weather
