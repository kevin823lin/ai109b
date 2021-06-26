# 第九周筆記

## 神經網路

在電腦領域，神經網路是指一種模擬神經系統所設計出來的程式，用來模擬人類視覺、聽覺等等智慧行為的原理，企圖讓電腦可以具有人類智慧的一種方法。

### 神經元

* 神經元示意圖
  ![神經元示意圖](../img/神經元示意圖.png)

  * a1~an 為輸入向量的各個分量
  * w1~wn 為神經元各個突觸的權值
  * b 為偏置
  * f 為傳遞函式，通常為非線性函式。一般有 traingd(), tansig(), hardlim()。以下預設為 hardlim()
  * t 為神經元輸出

### 神經元網路

* 單層神經元網路

    單層神經元網路是最基本的神經元網路形式，由有限個神經元構成，所有神經元的輸入向量都是同一個向量。由於每一個神經元都會產生一個純量結果，所以單層神經元的輸出是一個向量，向量的維數等於神經元的數目。

  * 單層神經元網路示意圖

    ![單層神經元網路示意圖](../img/單層神經元網路示意圖.png)

## 從微分到梯度下降法

### 微分 (單變數)

* [diff.py](https://gitlab.com/ccc109/ai/-/tree/master/07-neural/02-gradient/01-diff/diff.py)

    ```python
    def diff(f, x):
        df = f(x+dx)-f(x)
        return df/dx
    ```

### 偏微分 (多變數)

* [npGradient.py](https://gitlab.com/ccc109/ai/-/tree/master/07-neural/02-gradient/02-gradient/npGradient.py)

    ```python
    # 函數 f 對變數 p[k] 的偏微分: df / dp[k]
    def df(f, p, k):
        p1 = p.copy()
        p1[k] = p[k]+step
        return (f(p1) - f(p)) / step
    ```

### 梯度

* [npGradient.py](https://gitlab.com/ccc109/ai/-/tree/master/07-neural/02-gradient/02-gradient/npGradient.py)

    ```python
    # 函數 f 在點 p 上的梯度
    def grad(f, p):
        gp = p.copy()
        for k in range(len(p)):
            gp[k] = df(f, p, k)
        return gp
    ```

### 梯度下降法

* [gd1.py](https://gitlab.com/ccc109/ai/-/tree/master/07-neural/02-gradient/03-gd/gd1.py)

    ```python
    # 使用梯度下降法尋找函數最低點
    def gradientDescendent(f, p0, step=0.01):
        p = p0.copy()
        i = 0
        while (True):
            i += 1
            fp = f(p)
            gp = grad(f, p) # 計算梯度 gp
            glen = norm(gp) # norm = 梯度的長度 (步伐大小)
            print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
            if glen < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
                break
            gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
            p +=  gstep # 向 gstep 方向走一小步
        return p # 傳回最低點！
    ```

### 反傳遞演算法

* [net.py](https://gitlab.com/ccc109/ai/-/tree/master/07-neural/02-gradient/04-net/net.py)

    ```python
    class Gate:
        # ...
        def backward(self):
            x, y, o, gfx, gfy = self.x, self.y, self.o, self.gfx, self.gfy
            x.g += gfx(x.v,y.v) * o.g
            y.g += gfy(x.v,y.v) * o.g
        # ...

    class Net:
        # ...
        def backward(self): # 反向傳遞計算梯度 
            self.o.g = 1 # 設定輸出節點 o 的梯度為 1
            for gate in reversed(self.gates): # 反向傳遞計算每個節點 Node 的梯度 g
                gate.backward()
        # ...

    ```

## 梯度下降法

![梯度下降法](../img/Gradient.jpg)

* 要使用梯度下降法找到一個函數的局部極小值，必須向函數上當前點對應梯度（或者是近似梯度）的反方向的規定步長距離點進行疊代搜索。如果相反地向梯度正方向疊代進行搜索，則會接近函數的局部極大值點；這個過程則被稱為梯度上升法。

* 梯度就是斜率最大的那個方向，所以梯度下降法，其實就是朝著斜率最大的方向走。

### 實作

* 執行 `diff.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\02-gradient\01-diff> python .\diff.py    
    diff(f,2)= 12.006000999997823
    ```

* 執行 `e.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\02-gradient\01-diff> python .\e.py         
    n= 100.0 e(n)= 2.7048138294215285
    n= 200.0 e(n)= 2.711517122929317  
    n= 300.0 e(n)= 2.7137651579427837 
    .
    .
    .
    n= 9800.0 e(n)= 2.718143153583405
    n= 9900.0 e(n)= 2.718144554210053
    n= 10000.0 e(n)= 2.7181459268249255
    ```

* 執行 `gdNumber.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\02-gradient\03-gd> python .\gdNumber.py
    1:p=[1.0] f(p)=3.000 gp=[-2.010000000000023] glen=2.01000
    2:p=[1.0201] f(p)=2.959 gp=[-2.0502] glen=2.05020
    3:p=[1.040602] f(p)=2.917 gp=[-2.091204] glen=2.09120
    .
    .
    .
    35:p=[1.96547941] f(p)=0.137 gp=[-3.94095882] glen=3.94096
    36:p=[2.004889] f(p)=0.020 gp=[4.019778] glen=4.01978
    37:p=[1.96469122] f(p)=0.140 gp=[-3.93938244] glen=3.93938
    ```

* 執行 `gdGate.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\02-gradient\03-gd> python .\gdGate.py  
    2999:p=[ 1.70833465  1.70833465 -2.7326384 ] f(p)=0.506 gp=[-0.04493286 -0.04493286  0.06420767] glen=0.09034
    o0=0.061 o1=0.264 o2=0.264 o3=0.665
    ```

## 參考資料

* <https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C>

* <https://zh.wikipedia.org/zh-tw/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95>

* <https://gitlab.com/ccc109/ai/-/blob/master/07-neural/02-gradient/%E5%BE%9E%E5%BE%AE%E5%88%86%E5%88%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95.md>

* <https://gitlab.com/ccc109/ai/-/blob/master/07-neural/02-gradient/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95.md>
