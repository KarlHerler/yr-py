# yr-py

This is a simple python library for interacting with the brilliant [yr.no](http://yr.no) weather service.


## Installing
Just drop the yr.py file in your project and import it. (I'll probably put it on pip at some point)

## Usage
 - Import the library to wherever you want to use it using `from yr import yr`
 - Create a weather instance using `weather = yr("Finland/Western_Finland/Turku")` where the
   parameter is the fully qualified geoname. You can also specify a False flag if you do not want
   the library to fetch the data on creation.
 - access the forecast data in `yr.weather`, this will be an array with forecast maps


## The weather struct
This is found in `yr.weather` after the data has been fetched and parsed. This
structure is an array with maps of the following format:

```python
{
    'time': { 'from': <time>, 'to': <time>, 'period': <int>},
	'weather': {'number': <int>, 'name': <str>, 'var': <str>},
	'precipitation': {'value': <decimal>, 'minvalue': <decimal>, 'maxvalue':<decimal>},
	'wind': {
		'direction': {'deg':<decimal>, 'code':<str>, 'name':<str>},
		'speed': {'mps':<decimal>, 'name':<str>}
	},
	'temperature': {'unit':<str>, 'value':<decimal>},
	'pressure': {'unit':<str>, 'value':<decimal>}
}
```

NOTE: Timezone is always local time, the period signifies part of the day (0: night, 1: morning, 2: afteroon, 3: evening)

### Example

```python
{
    'time': { 'from': <time>, 'to': <time>, 'period': <int>},
	'weather': {'number': 3, 'name': "Partly Cloudy", 'var': "mf/03n.70"},
	'precipitation': {'value': 0.2, 'minvalue': 0, 'maxvalue': 0.5},
	'wind': {
		'direction': {'deg':297.1, 'code':"WNW", 'name': "West-northwest"},
		'speed': {'mps':"5.8", 'name':"Moderate breeze"}
	},
	'temperature': {'unit':"celsius", 'value':12},
	'pressure': {'unit':"hPa", 'value':1001.0}
}
```

## Notes about usage
Since yr.no gives away their data for free they want you to limit your queries
to one query per zone per 10 minutes. You should cache the results if you think
that you will come close to this limit.
