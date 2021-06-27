# 第十五周筆記

## Colab

* 可執行文件
  
  * python notebook

  * Linux 虛擬機

### 優缺點

* 優點
  1. 使用雲端空間，不用自己的電腦空間。
  1. 免費用Colab的GPU算力，執行epoch的速度很快。
  1. 可以跳過Mac、Win的各種坑，硬體設定省心。
  1. 手機平板也可以執行，但建議只用來看成果，因為容易斷線。
* 缺點
  1. 課程資料超過20G，超過免費的google雲端硬碟容量，也就是要租空間或有免費的教育方案，有些學校有提供校友免費申請，不妨花時間找找，付費資訊參閱google說明。
  1. Colab設定需要填坑。
  1. 一定要有網路。

## 機器學習

人工智慧的研究歷史有著一條從以「推理」為重點，到以「知識」為重點，再到以「學習」為重點的自然、清晰的脈絡。顯然，機器學習是實現人工智慧的一個途徑，即以機器學習為手段解決人工智慧中的問題。

### [循環神經網路 RNN](./week14.md#循環神經網路-rnn)

![循環神經網路 RNN](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Recurrent_neural_network_unfold.svg/1200px-Recurrent_neural_network_unfold.svg.png)

### [長短期記憶網路 LSTM](./week14.md#長短期記憶網路-lstm)

![長短期記憶網路 LSTM](https://pic2.zhimg.com/80/v2-556c74f0e025a47fea05dc0f76ea775d_1440w.jpg)

### One-hot

One-hot 在數位電路中被用來表示一種特殊的位元組合，該位元組裏，僅容許單一位元爲 1，其他位元都必須爲 0。之所以稱爲 one-hot 就是因爲只能有一個 1。若情況相反，只有一個 0，其餘爲 1，則稱爲 one-cold。

二進制 | 格雷碼 | One-hot
- | - | -
000 | 000 | 00000001
001 | 001 | 00000010
010 | 011 | 00000100
011 | 010 | 00001000
100 | 110 | 00010000
101 | 111 | 00100000
110 | 101 | 01000000
111 | 100 | 10000000

* 與其他編碼的差異

  * 優點

    1. 決定狀態機目前狀態的時間成本低，因爲讀取一個正反器的時間成本固定。
    1. 改變機器的狀態所需時間成本也是固定，因爲每次只需要改變兩個正反器的值。
    1. 設計及設計變更容易。
    1. 容易偵測出非法狀態。
    1. 可以有效率地使用 FPGA 的大量正反器。
    1. 相較於其他編碼，使用 one-hot 來實現狀態機通常可以達到更高的時脈頻率。

  * 缺點
    1. 比起其他編碼，需要更多的正反器，使得其在 PAL 裝置上不切實際。
    1. 會有很多非法狀態存在。這是由於 ![equation](https://latex.codecogs.com/svg.latex?N) 個正反器構成的計數器總共有 ![equation](https://latex.codecogs.com/svg.latex?2^N) 個狀態（每個正反器可以是0或1，所以總共 ![equation](https://latex.codecogs.com/svg.latex?2^N) 種可能狀態），但是合法狀態卻只有 ![equation](https://latex.codecogs.com/svg.latex?N) 個（即同一時間只允許一個正反器是1,其他必須爲0），所以總共會有 ![equation](https://latex.codecogs.com/svg.latex?2^N-N) 個可能的非法狀態。

## 參考資料

* <https://hackmd.io/@wiimax/S1VGctnSS>

* <https://zh.wikipedia.org/wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0>

* <https://zh-yue.m.wikipedia.org/wiki/%E9%81%9E%E8%BF%B4%E7%A5%9E%E7%B6%93%E7%B6%B2%E7%B5%A1>

* <https://zhuanlan.zhihu.com/p/32085405>

* <https://zh.wikipedia.org/wiki/One-hot>
