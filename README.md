# Read Me
放一些自己感兴趣的东西

# tax.py
2019年做过一次税率调整，计算一下自己可以少交多少税（2020年以后换了新的交税算法，但是总额和2019年的一样）

使用方法：python3 tax.py <月工资>

比如：python3 tax.py 10000

# bmr.py
计算自己的基础代谢率

公式只是参考，在基础代谢率上下浮动10-15%都是正常范围，超出这个范围可能就属于病理性原因了。

所以，同样的体重身高年龄性别体脂率，实际基础代谢率依然会有较大差异，最高最低可能会差30%左右。

使用方法：python3 bmr.py <体重/kg> <身高/cm> <年龄/year> <性别/男1女0> <体脂率/比如20.0>

比如：python3 bmr.py 80 178 35 1 20
