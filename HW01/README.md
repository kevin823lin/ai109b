# 習題 1 : 請用爬山演算法或遺傳演算法破解維吉尼雅密碼

## 執行結果

:x: 第一次算出 key = [4, 2, -3]

```text
PS D:\檔案\課程\1092\人工智慧\ai109b\HW01> python .\hillClimbingVirginia.py
start:  energy([1, 1, 1])=2.350000
0 : energy([1, 2, 1])=2.350000
2 : energy([1, 2, 2])=2.350000
.
.
.
52 : energy([4, 2, -2])=3.300000
56 : energy([4, 2, -3])=4.300000
solution:  energy([4, 2, -3])=4.300000
```

:heavy_check_mark: 第二次算出 key = [0, 2, 4]

```text
PS D:\檔案\課程\1092\人工智慧\ai109b\HW01> python .\hillClimbingVirginia.py
start:  energy([1, 1, 1])=2.350000
0 : energy([0, 1, 1])=4.600000
2 : energy([0, 1, 2])=4.600000
.
.
.
63 : energy([0, 2, 3])=8.650000
66 : energy([0, 2, 4])=11.650000
solution:  energy([0, 2, 4])=11.650000
```

:heavy_check_mark: 第三次算出 key = [0, 2, 4]

```text
PS D:\檔案\課程\1092\人工智慧\ai109b\HW01> python .\hillClimbingVirginia.py
start:  energy([1, 1, 1])=2.350000
1 : energy([1, 2, 1])=2.350000
2 : energy([1, 1, 1])=2.350000
.
.
.
55 : energy([0, 2, 3])=8.650000
69 : energy([0, 2, 4])=11.650000
solution:  energy([0, 2, 4])=11.650000
```

## 參考資料

程式修改自 <https://gitlab.com/ccc109/ai/-/tree/master/02-optimize/01-hillclimbing/04-framework>
