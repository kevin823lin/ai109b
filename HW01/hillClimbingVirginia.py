from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionVirginia import solutionVirginia # 引入平方根解答類別

# 執行爬山演算法 (最多十萬代、失敗一千次就跳出)。
hillClimbing(solutionVirginia([1,1,1]), 100000, 1000)
