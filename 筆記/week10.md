# 第十周筆記

## 迪摩根定律

德摩根發現了在命題邏輯中存在著下面這些關係：

* ![equation](https://latex.codecogs.com/svg.latex?(p\land&space;q)\equiv&space;(\neg&space;p)\lor&space;(\neg&space;q))

* ![equation](https://latex.codecogs.com/svg.latex?(p\lor&space;q)\equiv&space;(\neg&space;p)\land&space;(\neg&space;q))

即：

* 非（ ![equation](https://latex.codecogs.com/svg.latex?p) 且 ![equation](https://latex.codecogs.com/svg.latex?q) ）等價於（ 非 ![equation](https://latex.codecogs.com/svg.latex?p) ）或（ 非 ![equation](https://latex.codecogs.com/svg.latex?q) ）

* 非（ ![equation](https://latex.codecogs.com/svg.latex?p) 或 ![equation](https://latex.codecogs.com/svg.latex?q) ）等價於（ 非 ![equation](https://latex.codecogs.com/svg.latex?p) ）且（ 非 ![equation](https://latex.codecogs.com/svg.latex?q) ）

## 謂詞邏輯 (Predicate Logic)

在布林邏輯中，只有用來代表真假值的簡單變數，像是 A, B, C, X, Y, Z .... 等，所以邏輯算式看來通常如下：

* P & (P=>Q) => Q.

* A & B & C => D | E.

* -(A & B) <=> -A | -B.

這種命題邏輯裏沒有函數的概念，只有簡單的命題 (Proposition)，因此才稱為命題邏輯。

而在謂詞邏輯裏，則有「布林函數」的概念，因此其表達能力較強，例如以下是一些謂詞邏輯的範例。

* Parent(x,y) <= Father(x,y). 若 x 是 y 的父親，則 x 是 y 的父母親。

* Parent(John, Johnson).

* Ancestor(x,y) <= Parent(x,y).

* Ancestor(x,y) <= Ancestor(x,z) & Parent(z,y).

可以看到在這種邏輯系統裏，有「布林變數」的概念 (像是 x, y, z 等等)，也有函數的概念，像是 Parent(), Father(), Ancestor() 等等。

## 一階邏輯(First-Order Logic)

在上述這種謂詞邏輯系統中，如果我們加上 ![equation](https://latex.codecogs.com/svg.latex?\forall) (對於所有) 或 ![equation](https://latex.codecogs.com/svg.latex?\exists)  (存在) 這兩個變數限定符號，而其中的謂詞不可以是變項，而必須要是常項，這種邏輯就稱為一階邏輯。

* ![equation](https://latex.codecogs.com/svg.latex?\forall&space;People(x)=%3EMortal(x))；人都是會死的。

* ![equation](https://latex.codecogs.com/svg.latex?People(Socrates))；蘇格拉底是人。

* ![equation](https://latex.codecogs.com/svg.latex?Mortal(Socrates))；蘇格拉底會死。

## 二階邏輯

如果一階邏輯中的謂詞，放寬成可以是變項的話 (這些變項可以加上 ![equation](https://latex.codecogs.com/svg.latex?\\forall) 與 ![equation](https://latex.codecogs.com/svg.latex?\\exists) 等符號的約束)，那就變成了二階邏輯，以下是一些二階邏輯的規則範例。

* ![equation](https://latex.codecogs.com/svg.latex?\\exists&space;P(P(x)\\&P(y)))

* ![equation](https://latex.codecogs.com/svg.latex?\\forall&space;P&space;\\forall(P(x)\\&P(y)))

* ![equation](https://latex.codecogs.com/svg.latex?\\forall&space;P(P(0)\\&&space;\\forall&space;y(P(y)=>P(succ(y)))=>\\forall&space;yP(y))) -> 數學歸納法規則

### 實作

* 執行 `queen.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\04-logic> python .\kbTest.py
    ['A<=B', 'B<=C&D', 'C<=E', 'D<=F', 'E', 'F', 'Z<=C&D&G', '']
    rule:head=A terms=['B']
    rule:head=B terms=['C', 'D']
    rule:head=C terms=['E']
    rule:head=D terms=['F']
    rule:head=E terms=
    rule:head=F terms=
    rule:head=Z terms=['C', 'D', 'G']
    addFact(E)
    addFact(F)
    addFact(C)
    addFact(D)
    addFact(B)
    addFact(A)
    facts= dict_keys(['E', 'F', 'C', 'D', 'B', 'A'])
    ```

* 執行 `kbQuery.py`

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai\04-logic> python .\kbQuery.py animal_ostrich.kb
    ['哺乳類 <= 有毛', '\n哺乳類 <= 泌乳', '\n鳥類   <= 有羽毛', '\n鳥類   <= 會飛 & 生蛋', '\n食肉類 <= 哺乳類 & 吃肉', '\n食肉類 <= 有爪 & 利齒 & 兩眼前視', '\n有
    蹄類 <= 哺乳類 & 有蹄', '\n偶蹄類 <= 哺乳類 & 反芻', '\n獵豹   <= 哺乳類 & 吃肉 & 斑點', '\n老虎   <= 哺乳類 & 吃肉 & 條紋', '\n長頸鹿 <= 有蹄類 & 長腿 & 斑點', '\n斑馬   <= 有蹄類 & 條紋', '\n鴕鳥   <= 鳥類 & 長腿', '\n\n會飛', '\n生蛋', '\n長腿', '']
    rule:head=哺乳類 terms=['有毛']
    rule:head=哺乳類 terms=['泌乳']
    rule:head=鳥類 terms=['有羽毛']
    rule:head=鳥類 terms=['會飛 ', ' 生蛋']
    rule:head=食肉類 terms=['哺乳類 ', ' 吃肉']
    rule:head=食肉類 terms=['有爪 ', ' 利齒 ', ' 兩眼前視']
    rule:head=有蹄類 terms=['哺乳類 ', ' 有蹄']
    rule:head=偶蹄類 terms=['哺乳類 ', ' 反芻']
    rule:head=獵豹 terms=['哺乳類 ', ' 吃肉 ', ' 斑點']
    rule:head=老虎 terms=['哺乳類 ', ' 吃肉 ', ' 條紋']
    rule:head=長頸鹿 terms=['有蹄類 ', ' 長腿 ', ' 斑點']
    rule:head=斑馬 terms=['有蹄類 ', ' 條紋']
    rule:head=鴕鳥 terms=['鳥類 ', ' 長腿']
    rule:head=會飛 terms=
    rule:head=生蛋 terms=
    rule:head=長腿 terms=
    addFact(會飛)
    addFact(生蛋)
    addFact(長腿)
    addFact(鳥類)
    addFact(鴕鳥)
    facts= dict_keys(['會飛', '生蛋', '長腿', '鳥類', '鴕鳥'])
    ```

## 參考資料

* <https://zh.wikipedia.org/wiki/%E5%BE%B7%E6%91%A9%E6%A0%B9%E5%AE%9A%E5%BE%8B>

* <https://programmermedia.org/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/_doc/%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96/A-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96%E7%B0%A1%E4%BB%8B.md>
