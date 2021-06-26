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