import time
import colorama
from colorama import Fore

colorama.init()


# Очень хотелось по практиковаться с графикой, но очень не хватает времени

class TrafficLight:
    __traffic_light_color = 'Светофор'

    def switching_lights(elf):
        while True:
            print(Fore.RED + 'Красный свет')
            time.sleep(7)
            print(Fore.YELLOW + 'Желтый свет')
            time.sleep(2)
            print(Fore.GREEN + 'Зеленый свет')
            time.sleep(7)
            print(Fore.YELLOW + 'Желтый свет')
            time.sleep(2)


a = TrafficLight()
a.switching_lights()
