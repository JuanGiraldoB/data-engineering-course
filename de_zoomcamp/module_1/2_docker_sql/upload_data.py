import pandas as pd
from sqlalchemy import create_engine
from time import time

df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

df_iter = pd.read_csv('yellow_tripdata_2021-01.csv',
                      iterator=True, chunksize=100_000)

df = next(df_iter)

len(df)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.head(n=0).to_sql(con=engine, name='yellow_taxi_data', if_exists='replace')
df.to_sql(con=engine, name='yellow_taxi_data', if_exists='append')

while True:
    t_start = time()

    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(con=engine, name='yellow_taxi_data', if_exists='append')

    t_end = time()

    print('inserted another chunk..., took %.3f seconds' % (t_end - t_start))
