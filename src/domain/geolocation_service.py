from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import RateLimiter

class GeoLocationService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geopy_api")
        self.geocode = RateLimiter(self.geolocator.geocode, min_delay_seconds=1)

    def get_address(self, postal_code):
        try:
            location = self.geolocator.geocode(postal_code, addressdetails=True)
            if location:
                return location.raw.get('address', {})
            return None
        except GeocoderTimedOut:
            return None