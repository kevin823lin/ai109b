# 第四周筆記

## 線性規劃

在數學中，線性規劃（Linear Programming，簡稱LP）特指目標函數和約束條件皆為線性的最佳化問題。

### 什麼是線性

> 如果稱一個數學函數 ![equation](https://latex.codecogs.com/svg.image?L(x)) 為線性的，可以是指：
>
> 1. ![equation](https://latex.codecogs.com/svg.image?L(x)=L(x)) 是個只擁有一個變數的一階多項式函數，即是可以表示為 ![equation](https://latex.codecogs.com/svg.image?L(x)=kx+b) 的形式（其中 ![equation](https://latex.codecogs.com/svg.image?k,b) 為常數）。
>
> 2. ![equation](https://latex.codecogs.com/svg.image?L(x)=L(x)) 具有以下兩個性質：
>
>    * 可加性：![equation](https://latex.codecogs.com/svg.image?L(x+t)=L(x)+L(t))
>
>    * 一次齊次性：![equation](https://latex.codecogs.com/svg.image?L(mx)=mL(x))

### 實作

* 執行 `linearProgramming1.py`

    > 當 ![equation](https://latex.codecogs.com/svg.latex?\\begin{pmatrix}&space;x=4\\\\&space;y=-1\\\\&space;z=6&space;\\end{pmatrix}) 時，![equation](https://latex.codecogs.com/svg.image?\\left\\{\\begin{matrix}&space;min(x&plus;4y&plus;9z)\\\\0\\leq&space;x\\leq&space;4&space;\\\\&space;-1\\leq&space;y\\leq&space;1&space;&space;\\\\0\\leq&space;y&space;&space;\\\\x&plus;y\\leq5\\\\x&plus;z\\geq10&space;\\\\-y&plus;z=7&space;\\\\\\end{matrix}\\right.) 有最佳解為 54

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\04-linearProgramming> python .\linearProgramming1.py
    Welcome to the CBC MILP Solver 
    Version: 2.9.0
    Build Date: Feb 12 2015

    command line - C:\Users\kevin\AppData\Roaming\Python\Python38\site-packages\pulp\apis\..\solverdir\cbc\win\64\cbc.exe C:\Users\kevin\AppData\Local\Temp\355b6265bc734b9c941cf30a2d8d0fe6-pulp.mps branch printingOptions all solution C:\Users\kevin\AppData\Local\Temp\355b6265bc734b9c941cf30a2d8d0fe6-pulp.sol (default strategy 1)
    At line 2 NAME          MODEL
    At line 3 ROWS
    At line 8 COLUMNS
    At line 18 RHS
    At line 22 BOUNDS
    At line 26 ENDATA
    Problem MODEL has 3 rows, 3 columns and 6 elements
    Coin0008I MODEL read with 0 errors
    Presolve 1 (-2) rows, 2 (-1) columns and 2 (-4) elements
    0  Obj 51.9 Primal inf 2.099999 (1)
    1  Obj 54
    Optimal - objective value 54
    After Postsolve, objective 54, infeasibilities - dual 0 (0), primal 0 (0)
    Optimal objective 54 - 1 iterations time 0.002, Presolve 0.00
    Option for printingOptions changed from normal to all
    Total time (CPU seconds):       0.01   (Wallclock seconds):       0.01

    Status: Optimal
    x = 4.0
    y = -1.0
    z = 6.0
    objective= 54.0
    ```

## 整數規劃

> 要求為整數解的線性規劃，目前無快速算法

要求所有的未知量都為整數的線性規劃問題叫做整數規劃（integer programming, IP）或整數線性規劃（integer linear programming, ILP）問題。相對於即使在最壞情況下也能有效率地解出的線性規劃問題，整數規劃問題的最壞情況是不確定的，在某些實際情況中（有約束變量的那些）為NP困難問題。

0-1整數規劃是整數規劃的特殊情況，所有的變量都要是0或1（而非任意整數）。這類問題亦被分類為NP困難問題。

只要求當中某幾個未知數為整數的線性規劃問題叫做混合整數規劃（mixed integer programming, MIP）問題。這類問題通常亦被分類為NP困難問題。

### 實作

* 執行 `integerProgramming1.py`

    > 當 ![equation](https://latex.codecogs.com/svg.latex?\\begin{pmatrix}&space;x=1\\\\&space;y=2&space;\\end{pmatrix}) 時，![equation](https://latex.codecogs.com/svg.image?\\left\\{\\begin{matrix}&space;max(y)\\\\-x+y\\leq1&space;\\\\&space;3x+2y\\leq12&space;&space;\\\\2x+3y\\leq12&space;&space;\\\\x,y\\geq0\\\\x,y\in\mathbb{Z}\\end{matrix}\\right.) 有最佳解 ![equation](https://latex.codecogs.com/svg.latex?y=2)

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\02-optimize\05-integerProgramming> python .\integerProgramming1.py
    Welcome to the CBC MILP Solver 
    Version: devel
    Build Date: Nov 15 2020

    Starting solution of the Linear programming relaxation problem using Primal Simplex

    Coin0506I Presolve 3 (0) rows, 2 (0) columns and 6 (0) elements
    Clp1000I sum of infeasibilities 6.95088e-12 - average 2.31696e-12, 0 fixed columns
    Coin0506I Presolve 3 (0) rows, 2 (0) columns and 6 (0) elements
    Clp0029I End of values pass after 2 iterations
    Clp0000I Optimal - objective value 2.8
    Clp0000I Optimal - objective value 2.8
    Coin0511I After Postsolve, objective 2.8, infeasibilities - dual 0 (0), primal 0 (0)
    Clp0000I Optimal - objective value 2.8
    Clp0000I Optimal - objective value 2.8
    Clp0000I Optimal - objective value 2.8
    Clp0032I Optimal objective 2.8 - 0 iterations time 0.022, Idiot 0.02

    Starting MIP optimization
    Cgl0004I processed model has 3 rows, 2 columns (2 integer (0 of which binary)) and 6 elements
    Coin3009W Conflict graph built in 0.000 seconds, density: 0.000%
    Cgl0015I Clique Strengthening extended 0 cliques, 0 were dominated
    Cbc0012I Integer solution of -2 found by DiveCoefficient after 0 iterations and 0 nodes (0.01 seconds)
    Cbc0001I Search completed - best objective -2, took 0 iterations and 0 nodes (0.01 seconds)
    Cbc0035I Maximum depth 0, 0 variables fixed on reduced cost
    Total time (CPU seconds):       0.02   (Wallclock seconds):       0.02

    optimal solution cost 2.0 found
    solution:
    x : 1.0
    y : 2.0
    ```

## 圖形搜尋

圖形搜尋的方法大致可以分為「深度優先搜尋 (Depth-First Search, DFS)、廣度優先搜尋 (Breath-First Search, BFS)、最佳優先搜尋 (Best-First Search, BestFS) 等三類。

![圖、圖形 Graph 的範例](..\img\graphSearch.jpg)

### 深度優先搜尋

這個演算法會儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。

![圖、圖形 Graph 的範例](..\img\dfs.jpg)

### 廣度優先搜尋

BFS是從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。廣度優先搜尋的實現一般採用open-closed表。

![圖、圖形 Graph 的範例](..\img\bfs.jpg)

### 實作

* 執行 graph_search.py

    ```text
    結果:
    dfs:1 => 2 => 3 => 4 => 5 => 6 =>
    bfs:1 => 2 => 5 => 3 => 4 => 6 =>
    ```
