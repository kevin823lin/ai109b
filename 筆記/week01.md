# 第一周筆記

## 人工智慧現況

1. 人工智慧的領域著重於電腦算力，一般電腦在人工智慧的領域非常龜速

2. 人工智慧分成

   * 傳統模式
     * 搜尋與優化

   * 機器學習
      * 統計
      * 神經網路 ── 深度學習

3. 人工智慧最近因為深度學習而重新熱門起來

4. 許多訓練出的模型也被驗證出來是有效的

   * CNN
   * RNN
   * LSTM
   * BERT
5. 傳統模式的搜尋方式是解空間搜尋法，如下棋的 Min-Max

## 人工智慧應用

* 影像辨識
  * 傳統模式
    * 特徵擷取
  * 深度學習(CNN/Yolo)
    * 不抽特徵，全部透過梯度下降法，找到錯誤率最低的模型

## 實作

### 爬山演算法

* 方法：看左右有無高點
  * 若有高點就有高點就移過去
  * 若無高點，該點即為最高點

* 缺點：若有多個山峰，找到的點為「區域最佳解」，不一定為「全域最佳解」

#### 一維

* 程式

  hillClimbing1.py

  ```python
  # 簡易爬山演算法 -- 針對單變數函數
  def hillClimbing(f, x, dx=0.01):
      while (True):
          print('x={0:.5f} f(x)={1:.5f}'.format(x, f(x)))
          if f(x+dx)>f(x): # 如果右邊的高度 f(x+dx) > 目前高度 f(x) ，那麼就往右走
              x = x + dx
          elif f(x-dx)>f(x): # 如果左邊的高度 f(x-dx) > 目前高度 f(x) ，那麼就往左走
              x = x - dx
          else: # 如果兩邊都沒有比現在的 f(x) 高，那麼這裡就是區域最高點，直接中斷傳回
              break
      return x

  # 高度函數
  def f(x):
      return -1*(x*x-2*x+1)
      # return -1*(x*x+3*x+5)
      # return -1*abs(x*x-4)

  # 呼叫爬山演算法
  hillClimbing(f, 0) # 以 x=0 為起點，開始呼叫爬山演算法
  ```

* 結果

  ```text
  PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\02-var1> python .\hillClimbing1.py
  x=0.00000 f(x)=-1.00000
  x=0.01000 f(x)=-0.98010
  x=0.02000 f(x)=-0.96040
  x=0.03000 f(x)=-0.94090
  x=0.04000 f(x)=-0.92160
  .
  .
  .
  x=0.96000 f(x)=-0.00160
  x=0.97000 f(x)=-0.00090
  x=0.98000 f(x)=-0.00040
  x=0.99000 f(x)=-0.00010
  x=1.00000 f(x)=-0.00000
  ```

#### 二維

* 固定調整法

  * 程式

    hillClimbing2.py

    ```python
    import random

    def hillClimbing(f, x, y, h=0.01):
        while (True):
            fxy = f(x, y)
            print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
            if f(x+h, y) >= fxy: # 如果左邊的高度 f(x+h, y) >= 目前高度 fxy ，那麼就往左走
                x = x + h
            elif f(x-h, y) >= fxy: # 如果右邊的高度 f(x-h, y) >= 目前高度 fxy ，那麼就往右走
                x = x - h
            elif f(x, y+h) >= fxy: # 如果前面的高度 f(x, y+h) >= 目前高度 fxy ，那麼就往前走
                y = y + h
            elif f(x, y-h) >= fxy: # 如果後面的高度 f(x, y-h) >= 目前高度 fxy ，那麼就往後走
                y = y - h
            else: # 如果四邊都沒有比現在的 fxy 高，那麼這裡就是區域最高點，直接中斷傳回
                break
        return (x,y,fxy)

    def f(x, y):
        return -1 * ( x*x - 2*x + y*y + 2*y - 8 )

    hillClimbing(f, 0, 0)
    ```

  * 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\03-var2> python .\hillClimbing2.py
    x=0.000 y=0.000 f(x,y)=8.000
    x=0.010 y=0.000 f(x,y)=8.020
    x=0.020 y=0.000 f(x,y)=8.040
    x=0.030 y=0.000 f(x,y)=8.059
    x=0.040 y=0.000 f(x,y)=8.078
    .
    .
    .
    x=1.000 y=-0.960 f(x,y)=9.998
    x=1.000 y=-0.970 f(x,y)=9.999
    x=1.000 y=-0.980 f(x,y)=10.000
    x=1.000 y=-0.990 f(x,y)=10.000
    x=1.000 y=-1.000 f(x,y)=10.000
    ```

* 隨機調整法

  > 可擴充到 n 維

  * 程式

    hillClimbing2r.py

    ```python
    import random

    def hillClimbing(f, x, y, h=0.01):
        failCount = 0                    # 失敗次數歸零
        while (failCount < 10000):       # 如果失敗次數小於一萬次就繼續執行
            fxy = f(x, y)                # fxy 為目前高度
            dx = random.uniform(-h, h)   # dx 為左右偏移量
            dy = random.uniform(-h, h)   # dy 為前後偏移量
            if f(x+dx, y+dy) >= fxy:     # 如果移動後高度比現在高
                x = x + dx               #   就移過去
                y = y + dy
                print('x={:.3f} y={:.3f} f(x,y)={:.3f}'.format(x, y, fxy))
                failCount = 0            # 失敗次數歸零
            else:                        # 若沒有更高
                failCount = failCount + 1#   那就又失敗一次
        return (x,y,fxy)                 # 結束傳回 （已經失敗超過一萬次了）

    def f(x, y):
        return -1 * ( x*x -2*x + y*y +2*y - 8 )

    hillClimbing(f, 0, 0)

    ```

  * 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\01-hillclimbing\03-var2> python .\hillClimbing2r.py
    x=0.005 y=-0.008 f(x,y)=8.000
    x=0.000 y=-0.015 f(x,y)=8.027
    x=0.004 y=-0.016 f(x,y)=8.031
    x=0.010 y=-0.020 f(x,y)=8.041
    x=0.008 y=-0.028 f(x,y)=8.059
    .
    .
    .
    x=0.993 y=-1.005 f(x,y)=10.000
    x=1.001 y=-1.000 f(x,y)=10.000
    x=1.000 y=-1.000 f(x,y)=10.000
    x=1.000 y=-1.000 f(x,y)=10.000
    x=1.000 y=-1.000 f(x,y)=10.000
    ```
