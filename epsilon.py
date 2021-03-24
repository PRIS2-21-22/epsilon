class epsilon:
    
    value = [] #trapezoide o triangulo

    def __init__(self, m, a, b, d):
        #triangulo
        if (d==none)
            self.value=[a,b,d]
        else: #trapezoide
            self.value=[self,a,b,d]

    def suma(self,num):
        if (len(self.value)==3 and leng(num.value)==3):
                return [self.value[0] + num.value[0], self.value[1] + num.value[1], self.value[2] + num.value[2]]
          else:
                return [self.value[0] + num.value[0], self.value[1] + num.value[1], self.value[2] + num.value[2], self.value[3] + num.value[3]]

    def resta(self, num):
        if (len(num.value) == 3 and len(self.value) == 3):
            return self.suma(borroso(-num.value[0], -num.value[1], -num.value[2], d=None))
        else:
            return self.suma(borroso(-num.value[0],-num.value[1],-num.value[2],-num.value[3]))

    def op_opuesto(self):
        return
    
    def op_mult(self, num):
        return

    def op_div(self, num):
        return

r1 = borroso(m=0, a=1, b=2, d=3)
r2 = borroso(m=1, a=2, b=0, d=3)
rSuma = r1.suma(r2)
rResta = r1.resta(r2)
print(rResta)