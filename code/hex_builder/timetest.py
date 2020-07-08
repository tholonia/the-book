#
from astropy.time import Time
import datetime

obstime = Time('2020-06-24 17:31:07.154677')
print(obstime)


x = obstime + datetime.timedelta(0,3)

print(x)
