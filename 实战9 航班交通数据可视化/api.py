import pandas as pd
import warnings
warnings.filterwarnings('ignore')


data=pd.read_csv('D:/Data Science/plotly学习/个人/【14. Airport traffic data】Dropdown-bar-map/data/2011_february_us_airport_traffic.csv')

#获取州标签的唯一值，并核实无缺失值None
state_ls = data['state'].unique()

#获取州和机场的交通量
state_airport_data = data.groupby(['state','airport','lat','long'])['cnt'].sum().reset_index()

#获取最多的机场所在的州
max_airport= state_airport_data ['state'].value_counts().index[0]