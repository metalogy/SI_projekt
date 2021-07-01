from plant import Plant
#import menu

from rules import *
plants_container=[]
class PlantSelection(KnowledgeEngine):
    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='acidic'),
                SoilPH(soil_ph='not important'),
            ),

            OR(
                Humidity(humidity_type='wet'),
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important'),
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='mixed'),
                Insolation(insolation_type='dark'),
                Insolation(insolation_type='not important'),
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important'),
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='not important'),
            ),
            OR(
                Alergic(alergic_type='yes'),
                Alergic(alergic_type='not important'),
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='not important'),

            ),
            SecondaryColor(secondary_colour_type='not important')

        )
    )
    def plant_grass(self):
        plant=Plant('grass','Grass lorem ipsum')
        global plants_container
        plants_container.append(plant)

        print('Grass is ideal to plant')
        # TODO - może jakiś opis rośliny

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important'),
            ),

            OR(
                Humidity(humidity_type='dry'),
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important'),
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='not important'),
            ),
            OR(
                Size(size_type='small'),
                Size(size_type='not important'),
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='edible'),
                Function(function_type='aromatic'),
                Function(function_type='not important'),
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important'),
            ),
            OR(
                PrimaryColor(primary_colour_type='purple'),
                PrimaryColor(primary_colour_type='not important'),

            ),
            OR(
                SecondaryColor(secondary_colour_type='green'),
                SecondaryColor(secondary_colour_type='not important')
            ),

        )
    )
    def plant_lavender(self):
        print('Lavender is ideal to plant')
        plant=Plant('Lavender','Lavender lorem ipsum')
        global plants_container
        plants_container.append(plant)
        # TODO - może jakiś opis rośliny

    @Rule(
        AND(
            OR(
                SoilPH(soil_ph='neutral'),
                SoilPH(soil_ph='not important'),
            ),

            OR(
                Humidity(humidity_type='moderate'),
                Humidity(humidity_type='not important'),
            ),
            OR(
                Insolation(insolation_type='sunny'),
                Insolation(insolation_type='mixed'),
                Insolation(insolation_type='not important'),
            ),
            OR(
                Size(size_type='big'),
                Size(size_type='not important'),
            ),
            OR(
                Function(function_type='decorative'),
                Function(function_type='edible'),
                Function(function_type='not important'),
            ),
            OR(
                Alergic(alergic_type='no'),
                Alergic(alergic_type='not important'),
            ),
            OR(
                PrimaryColor(primary_colour_type='green'),
                PrimaryColor(primary_colour_type='purple'),
                PrimaryColor(primary_colour_type='not important'),

            ),
            OR(
                SecondaryColor(secondary_colour_type='white'),
                SecondaryColor(secondary_colour_type='red'),
                SecondaryColor(secondary_colour_type='purple'),
                SecondaryColor(secondary_colour_type='not important')
            ),

        )
    )
    def plant_cherry_tree(self):
        print('Cherry tree is ideal to plant')
        return 'Cherry tree is ideal to plant'
        # TODO - może jakiś opis rośliny

    # @Rule(
    #     AND(
    #         Soil(soil_type='fertile'),
    #         OR(
    #             Insolation(insolation_type='dark'),
    #             Insolation(insolation_type='mixed'),
    #         ),
    #         OR(
    #             Humidity(humidity_type='humid'),
    #             Humidity(humidity_type='medium'),
    #         ),
    #             Size(size_type='big'),
    #     )
    #
    # )
    # def plant_Oak(self):
    #     print("Oak is ideal to plant!")
    #
    # @Rule(
    #     AND(
    #         Soil(soil_type='barren'),
    #         OR(
    #             Insolation(insolation_type='sunny'),
    #             Insolation(insolation_type='mixed'),
    #         ),
    #             Humidity(humidity_type='dry'),
    #             Size(size_type='medium')
    #     )
    #
    # )
    # def plant_Cactus(self):
    #     print("Cactus is ideal to plant!")
    #
    # @Rule(
    #     AND(
    #         Soil(soil_type='barren'),
    #         Insolation(insolation_type='dark'),
    #         Humidity(humidity_type='dry'),
    #         OR(
    #             Size(size_type='big'),
    #             Size(size_type='medium'),
    #             Size(size_type='small')
    #         )
    #     )
    # )
    # def westland(self):
    #     print("Here nothing will grow!")
    #
    # @Rule(
    #     AND(
    #         Soil(soil_type='fertile'),
    #         OR(
    #             Insolation(insolation_type='sunny'),
    #             Insolation(insolation_type='mixed'),
    #         ),
    #         OR(
    #             Humidity(humidity_type='humid'),
    #             Humidity(humidity_type='medium'),
    #         ),
    #         OR(
    #             Size(size_type='big'),
    #             Size(size_type='small'),
    #             Size(size_type='medium'),
    #         ),
    #
    #     )
    #
    # )
    # def plant_Ficus(self):
    #     print("Ficus is ideal to plant!")

# engine = PlantSelection()
# engine.reset()
#
#
#
# print("What is the soil PH? \n3- Acidic \n2 - Neutral\n1 - Alkaline\n0 - Doesn't matter" )
# inpt = int(input())
# soil_ph = None
# if inpt == 3:
#     soil_ph = 'acidic'
# elif inpt == 2:
#     soil_ph='neutral'
# elif inpt == 1:
#     soil_ph='alkaline'
# else:
#     soil_ph = 'DNM'
# soil = SoilPH(soil_ph=soil_ph)
#
# print("What is the surrounding humidity?\n3 - humid\n2 - medium\n1 - dry\n0 - Doesn't matter")
# inpt = int(input())
# humidity_type = None
# if inpt == 3:
#     humidity_type = 'humid'
# elif inpt == 2:
#     humidity_type = 'medium'
# elif inpt==1:
#     humidity_type = 'dry'
# else:
#     humidity_type = 'DNM'
# humidity=Humidity(humidity_type=humidity_type)
#
#
# print("What is the insolation?\n3 - sunny\n2 - mixed\n1 - dark\n0 - Doesn't matter")
# inpt = int(input())
# insolation_type = None
# if inpt == 3:
#     insolation_type = 'sunny'
# elif inpt == 2:
#     insolation_type = 'mixed'
# elif inpt==3:
#     insolation_type = 'dark'
# else:
#     insolation_type = 'DNM'
# insolation=Insolation(insolation_type=insolation_type)
#
#
# print("What size should plant be?\n3 -big\n2 - medium\n1 - small\n0 - Doesn't matter")
# inpt = int(input())
# size_type = None
# if inpt == 3:
#     size_type = 'big'
# elif inpt == 2:
#     size_type = 'medium'
# elif inpt == 1:
#     size_type = 'small'
# else:
#     size_type = 'DNM'
# size=Size(size_type=size_type)
#
# print("What function should plant do?\n3 - decorative\n2 - aromatic\n1 - edible\n0 - Doesn't matter")
# inpt = int(input())
# function_type = None
# if inpt == 3:
#     function_type = 'decorative'
# elif inpt == 2:
#     function_type = 'aromatic'
# elif inpt == 1:
#     function_type = 'edible'
# else:
#     function_type = 'DNM'
# function=Function(function_type=function_type)
#
# print("Does plant need to be non alergic?\n2 - Yes\n1 - No\n\n0 - Doesn't matter")
# inpt = int(input())
# alergic_type = None
# if inpt == 2:
#     alergic_type = 'non_alergic'
# elif inpt == 1:
#     alergic_type = 'alergic'
# else:
#     alergic_type = 'DNM'
# alergic=Alergic(alergic_type=alergic_type)
#
# #TODO-Lista kolorów w GUI
# print("Enter primary colour? DNM - Doesn't matter")
# primary_colour_type = input()
# primary_colour=PrimaryColor(primary_colour_type=primary_colour_type)
#
# print("Enter secondary colour? DNM - Doesn't matter")
# secondary_colour_type = input()
# secondary_colour=SecondaryColor(secondary_colour_type=secondary_colour_type)
#
#
# engine.declare(soil,humidity,insolation,size,function,alergic,primary_colour,secondary_colour)
# engine.run()