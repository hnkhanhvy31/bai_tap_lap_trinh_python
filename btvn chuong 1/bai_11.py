class tam_giac:
    def __init__(self, a,b,c):
        if a<=0 or b<=0 or c<=0:
            raise ValueError("do dai canh phai lon hon 0")
        if not (a+b>c and b+c>a and a+c>b):
            raise ValueError("3 canh khong tao thanh 1 tam giac")
        self.a=a
        self.b=b
        self.c=c

class tam_giac_vuong(tam_giac):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    def dien_tich(self):    
        if self.a**2+self.b**2==self.c**2:
            return self.a*self.b
        if self.a**2+self.c**2==self.b**2:
            return self.a*self.c
        if self.c**2+self.b**2==self.a**2:
            return self.b*self.c
        else:
            print("khong tam giac vuong")
    def display(self):
        print(self.dien_tich())
class tam_giac_can(tam_giac):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    def dien_tich(self):
        if self.a==self.b:
            pass
class tam_giac_deu(tam_giac_can):
    def __init__(self,a,b,c,canhdeu,canhlon,canh):
        super().__init__(self,a,b,c,canhdeu,canhlon)
        self.canh=canh