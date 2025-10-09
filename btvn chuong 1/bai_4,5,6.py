class stack:
    def __init__(self,so_phantu):
        self.so_phantu= so_phantu
        self.data=[]
    def isEmpty(self):
        len(self.data)==0
    def isFull(self):
        len(self.data)==self.so_phantu
    def push(self,phantu):
        if self.isFull():
            print("ngan da day, khong the cho them")
        else:
            self.data.append(phantu)
    def pop(self,phantu):
        if self.isEmpty():
            print("ngan rong, khong the rut")
            return None
        else:
            return self.data.pop()
    def count(self):
        return len(self.data)
    def __del__(self):
        del(self.data)
    def in_nd(self):
        if self.isEmpty():
            print("ngan xep rong")
        else:
            print('noi dung ngan xep', self.data)
h=stack(5)
h.push(1)      
h.push(2) 
h.push(3) 
h.push(4) 
h.push(5) 
