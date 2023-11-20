import httpx
import time

class NominatimApi:
    BASE_URL = "https://nominatim.openstreetmap.org"

    def __init__(self, delay_between_requests=3):
        self.delay_between_requests = delay_between_requests

    async def _make_request(self, path: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL + path)

        response.raise_for_status()
        return response.json()

    async def get_value(self, country: str, region: str) -> (float, float):
        try:
            response = await self._make_request(f"/search?country={country}&city={region}&format=json")

            if len(response) == 0:
                return 0, 0

            time.sleep(4)
            return float(response[0]['lat']), float(response[0]['lon'])
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
