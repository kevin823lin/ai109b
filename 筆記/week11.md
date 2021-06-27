# 第十一周筆記

## 傅立葉轉換

傅立葉轉換是一種線性積分轉換，用於信號在時域（或空域）和頻域之間的轉換，在物理學和工程學中有許多應用。傅立葉轉換就像化學分析，確定物質的基本成分；信號來自自然界，也可對其進行分析，確定其基本成分。

## 科學計算常用函式庫

* matplotlib ── 畫圖、視覺化工具

  * subplot(x,y,z) row_x 乘 column_y 張圖中的第 z 張。

* numpy ── 數學矩陣運算

  * import numpy as np

  * np.arange(x,y) 從起始值到上限值。

  * np.add(x,y) 兩矩陣相加。

  * np.shape() 回傳矩陣為幾乘幾陣列，np.shape=(x,y) 重設矩陣維度。

  * np.linspace(x,y,z) 從 x~y 分成 z 個。

  * 可直接使用 a+b、a*b、a>b 等。

  * a[x:y:z] a變數中大於等於x，小於y,一次取z單位。

  * np.linalg.det(x) 求出 x 矩陣之行列式

  * np.random.randint(0,10,6) 0~10 取 6 個。

* scipy ── 擴充numpy

  * from scipy import linalg 計算矩陣特徵向量

  * linalg.solve(A,B) 解出 A,B 矩陣的特徵向量

* sympy ── 符號運算

  * x,y = symbols('x y')：建立變數 x、y。

  * diff(x,y)：對 x 做 y 微分。

  * integrate(x,y,z)：對 x 做積分，範圍是 y~z。

  * factor(x)：將 x 做因數分解。

  * expand(x)：將 x 乘開。

  * simplify(x)：將 x 進行同類項合併。

  * solve(x)：將 x 求解。

  * sqrt(x)：將 x 開根號。

## 參考資料

* <https://zh.wikipedia.org/wiki/%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2>
