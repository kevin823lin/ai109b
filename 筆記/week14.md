# 第十四周筆記

## 人工智慧與神經網路

### 人工智慧的方法

人工智慧的方法可以分成5種:

1. 比對法

    記錄問題與答案配對後，直接從表格內查出。

    例如：Alex。

1. 推理法

    撰寫規則後，電腦根據規則推論。

    例如：專家系統。

1. 搜尋法

    對所有可能的結果進行系統式的列舉，然後看看有沒有答案。

    例如：深度優先、廣度優先、電腦下棋。

1. 統計法

    找出機率最大的解答。

    例如：利用電腦亂數驗證中央極限定理。

1. 優化法

    對每個可能的解答，都給一個分數及權重，找出總分最好的解答。

    例如：爬山演算法、遺傳演算法。

### 神經網路

* 模仿人腦神經網路結構，但簡化了很多，只留下點+線+閘

    ![神經元示意圖](../img/神經元示意圖.png)

* 每個神經元都會用開關函數控制

    ![開關函數](../img/開關函數.png)

## 深度學習

* 深度學習是機器學習的分支，是一種以人工神經網路為架構，對資料進行表徵學習的演算法。 深度學習是機器學習中一種基於對資料進行表徵學習的演算法。

* 深度學習的神經網路除了多層感知器之外，還加入了：
  * 卷積神經網路 CNN
  * 循環神經網路 RNN, LSTM
  * 生成對抗網路 GAN
  * 強化學習機制 Reinforcement Learning

### 卷積神經網路 CNN

* 通常被用來《辨認影像》

### 循環神經網路 RNN

* 最常被用來處理語言，像是機器翻譯系統
* 簡單的 RNN 不穩定，只能記住短期的事情

### 長短期記憶網路 LSTM

* 用來解決 RNN 的問題

### 生成對抗網路 GAN

* 採用《偽造者與鑑賞家》對抗的方式， 讓雙方能夠在對抗過程中能力愈來愈強！
* GAN 擅長《模仿他人的風格》 或者將《素描》轉換成《擬真照片》

### 強化學習機制

* 常常透過《探索或自我對打》，找到好的 策略來進行決策！

* AlphaGo 圍棋程式就是《機率模型 + 強化學習 + 神經網路》結合得到的結果！

### 實作

* 執行 `alexnet.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\08-deep\02-pretrained\01-torchvision\01-classify> python .\alexnet.py
    img_t.shape= torch.Size([3, 224, 224])
    batch_t.shape= torch.Size([1, 3, 224, 224])
    C:\Users\kevin\AppData\Roaming\Python\Python38\site-packages\torch\nn\functional.py:718: UserWarning: Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important until they are released as stable. (Triggered internally at  ..\c10/core/TensorImpl.h:1156.)
    return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
    preds.shape= torch.Size([1, 1000])
    208 Labrador retriever
    ```

* 執行 `predict.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\08-deep\02-pretrained\01-torchvision\01-classify> python .\predict.py alexnet .\img\dog.jpg
    model= alexnet imgFile= .\img\dog.jpg
    img_t.shape= torch.Size([3, 224, 224])
    batch_t.shape= torch.Size([1, 3, 224, 224])
    C:\Users\kevin\AppData\Roaming\Python\Python38\site-packages\torch\nn\functional.py:718: UserWarning: Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important until they are released as stable. (Triggered internally at  ..\c10/core/TensorImpl.h:1156.)
    return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
    preds.shape= torch.Size([1, 1000])      
    class_idx= 208 label= Labrador retriever
    PS D:\檔案\課程\1092\人工智慧\ai\08-deep\02-pretrained\01-torchvision\01-classify> python .\predict.py alexnet .\img\cat.jpg
    model= alexnet imgFile= .\img\cat.jpg
    img_t.shape= torch.Size([3, 224, 224])
    batch_t.shape= torch.Size([1, 3, 224, 224])
    C:\Users\kevin\AppData\Roaming\Python\Python38\site-packages\torch\nn\functional.py:718: UserWarning: Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important until they are released as stable. (Triggered internally at  ..\c10/core/TensorImpl.h:1156.)
    return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
    preds.shape= torch.Size([1, 1000])
    class_idx= 285 label= Egyptian cat
    ```

## 參考資料

* <https://www.slideshare.net/ccckmit/ss-95049781>

* <https://medium.com/n%C3%BAcleoml/why-sigmoid-ee95299e11fd>

* <https://zh.wikipedia.org/zh-tw/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0>

* <https://pixabay.com/users/arpitade3-9047214/>
