from helpers.xml_configuration import XmlConfiguration, TypeXmlConfiguration
from entities.country import Country

class CountryXmlConfiguration(XmlConfiguration):

    def configure(self, builder: TypeXmlConfiguration) -> None:
        builder.setHeaderName('Countries')
        builder.hasKeys(['country', "price"])
        
        builder.hasConvertion(
            labda=lambda values: 
                Country(values['country'])
        )

        return builder.build()
