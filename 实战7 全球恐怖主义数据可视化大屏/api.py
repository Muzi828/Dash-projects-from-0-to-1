import os
os.chdir(r'd:/Data Science/plotly学习/个人/【12. Global terrorism】 Dropdown-Rangeslider-stackbarline-pie-map/')

import pandas as pd
data = pd.read_csv('data/modified_globalterrorismdb_0718dist.csv')


#首先对需要统计的字段进行缺失值填充，然后按照国家、地区、年份对死亡、受伤和攻击类型进行统计
data[['nkill','nwound','attacktype1']] = data[['nkill','nwound','attacktype1']].fillna(0)
df= data.groupby(['region_txt','country_txt','iyear'])[['nkill','nwound','attacktype1']].sum().reset_index()

#获取数据的时间跨度
year_min,year_max = df['iyear'].min(),df['iyear'].max()

#获取Dropdown组件中的标签信息，第一个是区域标签,核实没有缺失值None
region_ls = df['region_txt'].unique().tolist()

#获取Dropdown组件中的标签信息，第二个是国家标签,核实也没有缺失值None
country_ls = df['country_txt'].unique().tolist()


#根据筛选条件获取绘制图形的数据
def get_data(region,country,span_year):

    '''返回的是一个包含死亡、受伤和攻击类型的列表'''
    df_filter = df[
        (df['region_txt']==region) & (df['country_txt']==country) & (df['iyear']>=span_year[0]) & (df['iyear']<=span_year[1])
    ]
    filter_data_ls = df_filter[df_filter.columns[-3:]].values.T.tolist()
    return filter_data_ls

#获取带有经纬度信息的df
geo_df = data.groupby(['region_txt','country_txt','iyear','latitude','longitude'])[['nkill','nwound','attacktype1']].sum().reset_index()


#筛选组件中的便签选择优化,需要形成一个region作为键，country作为值的字典
option_df = data[['region_txt','country_txt']].groupby('region_txt').agg({'country_txt':lambda x:list(set(x))}).reset_index()

#以第一列为键，第二列为值构建字典变量
options_series = option_df.apply(lambda x: {x['region_txt']:x['country_txt']},axis=1)

#成功构建目标字典
all_options = {}
for i in options_series.values:
    all_options.update(i)