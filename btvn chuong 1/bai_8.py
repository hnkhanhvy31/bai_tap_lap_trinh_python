class date:
    def __init__(self,day=int,month=int,year=int):
        self.day=day
        self.month=month
        self.year=year
    def nam_nhuan(self):
        return (self.year%4==0 and self.year%100!=0 or self.year%400==0)
    def so_ngay(self):
        if self.month in [4,6,9,11]:
            return 30
        elif self.month==2:
            return 29 if self.nam_nhuan() else 28
        else:
            return 31
    def ngay_tiep_theo(self):
        so_ngay_hien_tai=self.so_ngay()
        if self.day<so_ngay_hien_tai:
            self.day+=1
            return (self.day,self.month,self.year)
        elif self.month<12:
            self.day+=1
            self.month+=1
            return self.day,self.month,self.year
        else:
            self.day+=1
            self.month+=1
            self.year+=1
            return self.day,self.month,self.year
    def display(self):
        print(f"ngay: {self.day}/{self.month}/{self.year}")
        print(f"so nay trong thang do: {self.so_ngay()}")
        print(f"ngay tiep theo: {self.ngay_tiep_theo()}")
        print(f"so nay trong thang do: {self.so_ngay()}")


class Employee:
    def __init__(self,ho_ten=str,ngay_sinh=date,ngay_vao_congty=date):
        self.ho_ten=ho_ten
        self.ngay_sinh=ngay_sinh
        self.ngay_vao_congty=ngay_vao_congty
    def display(self):
        print(f"ho ten nhan vien: {self.ho_ten}")
        print("ngay sinh:",end=" ",)
        self.ngay_sinh.display()
        print("ngay vao cong ty:",end=" ")
        self.ngay_vao_congty.display()

ns=date(day=6,month=2,year=2000)
nv=date(day=1,month=1,year=2024)
h=Employee("alice",ns,nv)
h.display()