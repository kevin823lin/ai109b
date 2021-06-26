# 第二周筆記

## 爬山演算法

### 架構

* 爬山演算法框架 `hillClimbing.py`

    ```python
    def hillClimbing(s, maxGens, maxFails):   # 爬山演算法的主體函數
        print("start: ", s.str())             # 印出初始解
        fails = 0                             # 失敗次數設為 0
        # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
        for gens in range(maxGens):
            snew = s.neighbor()               #  取得鄰近的解
            sheight = s.height()              #  sheight=目前解的高度
            nheight = snew.height()           #  nheight=鄰近解的高度
            if (nheight >= sheight):          #  如果鄰近解比目前解更好
                print(gens, ':', snew.str())  #    印出新的解
                s = snew                      #    就移動過去
                fails = 0                     #    移動成功，將連續失敗次數歸零
            else:                             #  否則
                fails = fails + 1             #    將連續失敗次數加一
            if (fails >= maxFails):
                break
        print("solution: ", s.str())          #  印出最後找到的那個解
        return s                              #    然後傳回。
    ```

* 解答框架 `solution.py`

    ```python
    class Solution: # 解答的物件模版 (類別)
        def __init__(self, v, step = 0.01):
            self.v = v       # 參數 v 為解答的資料結構
            self.step = step # 每一小步預設走的距離

        # 以下兩個函數至少需要覆蓋掉一個，否則會無窮遞迴
        def height(self): # 爬山演算法的高度函數
            return -1*self.energy()               # 高度 = -1 * 能量

        def energy(self): # 尋找最低點的能量函數
            return -1*self.height()               # 能量 = -1 * 高度
    ```

### 實作

* 求 ![equation](https://latex.codecogs.com/svg.latex?\left&space;|&space;x^2-4&space;\right&space;|) 最低點

  * 執行 `hillClimbingNumber.py`

    > 當 x = 2 時，![equation](https://latex.codecogs.com/svg.latex?\left&space;|&space;x^2-4&space;\right&space;|) 有最小值為 0

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\04-framework> python .\hillClimbingNumber.py
    start:  energy(0.000)=4.000
    0 : energy(0.010)=4.000 
    1 : energy(0.020)=4.000 
    3 : energy(0.030)=3.999 
    6 : energy(0.040)=3.998 
    7 : energy(0.050)=3.998 
    .
    .
    .
    413 : energy(1.960)=0.158
    414 : energy(1.970)=0.119
    416 : energy(1.980)=0.080
    418 : energy(1.990)=0.040
    419 : energy(2.000)=0.000
    solution:  energy(2.000)=0.000
    ```

  * 解答框架 `solutionNumber.py`

    ```python
    from hillClimbing import hillClimbing # 引入解答類別
    from solution import Solution
    import random

    class SolutionNumber(Solution):
        def neighbor(self): # 單變數解答的鄰居函數。
            x = self.v
            dx= self.step               # x:解答 , dx : 移動步伐大小
            xnew = x+dx if random.random() > 0.5 else x-dx # 用亂數決定向左或向右移動
            return SolutionNumber(xnew) # 建立新解答並傳回。

        def energy(self):               # 能量函數
            x = self.v                  # x:解答
            return abs(x*x-4)           # 能量函數為 |x^2-4|

        def str(self): # 將解答轉為字串，以供印出觀察。
            return "energy({:.3f})={:.3f}".format(self.v, self.energy())
    ```

* 求 ![equation](https://latex.codecogs.com/svg.latex?x^2&plus;3y^2&plus;z^2-4x-3y-5z&plus;8) 最低點

  * 執行 `hillClimbingArray.py`

    > 當 ![equation](https://latex.codecogs.com/svg.latex?\\begin{pmatrix}&space;x=2\\\\&space;y=5\\\\&space;z=2.5&space;\\end{pmatrix}) 時，![equation](https://latex.codecogs.com/svg.latex?x^2&plus;3y^2&plus;z^2-4x-3y-5z&plus;8) 有最小值為 -3

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\04-framework> python .\hillClimbingArray.py
    start:  energy([1, 1, 1])=1.000000
    2 : energy([1, 0.99, 1])=0.970300       
    3 : energy([1, 0.99, 1.01])=0.940400    
    4 : energy([1, 0.98, 1.01])=0.911300    
    5 : energy([1, 0.97, 1.01])=0.882800    
    6 : energy([1.01, 0.97, 1.01])=0.862900 
    .
    .
    .
    874 : energy([2.000000000000001, 0.49999999999999956, 2.459999999999991])=-2.998400
    879 : energy([2.000000000000001, 0.49999999999999956, 2.469999999999991])=-2.999100
    907 : energy([2.000000000000001, 0.49999999999999956, 2.4799999999999907])=-2.999600
    911 : energy([2.000000000000001, 0.49999999999999956, 2.4899999999999904])=-2.999900
    919 : energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
    solution:  energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
    ```

  * 解答框架 `solutionArray.py`

    ```python
    from solution import Solution
    from random import random, randint

    class SolutionArray(Solution):
        def neighbor(self):           #  多變數解答的鄰居函數。
            nv = self.v.copy()        #  nv=v.clone()=目前解答的複製品
            i = randint(0, len(nv)-1) #  隨機選取一個變數
            if (random() > 0.5):      #  擲骰子決定要往左或往右移
                nv[i] += self.step
            else:
                nv[i] -= self.step
            return SolutionArray(nv)  #  傳回新建的鄰居解答。

        def energy(self): #  能量函數
            x, y, z =self.v
            return x*x+3*y*y+z*z-4*x-3*y-5*z+8 #  (x^2+3y^2+z^2-4x-3y-5z+8)

        def str(self):    #  將解答轉為字串的函數，以供列印用。
            return "energy({:s})={:f}".format(str(self.v), self.energy())
    ```

* 求 ![equation](https://latex.codecogs.com/svg.latex?\\left\\{\\begin{matrix}&space;4a&plus;3b&plus;6c=1&space;\\\\&space;1a&plus;1b&plus;2c=2&space;\\\\&space;2a&plus;1b&plus;3c=-1&space;\\end{matrix}\\right.) 最低點

  * 執行 `hillClimbingEquation.py`

    > 當 ![equation](https://latex.codecogs.com/svg.latex?\\begin{pmatrix}&space;x=-5\\\\&space;y=3\\\\&space;z=2&space;\\end{pmatrix}) 時，![equation](https://latex.codecogs.com/svg.latex?\\left\\{\\begin{matrix}&space;4a&plus;3b&plus;6c=1&space;\\\\&space;1a&plus;1b&plus;2c=2&space;\\\\&space;2a&plus;1b&plus;3c=-1&space;\\end{matrix}\\right.) 有最小值為 0

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\04-framework> python .\hillClimbingEquation.py
    .
    .
    .
    6114 : energy([[-4.99642621  3.00078503  1.997283  ]])=0.001151
    7099 : energy([[-4.99760248  3.00055835  1.99814385]])=0.000797
    7461 : energy([[-5.00007407  3.00055835  1.99971729]])=0.000547
    7658 : energy([[-4.99986312  3.00055835  1.99971729]])=0.000542
    7993 : energy([[-4.99997407  3.00055835  1.99966655]])=0.000456
    solution:  energy([[-4.99997407  3.00055835  1.99966655]])=0.000456
    ```

  * 解答框架 `solutionEquation.py`

    ```python
    """
    A X = B ，求 X 是多少？

    範例：題目來源: http://mail.im.tku.edu.tw/~idliaw/LinTup/99ie/99IEntu.pdf

    4a+3b+6c=1
    1a+1b+2c=2
    2a+1b+3c=-1
    """

    from random import random, randint
    import numpy as np
    from numpy import linalg as LA
    from solution import Solution

    A = np.array([[4,3,6],[1,1,2],[2,1,3]])
    B = np.array([[1,2,-1]]).transpose()

    class SolutionEquation(Solution):
        def neighbor(self):    #  多變數解答的鄰居函數。
            nx = self.v.copy()              #  複製目前解的矩陣
            rows = nx.shape[0]
            #  修改了這裡：最多改變 n 個維度(只是某些 n 維的例子可以，無法確定一定可以，除非能證明能量函數只有一個低點)
            for _ in range(rows):         #  原本只改一維，會找不到！
                i = randint(0, rows-1) #  隨機選取一個變數
                if (random() > 0.5):                    #  擲骰子決定要往左或往右移
                    nx[i][0] += self.step * random()  #  原本是 nx.m[i][0] += self.step 
                else:
                    nx[i][0] -= self.step * random()  #  原本是 nx.m[i][0] -= self.step 

            return SolutionEquation(nx)                    #  傳回新建的鄰居解答。

        def energy(self):      #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
            X = self.v
            Y = A.dot(X)
            return LA.norm(Y-B, 2)

        def str(self):    #  將解答轉為字串的函數，以供列印用。
            return "energy({:s})={:f}".format(str(self.v.transpose()), self.energy())

        @classmethod
        def zero(cls):
            return SolutionEquation(np.zeros((3,1)))
    ```

* 求最佳課表（分數最高點）

  * 執行 `hillClimbingScheduling.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\04-framework> python .\hillClimbingScheduling.py | sls score
    start:  score=27.200000 
    0 : score=27.200000 
    1 : score=27.200000 
    4 : score=25.200000 
    5 : score=25.200000 
    .
    .
    .
    29913 : score=-3.900000 
    29934 : score=-3.900000 
    29964 : score=-3.900000 
    solution:  score=-3.900000 

    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\04-framework> python .\hillClimbingScheduling.py
    start:  score=33.000000 
    A11:系統 A12:科學 A13:智慧 A14:網頁 A15:離散 A16:智慧 A17:軟工 
    A21:離散 A22:視窗 A23:動畫 A24:智慧 A25:智慧 A26:行動 A27:軟工 
    A31:工數 A32:計概 A33:嵌入 A34:電子 A35:動畫 A36:計概 A37:軟工 
    A41:離散 A42:線代 A43:電子 A44:嵌入 A45:機率 A46:智慧 A47:視窗 
    A51:媒體 A52:線代 A53:系統 A54:動畫 A55:網頁 A56:機率 A57:機率 
    B11:離散 B12:視窗 B13:計概 B14:網站 B15:　　 B16:線代 B17:行動 
    B21:工數 B22:動畫 B23:網頁 B24:視窗 B25:結構 B26:軟工 B27:科學 
    B31:離散 B32:網路 B33:網頁 B34:電子 B35:視窗 B36:媒體 B37:智慧 
    B41:線代 B42:嵌入 B43:行動 B44:嵌入 B45:嵌入 B46:電子 B47:電子 
    B51:線代 B52:科學 B53:　　 B54:機率 B55:行動 B56:離散 B57:視窗
    .
    .
    .
    solution:  score=-3.900000 
    A11:　　 A12:媒體 A13:媒體 A14:媒體 A15:工數 A16:工數 A17:工數 
    A21:　　 A22:網頁 A23:網頁 A24:網頁 A25:電子 A26:機率 A27:機率 
    A31:　　 A32:視窗 A33:視窗 A34:視窗 A35:網路 A36:網路 A37:網路 
    A41:　　 A42:動畫 A43:動畫 A44:動畫 A45:計概 A46:計概 A47:計概 
    A51:　　 A52:科學 A53:科學 A54:科學 A55:智慧 A56:智慧 A57:智慧 
    B11:　　 B12:系統 B13:系統 B14:系統 B15:軟工 B16:軟工 B17:軟工 
    B21:　　 B22:演算 B23:演算 B24:演算 B25:電子 B26:電子 B27:電子 
    B31:　　 B32:結構 B33:結構 B34:結構 B35:離散 B36:離散 B37:離散 
    B41:　　 B42:嵌入 B43:嵌入 B44:嵌入 B45:網站 B46:網站 B47:網站 
    B51:　　 B52:行動 B53:行動 B54:行動 B55:線代 B56:線代 B57:線代
    ```

  * 解答框架 `solutionScheduling.py`

    ```python
    from random import random, randint, choice
    from solution import Solution
    import numpy as np

    courses = [...] # 定義課程教師、名稱、班級

    teachers = ['甲', '乙', '丙', '丁', '戊']

    rooms = ['A', 'B']

    slots = [...] # 定義課表格式

    cols = 7

    def randSlot() :
        return randint(0, len(slots)-1)

    def randCourse() :
        return randint(0, len(courses)-1)


    class SolutionScheduling(Solution) :
        def neighbor(self):    # 單變數解答的鄰居函數。
            fills = self.v.copy()
            choose = randint(0, 1)
            if choose == 0: # 任選一個改變 
                i = randSlot()
                fills[i] = randCourse()
            elif choose == 1: # 任選兩個交換
                i = randSlot()
                j = randSlot()
                t = fills[i]
                fills[i] = fills[j]
                fills[j] = t
            return SolutionScheduling(fills)                  # 建立新解答並傳回。

        def height(self) :      # 高度函數
            courseCounts = [0] * len(courses)
            fills = self.v
            score = 0
            # courseCounts.fill(0, 0, courses.length)
            for si in range(len(slots)):
                courseCounts[fills[si]] += 1
                #                        連續上課:好                   隔天:不好     跨越中午:不好
                if si < len(slots)-1 and fills[si] == fills[si+1] and si%7 != 6 and si%7 != 3:
                    score += 0.1
                if si % 7 == 0 and fills[si] != 0: # 早上 8:00: 不好
                    score -= 0.12
            
            for ci in range(len(courses)):
                if (courses[ci]['hours'] >= 0):
                    score -= abs(courseCounts[ci] - courses[ci]['hours']) # 課程總時數不對: 不好
            return score

        def str(self) :    # 將解答轉為字串，以供印出觀察。
            outs = []
            fills = self.v
            for i in range(len(slots)):
                c = courses[fills[i]]
                if i%7 == 0:
                    outs.append('\n')
                outs.append(slots[i] + ':' + c['name'])
            return 'score={:f} {:s}\n\n'.format(self.energy(), ' '.join(outs))
        
        @classmethod
        def init(cls):
            fills = [0] * len(slots)
            for i in range(len(slots)):
                fills[i] = randCourse()
            return SolutionScheduling(fills)

    ```

* 模擬退火法

  * 簡介

    避免因為局部最低而放棄全域最低

  * 虛擬碼

    ```text
    Algorithm SimulatedAnnealing(s)
      while (溫度還不夠低，或還可以找到比 s 更好的解 s' 的時候)
          根據能量差與溫度，用機率的方式決定是否要移動到新解 s'。
          # (機率：溫度高時可以往上走，溫度低的時候差不多只能往下走)
          將溫度降低一些
      end
    end
    ```

## 參考資料

* <https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github>

* <http://programmermedia.org/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-optimize/01-hillclimbing/04-framework/%E5%AF%A6%E4%BD%9C%EF%BC%9A%E9%80%9A%E7%94%A8%E7%9A%84%E6%A8%A1%E6%93%AC%E9%80%80%E7%81%AB%E6%B3%95%E6%9E%B6%E6%A7%8B.md>