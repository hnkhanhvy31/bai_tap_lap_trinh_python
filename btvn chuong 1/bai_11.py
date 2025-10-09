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

class tam_giac_can(tam_giac):
    def __init__(self,a,b,c,canhdeu, canhlon):
        super().__init__(a,b,c)
        self.canhdeu=canhdeu
        self.canhlon=canhlon

class tam_giac_deu(tam_giac_can):
    def __init__(self,a,b,c,canhdeu,canhlon,canh):
        super().__init__(self,a,b,c,canhdeu,canhlon)
        self.canh=canh