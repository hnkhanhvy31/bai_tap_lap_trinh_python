class da_giac:
    def chu_vi(self):
        pass
    def dien_tich(self):
        pass

class hinh_binh_hanh(da_giac):
    def __init__(self,canh_ben, canh_day, chieucao):
        self.canh_ben=canh_ben
        self.canh_day=canh_day
        self.chieucao=chieucao
    def chu_vi(self):
        return 2*(self.canh_ben+self.canh_day)
    def dien_tich(self):
        return self.canh_day*self.chieucao
    
class hcn(hinh_binh_hanh):
    def __init__(self,chieu_dai,chieu_rong,canh_ben,canh_day,chieucao):
        super().__init__(canh_ben,canh_day,chieucao)
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong
    def chu_vi(self):
        return 2*(self.chieu_dai+self.chieu_rong)
    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    
class hv(hcn):
    def __init__(self,canh,canh_ben,canh_day,chieucao,chieu_dai,chieu_rong):
        super().__init__(canh_ben,canh_day,chieucao,chieu_dai,chieu_rong)
        self.canh=canh
    def chu_vi(self):
        return 4*self.canh
    def dien_tich(self):
        return self.canh*self.canh
    
#hinh binh hanh
canh_ben=int(input("nhap canh ben cua hbh: "))
canh_day=int(input("nhap canh ben cua hbh: "))
chieucao=int(input("nhap chieu cao cua hbh: "))
hbh=hinh_binh_hanh(canh_ben,canh_day,chieucao)
print(f"chu vi cua hinh binh hanh la: {hbh.chu_vi()}")
print(f'dien tich cua hinh binh hanh la: {hbh.dien_tich()}')

#hinh chu nhat
chieu_dai=int(input("nhap chieu dai cua hinh chu nhat: "))
chieu_rong=int(input("nhap chieu rong cua hinh chu nhat: "))
hinh_cn=hcn(chieu_dai,chieu_rong,canh_ben,canh_day,chieucao)
print(f"chu vi hinh chu nhat la: {hinh_cn.chu_vi()}")
print(f"dien tich hinh chu nhat la: {hinh_cn.dien_tich()}")

#hinh vuong
canh=int(input("nhap canh cua hinh vuong: "))
hinh_v=hv(canh,chieu_dai,chieu_rong,canh_ben,canh_day,chieucao)
print(f"chu vi cua hinh vuong: {hv.chu_vi()}")
print(f"dien tich hinh vuong la: {hv.dien_tich()}")