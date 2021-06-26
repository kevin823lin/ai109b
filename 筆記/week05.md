# 第五周筆記

## 八皇后問題

> 八皇后問題是一個以西洋棋為背景的問題：如何能夠在 8×8 的西洋棋棋盤上放置八個皇后，使得任何一個皇后都無法直接吃掉其他的皇后？為了達到此目的，任兩個皇后都不能處於同一條橫行、縱行或斜線上。八皇后問題可以推廣為更一般的 n 皇后擺放問題：這時棋盤的大小變為 n×n，而皇后個數也變成 n。若且唯若 n = 1 或 n ≥ 4 時問題有解。

### 實作

* 執行 `queen.py`

    ```python
    # 資料結構       
    #   四皇后解答 q=[1,3,0,2] 代表
    #   x=[1,3,0,2]
    #   y=[0,1,2,3]
    #   圖形如下
    #   [[0,1,0,0],
    #    [0,0,0,1],
    #    [1,0,0,0],
    #    [0,0,1,0]]
    def queen(n): # n 皇后主函數
        q = [] # q 代表已經排下去的皇后，一開始還沒排，所以是空的
        return queenNext(n, q) # 呼叫 queenNext 遞迴下去排出所有可能

    # 思考：排到一半 q=[1,3] 繼續排下去
    #      對 [1,3,0..], [1,3,1..], [1,3,2..], [1,3,3..] 全部試一遍
    def queenNext(n, q): # 已經排好 q[0..y2-1], 繼續排下去 [y2...n-1]
        y2 = qlen = len(q)
        if qlen == n: # 全部排好了
            print(q)  # 印出盤面
            return
        # 還沒排滿，繼續排下去
        for x2 in range(n): # 對本列的每一個 x2 去嘗試
            isConflict = False
            for y in range(qlen): # 前面已經排下去的舊皇后，座標為 (x,y)
                x = q[y]
                if conflict(x,y,x2,y2): # 檢查新排的皇后(x2,y2)，和前面的有沒有衝突
                    isConflict = True
            if not isConflict:  # 如果沒有衝突，就繼續排下去
                q.append(x2)    # 把 (x2,y2) 放進盤面
                queenNext(n, q) # 繼續遞迴尋找下一個皇后位置
                q.pop()         # 把 (x2,y2) 移出盤面
            
    def conflict(x1,y1,x2,y2): # 判斷 (x1,y1), (x2,y2) 兩個位置有沒有衝突
        if x1==x2: return True
        if y1==y2: return True
        if x1+y1==x2+y2: return True
        if x1-y1==x2-y2: return True
        return False

    queen(4) # 列出四皇后的解答
    queen(8) # 列出八皇后的解答
    ```

* 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai109b\HW02> python .\queen.py
    [1, 3, 0, 2]
    [2, 0, 3, 1]
    [0, 4, 7, 5, 2, 6, 1, 3]
    [0, 5, 7, 2, 6, 3, 1, 4]
    .
    .
    .
    [7, 2, 0, 5, 1, 4, 6, 3]
    [7, 3, 0, 2, 5, 1, 6, 4]
    ```

## 列出所有排列

### 實作

* 執行 `permutation.py`

    ```python
    def perm(n): # 主函數
        p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
        return permNext(n, p) # 呼叫 permNext 遞迴下去排出所有可能

    # 思考：排到一半 p=[1,3] 繼續排下去
    #      對 [1,3,0..], [1,3,1..], [1,3,2..], [1,3,3..] 全部試一遍
    def permNext(n, p): # 已經排好 p[0..i-1], 繼續排下去 [i...n-1]
        i = len(p)
        if i == n:  # 全部排好了
            print(p)  # 印出排列
            return
        # 還沒排滿，繼續排下去
        for x in range(n): # 對本列的每一個 x 去嘗試
            p.append(x)    # 把 x 放進盤面
            permNext(n, p) # 繼續遞迴尋找下一個排列
            p.pop()        # 把 x 移出盤面
            
    perm(2) # 列出 2 個的排列
    perm(3) # 列出 3 個的排列
    ```

* 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\03-search\Q3-queen> python .\permutation.py
    [0, 0]
    [0, 1]
    [1, 0]
    [1, 1]
    [0, 0, 0]
    [0, 0, 1]
    [0, 0, 2]
    [0, 1, 0]
    [0, 1, 1]
    [0, 1, 2]
    [0, 2, 0]
    [0, 2, 1]
    [0, 2, 2]
    [1, 0, 0]
    [1, 0, 1]
    [1, 0, 2]
    [1, 1, 0]
    [1, 1, 1]
    [1, 1, 2]
    [1, 2, 0]
    [1, 2, 1]
    [1, 2, 2]
    [2, 0, 0]
    [2, 0, 1]
    [2, 0, 2]
    [2, 1, 0]
    [2, 1, 1]
    [2, 1, 2]
    [2, 2, 0]
    [2, 2, 1]
    [2, 2, 2]
    ```

## 真值表

真值表是使用於邏輯中（特別是在連結邏輯代數、布林函數和命題邏輯上）的一類數學用表，用來計算邏輯表示式在每種論證（即每種邏輯變數取值的組合）上的值。尤其是，真值表可以用來判斷一個命題表示式是否對所有允許的輸入值皆為真，亦即是否為邏輯有效的。

A | B
- | -
0 | 0
0 | 1
1 | 0
1 | 1

A | B | C
- | - | -
0 | 0 | 0
0 | 0 | 1
0 | 1 | 0
0 | 1 | 1
1 | 0 | 0
1 | 0 | 1
1 | 1 | 0
1 | 1 | 1

### 實作

* 執行 `truthtable.py`

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

* 執行 `truthtable2.py`

    ```python
    def truthTable(n, f): # 列出 n 變數的所有可能 0,1 排列
        p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
        return tableNext(n, p, f) # 呼叫 tableNext 遞迴下去排出所有可能

    def tableNext(n, p, f):
        i = len(p) # i 是下一個排列的位置
        if i == n: # 全部排好了
            print(p, f(p)) # 印出排列
            return # 返回上層
        for x in [0,1]: # x 是 0 或 1
            p.append(x) # 把 x 放進表
            tableNext(n, p, f) # 繼續遞迴尋找下一個排列
            p.pop() # 把 x 移出表

    def f(p):
        x,y,z = p
        return x or (y and z)

    # truthTable(2, f) # 印出 2 變數的真值表
    print('[x, y, z] f')
    truthTable(3, f) # 印出 3 變數的真值表

    ```

* 結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\03-search\Q3-queen> python .\truthtable2.py
    [x, y, z] f
    [0, 0, 0] 0
    [0, 0, 1] 0
    [0, 1, 0] 0
    [0, 1, 1] 1
    [1, 0, 0] 1
    [1, 0, 1] 1
    [1, 1, 0] 1
    [1, 1, 1] 1
    ```

## 參考資料

* <https://zh.wikipedia.org/wiki/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98>

* <https://zh.wikipedia.org/zh-tw/%E7%9C%9F%E5%80%BC%E8%A1%A8>
