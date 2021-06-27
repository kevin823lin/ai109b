# 第十三周筆記

## 反傳遞演算法

反傳遞演是「誤差反傳遞演」的簡稱，是一種與最優化方法（如梯度下降法）結合使用的，用來訓練人工神經網絡的常見方法。該方法對網絡中所有權重計算損失函數的梯度。這個梯度會反饋給最優化方法，用來更新權值以最小化損失函數。

### 反傳遞演算法主要由兩個階段組成：

* 第 1 階段：激勵傳遞

    每次疊代中的傳遞環節包含兩步：

  1. （前向傳遞階段）將訓練輸入送入網絡以獲得激勵響應；

  1. （反向傳遞階段）將激勵響應同訓練輸入對應的目標輸出求差，從而獲得輸出層和隱藏層的響應誤差。

* 第 2 階段：權重更新

    對於每個突觸上的權重，按照以下步驟進行更新：

  1. 將輸入激勵和響應誤差相乘，從而獲得權重的梯度；

  1. 將這個梯度乘上一個比例並取反後加到權重上。

這個比例（百分比）將會影響到訓練過程的速度和效果，因此成為「訓練因子」。梯度的方向指明了誤差擴大的方向，因此在更新權重的時候需要對其取反，從而減小權重引起的誤差。

第 1 和第 2 階段可以反覆循環疊代，直到網絡對輸入的響應達到滿意的預定的目標範圍為止。

### 實作

* 執行 `net1.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\03-net> python .\net1.py
    net.forward()= 10
    net.backwward()
    x= v:1 g:2 y= v:3 g:6 o= v:10 g:1
    gfx = x.g/o.g =  2.0 gfy = y.g/o.g= 6.0
    ```

* 執行 `net2.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\03-net> python .\net2.py
    0  =>  10
    1  =>  9.216
    2  =>  8.4934656
    3  =>  7.827577896960003 
    4  =>  7.213895789838339 
    .
    .
    .
    95  =>  0.004280892060076547
    96  =>  0.003945270122566546
    97  =>  0.003635960944957329
    98  =>  0.003350901606872675
    99  =>  0.003088190920893857
    x= 0.01687031935884968 y= 0.050610958076549
    ```

## Pytorch

PyTorch 是一個開源的 Python 機器學習庫，基於 Torch，底層由 C++ 實現，應用於人工智慧領域，如自然語言處理。

PyTorch主要有兩大特徵：

1. 類似於NumPy的張量計算，可使用GPU加速；
1. 基於帶自動微分系統的深度神經網路。

### 實作

* 執行 `autograd0.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\04-torch> python .\autograd0.py
    tensor(2.)
    tensor(6.)
    10.0
    ```

* 執行 `autograd1.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\04-torch> python .\autograd1.py
    tensor(2.)
    tensor(6.)
    10.0
    ```

* 執行 `autograd2.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\04-torch> python .\autograd2.py
    f= 10.0
    x.grad= tensor([2., 6.])
    ```

* 執行 `torchGd1.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\05-torchGd> python .\torchGd1.py 
    99 x= 1.0026644468307495 loss= 0.994678258895874
    199 x= 1.183614730834961 loss= 0.6664848327636719
    299 x= 1.3317338228225708 loss= 0.4465796947479248
    399 x= 1.4529796838760376 loss= 0.29923129081726074
    499 x= 1.552227258682251 loss= 0.20050048828125
    .
    .
    .
    4599 x= 1.9998756647109985 loss= 0.0
    4699 x= 1.9998995065689087 loss= 0.0
    4799 x= 1.9999170303344727 loss= 0.0
    4899 x= 1.9999289512634277 loss= 0.0
    4999 x= 1.9999408721923828 loss= 0.0
    Result: x = 1.9999409914016724 loss=0.0
    ```

* 執行 `torchGd2.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\05-torchGd> python .\torchGd2.py
    99 parameters= [tensor(0.1073, requires_grad=True)] loss= 3.5821847915649414
    199 parameters= [tensor(0.4507, requires_grad=True)] loss= 2.4002492427825928
    299 parameters= [tensor(0.7318, requires_grad=True)] loss= 1.608290672302246
    399 parameters= [tensor(0.9619, requires_grad=True)] loss= 1.0776381492614746
    499 parameters= [tensor(1.1503, requires_grad=True)] loss= 0.7220726013183594
    .
    .
    .
    4599 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
    4699 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
    4799 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
    4899 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
    4999 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
    Result: parameters = [tensor(1.9999, requires_grad=True)] loss=0.0
    ```

* 執行 `torchGd3.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\07-neural\05-torchGd> python .\torchGd3.py
    x= tensor([-0.0018, -0.0035], requires_grad=True)
    ```

## 參考資料

* <https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95>

* <https://zh.wikipedia.org/wiki/PyTorch>
