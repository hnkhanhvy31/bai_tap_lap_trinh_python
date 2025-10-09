class canh_hcn:
    canh=0
    def __init__(hcn,cd=0,cr=0):
        hcn.cd=int(cd)
        hcn.cr=int(cr)
    def nhap_canh(hcn):
        while True:
            try:
                cd=int(input("nhap chieu dai: "))
                cr=int(input("nhap chieu rong: "))
                if cd<=0 or cr<=0:
                    print("vui long nhap lai")
            except ValueError:
                print('gia tri khong hop le')
                continue
            else:
                hcn.cd=cd
                hcn.cr=cr
                break
    def chu_vi(hcn):
        return 2*(hcn.cd+hcn.cr)
    def dien_tich(hcn):
        return hcn.cd*hcn.cr
    def thong_tin(hcn):
        print(f"chieu dai hinh chu nhat: {hcn.cd}")
        print(f"chieu rong hinh chu nhat: {hcn.cr}")
        print(f"chu vi hinh chu nhat: {hcn.chu_vi()}")
        print(f"dien tich hinh chu nhat: {hcn.dien_tich()}")
if __name__=='__main__':
    h=canh_hcn()
    h.nhap_canh()
    h.thong_tin()