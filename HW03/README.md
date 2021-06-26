# 習題 2 : 請用搜尋法（深度優先）求解八個皇后問題

> 看懂老師給的解答後，自己重寫一遍，並加入註解

* [程式碼](./truthtable.py)

    ```python
    def truthTable(n): # 列出 n 個變數的真值表
        p = [] # 存放填入的 0 || 1
        return tableNext(n, p) # 呼叫填表函數

    def tableNext(n, p): # 填表函數
        i = len(p) # 已填入的長度
        if i == n: # 填完就印出並離開
            print(p)
            return
        for x in [0, 1]: # 依序選擇 0, 1
            p.append(x) # 將 x 填入 p
            tableNext(n, p) # 遞迴執行 tableNext，p 依序為 [0, ..., 0, 0]、[0, ..., 0, 1]、[0, ..., 1, 0] ...
            p.pop() # 將 p 最後一項丟掉

    truthTable(2) # 印出 2 個變數的真值表
    truthTable(3) # 印出 3 個變數的真值表
    ```

* 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai109b\HW03> python .\truthtable.py
    [0, 0]
    [0, 1]
    [1, 0]
    [1, 1]
    [0, 0, 0]
    [0, 0, 1]
    [0, 1, 0]
    [0, 1, 1]
    [1, 0, 0]
    [1, 0, 1]
    [1, 1, 0]
    [1, 1, 1]
    ```

## 參考資料

* [老師的程式](https://gitlab.com/ccc109/ai/-/blob/master/03-search/Q3-queen/truthtable.py)
