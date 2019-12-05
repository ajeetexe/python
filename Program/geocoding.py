from geopy.geocoders import Nominatim

nom = Nominatim()
hi = nom.geocode('3995 23rd St , San Francisco, CA 94114')
print(hi)
print(hi.longitude, hi.latitude)