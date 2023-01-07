


import os
import pandas as pd

year_ls = []
for i in os.listdir('实战3 个人理财看板/data'):
    df = pd.read_excel(f'实战3 个人理财看板/data/{i}')
    month_total = sum(df.sum().to_list())
    year_ls.append(month_total)
year_total = sum(year_ls)

seadon_dict = {
    '第一季度':[1,2,3],
    '第二季度':[4,5,6],
    '第三季度':[7,8,9],
    '第四季度':[10,11,12],
}
