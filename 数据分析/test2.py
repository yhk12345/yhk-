import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

os.chdir(r"E:\数据挖掘\1511R\大数据_1511R（数据挖掘）_02_单元")
infile = "loans.xlsx"
#读取数据
data = pd.read_excel(infile)
print(len(data))
#将列名改为小写形式
data.columns = data.columns.map(str.lower)
#删除每月归还额变量
del data['每月归还额']
#print(data)
#频数统计
#print(data['还款状态'].value_counts())
#分组统计
#print(data.groupby('还款状态').mean())
#贷款金额的均值做分组统计
#print(data.groupby('贷款金额').mean())
#统计贷款金额的均值、标准差、最小值、最大值、中位数
datamean = data['贷款金额'].mean()
#print(datamean)
datamedian = data['贷款金额'].median()
#print(datamedian)
datastd = data['贷款金额'].std()
print(datastd)
datamin = data['贷款金额'].min()
#print(datamin)
datamax = data['贷款金额'].max()
#print(datamax)