from xml_generation.csv_to_xml_converter import CSVtoXMLConverter

def to_xml(s: str):
    converter = CSVtoXMLConverter("/data/dataset.csv")
    converter.to_xml()

    ## Storage xml file on postgresql

    return "E bem..."