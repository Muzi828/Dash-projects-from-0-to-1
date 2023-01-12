import pandas as pd
import warnings  #由于版本的关系可能出现警告，忽略掉即可
warnings.filterwarnings('ignore')

#读入数据文件
data = pd.read_csv('d:/Data Science/plotly学习/个人/【13. Sale board】Rangeslider-Checklist-Bar-Pie-Scatter-Table/data/train.csv')

def get_year_month_day(df,time_col):
    
    '''Extract the year, month, and day of the time field data'''
    
    df[time_col]  = pd.to_datetime(df[time_col])
    df['year'] = df[time_col].dt.year
    df['month'] = df[time_col].dt.month
    df['day'] = df[time_col].dt.day
    return df

#借助时间解析函数，获取年、月、日信息
data = get_year_month_day(data,'Order Date')

#获取数据的年份唯一值,核实没有缺失值None
year_ls = data['year'].unique()

# 获取类别部门唯一值，核实没有缺失值
segment_ls = data['Segment'].unique()

#封装获取数据的过程，方便回调
def get_data(year,segment):
    return data[(data['year']==year) & (data['Segment']==segment)]

