# CSV2STA
A simple tool to upload CSV data to the SensorThingsAPI

## Prerequisites
* SensorThings Server
* Python 3.7++

## How to use?
* Set the SensorThings Observation URL in the `Post.py`
```python
STA_Endpoint = "http://xxx/xxx/v1.0/Observations"
```
* prepare your CSV structure based on the sample CSV file
* Run 
```
python Post.py
```
## Authors

**Joe T. Santhanavanich <thunyathep.santhanavanich@hft-stuttgart.de>** 

## License

This project is licensed under the Apache License Version 2.0 - see the [LICENSE.md](LICENSE.md) file for details.
