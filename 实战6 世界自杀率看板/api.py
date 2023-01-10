#切换程序的执行路径
import os
os.chdir('d:/Data Science/plotly学习/个人/【11. World suicide rate】Dropdown-Rangedlider-checklist-scatter')

#将文件数据读入到python中
import pandas as pd
df = pd.read_csv('data/suicide rates.csv')


#获取国家信息的唯一值，需要核实是否存在缺失值None
country_ls = df['country'].unique().tolist()

#获取数据的时间跨度
year_min,year_max = df['year'].min(),df['year'].max()

#获取年龄分组情况
age = df['age'].unique().tolist()

#借助sorted()函数进行自定义排序规则设置
age_ordered = sorted(age,key=lambda x: int(x.split('-')[0]) if '-' in x else int(x[:2]))

#汇总后的数据
suicide_df = df.groupby(['age', 'country', 'sex', 'year', 'population', 'suicides/100k pop'])['suicides_no'].sum().reset_index()