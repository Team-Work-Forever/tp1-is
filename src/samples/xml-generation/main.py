from csv_to_xml_mine import CSVtoXMLMine
from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/dataset.csv")
    # converter = CSVtoXMLMine("/data/dataset.csv")

    with open("/data/dataset.xml", "w") as file:
        file.write(converter.to_xml_str())