import httpx
import time

class NominatimApi():
    BASE_URL = "https://nominatim.openstreetmap.org"
    CACHE_MAP = {}
    
    def get_key(self, country, region):
        return '-'.join([country, region])

    def insert_region(self, country, region, point):
        key = self.get_key(country, region)

        if key not in NominatimApi.CACHE_MAP:
            NominatimApi.CACHE_MAP[key] = [point]
        else:
            NominatimApi.CACHE_MAP[key].append(point)

    def get_region(self, country, region):
        key = self.get_key(country, region)

        if key in NominatimApi.CACHE_MAP:
            NominatimApi.CACHE_MAP[key]
        
        return None

    async def _make_request(self, path: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL + path)

        response.raise_for_status()
        return response.json()

    async def get_value(self, country: str, region: str) -> (str, str):
        point = self.get_region(country, region)

        if point is not None:
            return point

        try:
            response = await self._make_request(f"/search?country={country}&city={region}&format=json")

            if len(response) == 0:
                return 0, 0
            
            result = str(response[0]['lat']), str(response[0]['lon'])

            self.insert_region(country, region, result)

            time.sleep(1)
            return result
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise