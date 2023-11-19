import httpx

class NominatimApi():
    BASE_URL = "https://nominatim.openstreetmap.org"

    async def _make_request(self, path: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL + path)

        if response.status_code != 200:
            raise Exception("Some error occorred")
        
        return response.json()

    async def get_value(self, country: str, region: str) -> (float, float):
        response = await self._make_request(f"/search?country={country}&city={region}&format=json")

        if len(response) == 0:
            return (0, 0)

        return (response[0]['lat'], response[0]['lon'])