#!/usr/bin/python

import pandas as pd
from sqlalchemy import create_engine

pip install psycopg2

db_config = {'user': 'user', 
             'pwd': 'password',
             'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
             'port': 1234,
             'db': 'data-analyst-youtube-data'} 

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'], db_config['pwd'], db_config['host'], db_config['port'], db_config['db'])


# connecting to the database
engine = create_engine(connection_string)

# create an sql query
query = ''' SELECT * FROM video_count'''

# run query and store results in dataframe
trending_by_time = pd.io.sql.read_sql(query, con=engine, index_col = 'record_id')

trending_by_time.to_csv('trending_by_time.csv', index = False)