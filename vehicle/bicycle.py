#自行车
import math


class Bicycle:
    def run(self,km):
        print(f"骑行{km} km")

class EBicycle(Bicycle):
    battery_level : int
    def __init__(self,vol):  #__inin__为构造器，如果没有将调用不了之类
        self.battery_level = vol    #vol为电量

    def fill_cha(self,vvv):    #vvv为充电
        self.battery_level = self.battery_level + vvv

    def run(self,km):
        miles =  10 * self.battery_level- km
        miles1 = self.battery_level - km / 10
        if miles > 0:
            print("电量够用")
            print(f"骑行了{km}km")
            print(f"还剩下{miles1}电量")
        else:

            print("电量不够用")
            print(f"骑行了{10 * self.battery_level}km")
            print(f"还需要脚蹬{math.fabs(miles)}km")

p1 = EBicycle(10)
p1.fill_cha(10)
p1.run(3)
