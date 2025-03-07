# Bustime

## Installing on Raspbian Jessie

```sh
sudo apt-get install python-pip
sudo pip install bustime
```

## Running from project directory

```sh
BUSTIME_API_KEY=<api_key> python bustime -s 305174
```

## Example usage

```python
from os import getenv
from bustime import StopMonitor

BUSTIME_API_KEY = getenv('BUSTIME_API_KEY')

monitor = StopMonitor(BUSTIME_API_KEY, '306809', 'b62', 2)
print(monitor)
```

## References
- http://bt.mta.info/wiki/Developers/OneBusAwayRESTfulAPI
- http://bt.mta.info/wiki/Developers/SIRIStopMonitoring
- https://bustime.mta.info/m/index?q=401768

