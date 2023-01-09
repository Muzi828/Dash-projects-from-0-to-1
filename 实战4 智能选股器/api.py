import tushare as ts


TOKEN = 'xxx'

pro = ts.pro_api(token=TOKEN)

result = pro.stock_basic()
industry_list = list(set(result['industry'].tolist()))
industry_list.remove(None)


import random
import warnings
warnings.filterwarnings('ignore')


def add_fields(industry):
    df = result[result['industry']==industry]
    df['量比'] = [random.choice(range(0,10)) for i in range(len(df))]
    df['换手率'] = [random.choice(range(-10,10)) for i in range(len(df))]
    return df


import pandas as pd
from datetime import timedelta
end_date = pd.to_datetime('today').strftime('%Y%m%d')
start_date = (pd.to_datetime('today') - timedelta(60)).strftime('%Y%m%d')
trade_days = pro.query('trade_cal', start_date=start_date, end_date=end_date)
start_date = trade_days[trade_days['is_open']==1]['cal_date'].iloc[0]
end_date = trade_days[trade_days['is_open']==1]['cal_date'].iloc[-1]