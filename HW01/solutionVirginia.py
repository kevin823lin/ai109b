from solution import Solution
from virginia import *
from random import random, randint

class solutionVirginia(Solution):
    def neighbor(self):           #  多變數解答的鄰居函數。
        nv = self.v.copy()        #  nv=v.clone()=目前解答的複製品
        i = randint(0, len(nv)-1) #  隨機選取一個變數
        if (random() > 0.5):      #  擲骰子決定要往左或往右移
            nv[i] += self.step
        else:
            nv[i] -= self.step
        return solutionVirginia(nv)  #  傳回新建的鄰居解答。

    def height(self): #  能量函數
        x, y, z = self.v
        plain = "This is a book. That is a cat. I am a boy. One of my boy go to school today."
        key = [0,2,4]
        etext = encrypt(plain, key)
        dtext = decrypt(etext, [x, y, z])
        return fit(dtext)

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v), self.height())


