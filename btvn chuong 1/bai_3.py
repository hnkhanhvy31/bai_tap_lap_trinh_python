class phan_so:
    ps=0
    def __init__(phanso,tu_so=0,mau_so=0):
        phanso.tu_so=int(tu_so)
        phanso.mau_so=int(mau_so)
    def nhap(phanso):
        while True:
            try:
                tu_so=int(input('nhap tu so: '))
                mau_so=int(input('nhap mau so: '))
                if mau_so<=0:
                    print('vui long nhap lai')
                    continue
            except ValueError:
                print('vui long nhap gia tri khac')
            else:
                phanso.tu_so=int(tu_so)
                phanso.mau_so=int(mau_so)
                break
    def in_phanso(phanso):
        print(f'phan so: {phanso.tu_so}/{phanso.mau_so}')
h=phan_so()
h.nhap()
h.in_phanso()

