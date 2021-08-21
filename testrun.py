from os import getenv
from bustime.monitor import StopMonitor


BUSTIME_API_KEY = getenv('BUSTIME_API_KEY')

print("M15")
monitor = StopMonitor(BUSTIME_API_KEY, '401768', 'm15', 2)
print(monitor)



print("\nM15-SBS")
monitor = StopMonitor(BUSTIME_API_KEY, '401768', 'm15-sbs', 2)
print(monitor)
