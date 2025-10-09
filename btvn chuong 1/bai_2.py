class self:
    thisinh=0
    def __init__(self,ho_ten,diem_toan=0,diem_ly=0,diem_hoa=0):
        self.ho_ten=ho_ten
        self.diem_toan=float(diem_toan)
        self.diem_ly=float(diem_ly)
        self.diem_hoa=float(diem_hoa)
    def nhap_thongtin(self):
        ho_ten=input("nhap ho ten thi sinh: ")
        while True:
            try:
                diem_toan=float(input('nhap diem toan: '))
                diem_ly=float(input('nhap diem ly: '))
                diem_hoa=float(input('nhap diem hoa: '))
                if diem_toan<=0 or diem_hoa<=0 or diem_ly<=0:
                    print("vui long nhap lai")
                    continue
            except ValueError:
                print("vui long nhap lai gia tri")
            else:
                self.ho_ten=ho_ten
                self.diem_toan=float(diem_toan)
                self.diem_ly=float(diem_ly)
                self.diem_hoa=float(diem_hoa)
                break
    def tong_diem(self):
        return self.diem_ly+self.diem_hoa+self.diem_toan
    def self_trung_tuyen(self):
        if self.tong_diem()>=20:
            print("thi sinh trung tuyen")
        else:
            print("thi sinh khong trung tuyen")
    def in_thong_tin(self):
        print(f"ten thi sinh: {self.ho_ten}")
        print(f"diem toan: {self.diem_toan}, diem ly: {self.diem_ly}, diem hoa: {self.diem_hoa}")
        print(f"{self.self_trung_tuyen}")
h=self("a")
h.nhap_thongtin()
h.in_thong_tin()
        