from plant import Plant
from rules import *

plants_container = []


class PlantSelection(KnowledgeEngine):
    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='mixed'),
                Insolation(insolation_type='dark'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='yes'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            SecondaryColor(secondary_colour_type='not important')

        )
    )
    def plant_grass(self):
        plant = Plant('Grass, Festuca rubra', 'Ideal for lawns. Soft and calming.')
        global plants_container
        plants_container.append(plant)

        # print('Grass is ideal to plant')

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='dry'),
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='edible'),
                Function(function_type='aromatic'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='purple'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='green'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_lavender(self):
        # print('Lavender is ideal to plant')
        plant = Plant('Lavender, Lavandula angustifolia', 'Lavender pleases soul, eye nose and tongue.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='mixed'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='big'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='edible'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='red'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_cherry_tree(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Cherry tree, Prunus cerasus L', 'Cheri Cheri Lady')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='alkaline'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='mixed'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='medium'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='purple'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_detuzia(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Yuki cherry blossom, Deutzia Thunb',
                      'A shower of elegant pink flowers creates a carpet of color.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='alkaline'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='big'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='yes'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='brown'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_oak(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Irish Oak, Quercus petraea', 'Build a house, plant a tree, have a child.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='dry'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='big'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='brown'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_palm(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Chusan palm, Trachycarpus fortunei', 'Palm that can withstand forsts.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='big'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='edible'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='yellow'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_pear(self):
        plant = Plant('European pear, Pyrus communis', 'Juicy.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='aromatic'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='purple'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='green'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_stock(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Night-scented stock, Matthiola longipetala', 'Spreads the scent at eavnings.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='dark'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='white'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='green'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_horsetail(self):
        plant = Plant('Horsetail, Spathiphyllum cochlearispathum', 'It cleans air.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='dark'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='red'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_evergreen(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Chinese Evergreen, Aglaonema', 'One of the most popular houseplants.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='medium'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='edible'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='red'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_strawberry(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Garden strawberry, Fragaria × ananassa', 'Best known hybrid species.')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='moderate'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='medium'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='red'),
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='pink'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_rose(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Rose, Rosa L.', 'Caution, it stings!')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='dry'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='medium'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_golden_torch(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Golden torch, Echinopsis spachiana', 'Native to South America')
        global plants_container
        plants_container.append(plant)

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important')
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='not important')
            ),
            OR(
                Insolation(insolation_type='moderate'),
                Insolation(insolation_type='not important')
            ),
            OR(
                Size(size_type='medium'),
                Size(size_type='not important')
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important')
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important')
            ),
            OR(
                PrimaryColor(primary_colour_type='pink'),
                PrimaryColor(primary_colour_type='not important')

            ),
            OR(
                SecondaryColor(secondary_colour_type='green'),
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='not important')
            )

        )
    )
    def plant_bleeding_heart(self):
        # print('Cherry tree is ideal to plant')
        plant = Plant('Bleeding heart, Lamprocapnos spectabilis',
                      'It is valued for its heart-shaped pink and white flowers, borne in spring.')
        global plants_container
        plants_container.append(plant)
