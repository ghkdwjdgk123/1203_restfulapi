import pickle

with open('./lr_model.pkl', 'rb') as f:
    lr_reg = pickle.load(f)

import pandas as pd

bike_df = pd.read_csv('./test (1).csv')


bike_df['datetime'] = bike_df.datetime.apply(pd.to_datetime)
# datetime 타입에서 년, 월, 일, 시간 추출
bike_df['year'] = bike_df.datetime.apply(lambda x : x.year)
bike_df['month'] = bike_df.datetime.apply(lambda x : x.month)
bike_df['day'] = bike_df.datetime.apply(lambda x : x.day)
bike_df['hour'] = bike_df.datetime.apply(lambda x: x.hour)

bike_df.drop('datetime', axis = 1,inplace=True)

bike_df = bike_df[['season', 'holiday', 'workingday', 'weather', 'temp', 'atemp',
       'humidity', 'windspeed', 'year', 'month', 'day', 'hour']]

lr_reg.predict(bike_df)

pd.DataFrame(.iloc[:1].values)
