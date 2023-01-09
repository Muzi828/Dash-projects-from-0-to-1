import pandas as pd

today = pd.to_datetime('today').strftime('%B %d %Y')


import os
os.chdir(r'D:\Data Science\plotly学习\个人\【10. Covid data visualizing】Dropdown-pie-line-map-indicator-bar\assets')
confirmed = pd.read_csv('data/confirmed.csv')
deaths = pd.read_csv('data/death.csv')
recovered = pd.read_csv('data/recovered.csv')

#数据逆透视：把在标题上的信息转化成为单元格中信息（即行转列）
total_confirmed = pd.melt(confirmed,id_vars=confirmed.columns[:4],value_vars=confirmed.columns[4:],var_name='date',value_name='confirmed')
total_deaths = pd.melt(deaths,id_vars=deaths.columns[:4],value_vars=deaths.columns[4:],var_name='date',value_name='death')
total_recovered = pd.melt(recovered,id_vars=recovered.columns[:4],value_vars=recovered.columns[4:],var_name='date',value_name='recovered')

#数据合并
covid_data = total_confirmed.merge(right = total_deaths, how = 'left', on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])
covid_data = covid_data.merge(right = total_recovered, how = 'left', on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])

#缺失值处理
covid_data['recovered'] = covid_data['recovered'].fillna(0)

#衍生字段创建
covid_data['active'] = covid_data['confirmed'] - covid_data['death'] - covid_data['recovered']

#将日期转化为时间格式（会自动进行解析）
covid_data['date'] = pd.to_datetime(covid_data['date'])

#获取按照日期汇总得到的确诊，死亡和治愈和active的人员
covid_data_1 = covid_data.groupby('date')[['confirmed','death','recovered','active']].sum().reset_index()

#获取最近一天的确诊，死亡和治愈和active的人员值
confirmed_num = covid_data_1['confirmed'].iloc[-1]
rate_confirmed = (confirmed_num - covid_data_1['confirmed'].iloc[-2])

death_num = covid_data_1['death'].iloc[-1]
rate_death = death_num - covid_data_1['death'].iloc[-2]

recovered_num = 'No data available' if covid_data_1['recovered'].iloc[-1] ==0 else covid_data_1['recovered'].iloc[-1]
rate_recovered = 'No data available' if recovered_num == 'No data available' else  recovered_num - covid_data_1['recovered'].iloc[-2]

active_num = covid_data_1['active'].iloc[-1]
rate_active = active_num - covid_data_1['active'].iloc[-2]


#更新header.py中的数据获取时间
updata_time = covid_data_1['date'].iloc[-1].strftime('%B %d %Y')

# 设置Dropdown下拉组件中的标签
country_ls = covid_data['Country/Region'].unique().tolist()


#获取每个国家/地区每天的信息
covid_data_2 = covid_data.groupby(['date', 'Country/Region'])[
            ['confirmed', 'death', 'recovered', 'active']].sum().reset_index()



def get_30_days_data(country):
    covid_data_3 = covid_data_2[covid_data_2['Country/Region'] == country][['date', 'Country/Region', 'confirmed']].reset_index()
    covid_data_3['confirmed new add'] = covid_data_3['confirmed'] -  covid_data_3['confirmed'].shift(1)
    covid_data_3['Rolling Ave.'] = covid_data_3['confirmed new add'].rolling(7).mean()
    return covid_data_3

#获取地理编码信息
iso_code = []
conutry = []
country_chinese = []

with open('data/iso编码.txt','r',encoding='utf-8') as f:
    for i in f.readlines():
        # print(i.split('    '))
        contents = i.split('    ')
        iso_code.append(contents[0])
        conutry.append(contents[-2].replace('&','and').strip()) 
        country_chinese.append(contents[-1].replace('\n',''))


df_iso = pd.DataFrame({'iso':iso_code,
                      'country':conutry,
                      'country_chinese ':country_chinese})

#替换掉疫情数据中的非iso对应的地区信息
replace_dict = {
    'Bahamas':'The Bahamas',
    'Burkina Faso':'Burkina',
    'Burma':'Myanmar (Burma)',
    'Cabo Verde':'Cape Verde',
    'Comoros':'The Comoros',
    'Congo (Brazzaville)':'Republic of the Congo',
    'Congo (Kinshasa)':'Democratic Republic of the Congo',
    "Cote d'Ivoire":"Côte d'Ivoire",
    'Czechia':'Czech Republic',
    'Eswatini':'Swaziland',
    'Holy See':'Vatican City (The Holy See)',
    'Korea, North':'North Korea',
    'Korea, South':'South Korea',
    'Kosovo':'Serbia',
    'Marshall Islands':'Marshall islands',
    'Micronesia':'Federated States of Micronesia',
    'North Macedonia':'Republic of Macedonia (FYROM)',
    'Philippines':'The Philippines',
    'Russia':'Russian Federation',
    'Saint Kitts and Nevis':'St. Kitts and Nevis',
    'Saint Lucia':'St. Lucia',
    'Saint Vincent and the Grenadines':'St. Vincent and the Grenadines',
    'Taiwan*':'Taiwan',
    'Timor-Leste':'Timor-Leste (East Timor)',
    'United Kingdom':'Great Britain (United Kingdom; England)',
    'US':'United States of America (USA)',
    'West Bank and Gaza':'Jordan'  
}

covid_data['Country/Region'] = covid_data['Country/Region'].replace(replace_dict)

#将疫情数据和iso数据信息进行合并
geo_data = pd.merge(covid_data,df_iso,left_on='Country/Region',right_on='country') 

#还需要将时间字段转化为字符串，并提取年月的信息
geo_data['date_str'] = geo_data['date'].astype(str)
geo_data['date_play'] =geo_data['date_str'].str[:7] 

#补充格陵兰岛的数据
date = geo_data['date_str'].unique()
date_play = [i[:7] for i in date]

df_greenland = pd.DataFrame({
    'Country/Region':['Greenland']*len(date),
    'iso':['GRL']*len(date),
    'date':date,
    'date_play':date_play,
    'confirmed':[0]*len(date)
})

#最终的地理数据
geo_data = pd.concat([geo_data,df_greenland])