from entities.region import Region
from helpers.xml_configuration import XmlConfiguration, TypeXmlConfiguration

class RegionXmlConfiguration(XmlConfiguration):

    def configure(self, builder: TypeXmlConfiguration) -> None:
        # builder.hasKeys(['region_1'])
        builder.setHeaderName('Regions')
        builder.hasKeys(['region_1'])
        builder.hasDependencies(['country'])

        builder.hasConvertion(
            labda=lambda values, foreign_keys: 
                Region(
                    foreign_keys['country'],
                    values['region_1'])
        )
        
        return builder.build()