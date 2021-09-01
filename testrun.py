from os import getenv
from bustime.monitor import StopMonitor


BUSTIME_API_KEY = getenv('BUSTIME_API_KEY')

print("M15")
monitor = StopMonitor(BUSTIME_API_KEY, '401768', 'm15', 3)
print(monitor)



print("\nM15-SBS South-Bound")
monitor = StopMonitor(BUSTIME_API_KEY, '401768', 'M15+', 3)
print(monitor)


print("\nM15-SBS North-Bound")
monitor = StopMonitor(BUSTIME_API_KEY, '405319', 'M15+', 3)
print(monitor)
