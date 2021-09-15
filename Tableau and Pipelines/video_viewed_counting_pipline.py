#!/usr/bin/python 
 
import sys 
import getopt 
from datetime import datetime 
import pandas as pd 
from sqlalchemy import create_engine 
 
if __name__ == "__main__": 
 
    # Input parameters 
    unixOptions = "sdt:edt" 
    gnuOptions = ["start_dt=", "end_dt="] 
     
    fullCmdArguments = sys.argv 
    argumentList = fullCmdArguments[1:] #excluding script name 
     
    try: 
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions) 
    except  
        getopt.error as err: 
        print (str(err)) 
        sys.exit(2) 
     
    start_dt = '' 
    end_dt = '' 
    for currentArgument, currentValue in arguments: 
        if currentArgument in ("-sdt", "--start_dt"): 
            start_dt = currentValue 
        elif currentArgument in ("-edt", "--end_dt"): 
            end_dt = currentValue 
     
    db_config = {'user': 'user',          
                 'pwd': 'password',  
                 'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',        
                 'port': 1234,               
                 'db': 'data-analyst-youtube-data'}              
     
    connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'], 
                                                             db_config['pwd'], 
                                                             db_config['host'], 
                                                             db_config['port'], 
                                                             db_config['db']) 
    engine = create_engine(connection_string) 
     
    # Selecting only vidios that were viewed 
    # between start_dt and end_dt 
    query = ''' SELECT * 
            FROM data_raw 
            WHERE trending_date::TIMESTAMP BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP 
        '''.format(start_dt, end_dt) 
     
    data_raw = pd.io.sql.read_sql(query, con = engine, index_col = 'record_id') 
 
    columns_numeric = ['videos_count'] 
    columns_datetime = ['trending_date'] 
    data_raw['videos_count'] = pd.to_numeric(data_raw['videos_count'], errors='coerce') 
    data_raw['trending_date'] = pd.to_datetime(data_raw['trending_date'])  
     
    videos_count = data_raw.groupby(['region', 'trending_date', 'category_title']).agg({'video_id': 'count'}) 
     
    videos_count = videos_count.rename(columns = {'video_id': 'video_count'}) 
    
    # Deleting older records between start_dt and end_dt 
    query = '''DELETE FROM videos_count  
                   WHERE trending_date BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP 
            '''.format(start_dt, end_dt) 
    engine.execute(query) 
     
    videos_count.to_sql(name = 'videos_count', con = engine, if_exists = 'append', index = False)  