from csv import DictReader


class CSVReader:

    def __init__(self, path, delimiter=','):
        self._path = path
        self._delimiter = delimiter

    def loop(self):
        with open(self._path, 'r') as file:
            for row in DictReader(file, delimiter=self._delimiter):
                yield row
        file.close()

    # def has_empty_value(self, row):
    #     for value in row[1:]:
    #         if value == '':
    #             return True
            
    #     return False

    # def read(self):
    #     entries = []

    #     for row in self.loop():
    #         if any(row[value] == '' for value in row):
    #             continue
            
    #         entries.append(row)
            
    #     return entries
                
    def read_entities(self, attr, builder, after_create=None):
        entities = {}
        for row in self.loop():
            e = row[attr]
            if e not in entities:
                entities[e] = builder(row)
                after_create is not None and after_create(entities[e], row)

        return entities
