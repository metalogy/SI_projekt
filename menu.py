from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from main import PlantSelection, plants_container
from rules import *



class Menu(Screen):

    ph = None
    hum = None
    ins = None
    size = None
    fun = None
    alg = None
    col = None
    col1 = None
    eng = PlantSelection()

    def __init__(self, **kw):
        super().__init__(**kw)

    def read_ph(self, v):
        self.ph = v

    def read_hum(self, v):
        self.hum = v

    def read_ins(self, v):
        self.ins = v

    def read_size(self, v):
        self.size = v

    def read_fun(self, v):
        self.fun = v

    def read_alg(self, v):
        self.alg = v

    def read_col(self, v):
        self.col = v

    def read_col1(self, v):
        self.col1 = v

    def propose(self):

        self.eng.reset()
        #print(self.ph, self.hum, self.ins, self.size, self.fun, self.alg, self.col, self.col1)  # debug
        soil = SoilPH(soil_ph=str(self.ph))
        hum = Humidity(humidity_type=str(self.hum))
        ins = Insolation(insolation_type=str(self.ins))
        size = Size(size_type=str(self.size))
        fun = Function(function_type=str(self.fun))
        alg = Alergic(alergic_type=str(self.alg))
        pri = PrimaryColor(primary_colour_type=str(self.col))
        sec = SecondaryColor(secondary_colour_type=str(self.col1))
        self.eng.declare(soil, hum, ins, size, fun, alg, pri, sec)

        self.eng.run() #ZAWSZE ZWRACA NONE
        if plants_container is not None:
            data='Ideal plants to plant in your garden will be:\n'
            for plant in plants_container:
                data+='\n'+plant.plant_name+'\n'+plant.plant_description+'\n\n'
                self.ids.res.text=data
            print(data) #DEBUG
        else:
            self.ids.res.text = "Unfortunately, there is no plant in our database,\n which satisfies your requirements."
        plants_container.clear()


class GardenApp(App):

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Menu(name="menu"))
        return manager


if __name__ == '__main__':
    GardenApp().run()
