class Ref1():
    #fuck1_ = 'ref1 fuck1 global'
    fuck2_ = 'ref1 fuck2 global'
    def __init__(self,a,b):
        print('init ref1 called')
        self.fuck1_ = 'ref1 init fuck '
        self.fuck2_ = 'ref1 fuck2 init'
        print(a,b)
        #None

class Ref2(Ref1):
    #fuck2_ = 'ref2 global fuck2'
    def __init__(self):
        #print(self.fuck1_)
        #self.fuck1_ = 'fuck11'
        super().__init__(1,2)
        
        print(self.fuck2_)
        self.fuck2_ = 'ref 2 init fuck 1'

ref1 = Ref1(1,'suck my cock')
ref2 = Ref2()
print( ref1.fuck1_)
print( ref1.fuck2_)
print( ref2.fuck1_)
print( ref2.fuck2_)
ref2.fuck1_ = 'new ref2 fuck1'
ref2.fuck2_ = 'new ref2 fuck2'
print( ref1.fuck1_)
print( ref1.fuck2_)
print( ref2.fuck1_)
print( ref2.fuck2_)
ref1.fuck1_ = 'new ref1 fuck1'
ref1.fuck2_ = 'new ref1 fuck2'
print( ref1.fuck1_)
print( ref1.fuck2_)
print( ref2.fuck1_)
print( ref2.fuck2_)