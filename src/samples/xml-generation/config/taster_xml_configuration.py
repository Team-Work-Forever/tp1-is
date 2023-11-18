from entities.taster import Taster
from helpers.xml_configuration import XmlConfiguration, TypeXmlConfiguration

class TasterXmlConfiguration(XmlConfiguration):
    
    def configure(self, builder: TypeXmlConfiguration) -> None:
        builder.setHeaderName('Tasters')
        builder.hasKeys(['taster_name', 'taster_twitter_handle'])

        builder.hasConvertion(
            labda=lambda values: 
                Taster(
                    values['taster_name'], 
                    values['taster_twitter_handle'])
        )
        
        return builder.build()