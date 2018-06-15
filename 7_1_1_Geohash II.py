"""
This is a followup question for Geohash.

Convert a Geohash string to latitude and longitude.

Try http://geohash.co/.

Check how to generate geohash on wiki: Geohash or just google it for more details.

Example
Given "wx4g0s", return lat = 39.92706299 and lng = 116.39465332.

Return double[2], first double is latitude and second double is longitude.
"""

class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # Write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        for c in geohash:
            b += self.i2b(_base32.find(c)) 

        odd = ''.join([b[i] for i in range(0, len(b), 2)])
        even = ''.join([b[i] for i in range(1, len(b), 2)])

        location = []
        location.append(self.get_location(-90.0, 90.0, even))
        location.append(self.get_location(-180.0, 180.0, odd))
        return location

    def i2b(self, val):
        b = ""
        for i in range(5):
            if val % 2:
                b = '1' + b
            else:
                b = '0' + b
            val //= 2
        return b

    def get_location(self, start, end, string):
        for c in string:
            mid = (start + end) / 2.0
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2.0