import math
class Diem:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def display(self):
        print(f"tam: ({self.x},{self.y})")

class elip(Diem):
    def __init__(self,x=0,y=0,r_be=0.5,r_lon=1):
        super().__init__(x,y)
        self.r_be=r_be
        self.r_lon=r_lon
    def dien_tich(self):
        return math.pi*self.r_lon*self.r_be
    def chu_vi(self):
        return math.pi*(3*(self.r_lon+self.r_be)-((3*self.r_lon+self.r_be)+(self.r_lon+3*self.r_be))**(1/2)) 
    def display(self):
        print(f"chu vi elip: {self.chu_vi()}")
        print(f"dien tich elip: {self.dien_tich()}")

class duong_tron(elip):
    def __init__(self,x=0,y=0,r_lon=1,r_be=0.5,bankinh=0.5):
        super().__init__(x,y,r_lon,r_be)
        self.bankinh=bankinh
    def chu_vi(self):
        return 2*math.pi*self.bankinh
    def dien_tich(self):
        return math.pi*self.bankinh**2
    def display(self):
        print(f"chu hinh tron: {self.chu_vi()}")
        print(f"dien tich hinh tron: {self.dien_tich()}")