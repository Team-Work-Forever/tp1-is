from entities.wine import Wine
from helpers.xml_configuration import XmlConfiguration, TypeXmlConfiguration


class WineXmlConfiguration(XmlConfiguration):

    def configure(self, builder: TypeXmlConfiguration) -> None:
        builder.setHeaderName("Wines")
        builder.hasKeys(["variety", "price"])

        builder.hasConvertion(
            lambda values:
                Wine(
                    values["price"],
                    '',
                    1,
                    1,
                    values["variety"],
                    ''
                )
        )

        return builder.build()