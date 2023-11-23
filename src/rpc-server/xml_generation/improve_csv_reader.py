from asyncio.coroutines import iscoroutine
from csv import DictReader


class BetterCSVReader:

    def __init__(self, path, delimiter=','):
        self._path = path
        self._delimiter = delimiter

    def loop(self):
        with open(self._path, 'r') as file:
            for row in DictReader(file, delimiter=self._delimiter):
                yield row
        file.close()

    async def read_entities_async(self, attr, builder, after_create=None, batch_size=1000):
        entities = {}
        with open(self._path, 'r') as file:
            csv_reader = DictReader(file, delimiter=self._delimiter)

            for i, row in enumerate(csv_reader, start=1):
                e = '-'.join([row[at] for at in attr if at in row and row[at] != ''])

                if e not in entities:
                    try:
                        vamos = builder(row)
                        entities[e] = vamos
                    except Exception as i:
                        print(f"Why i'm still here {i}")

                    # if iscoroutine(entities[e]):
                    #     entities[e] = await entities[e]

                    if after_create:
                        after_create(entities[e], row)

                if i % batch_size == 0:
                    yield entities
                    entities = {}

        if entities:
            yield entities

    async def read_entities(self, attr, builder, after_create=None, batch_size=1000):
        entities_list = [entity async for entity in self.read_entities_async(attr, builder, after_create, batch_size)]

        entities = {}
        for entity_dict in entities_list:
            entities.update(entity_dict)

        return entities