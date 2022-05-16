import pandas as pd
import nunpy as np
import time
import pickle
import pandas as pd
import numpy as np
import time
import pickle
path1="/content/drive/MyDrive/energy_consump_preprocessed.csv"
model_path="/content/drive/MyDrive/kaggle/model_final.pkl"
meta_data=pd.read_csv(path1)
def test_convertor(meta_data):
    meta_data=meta_data[["date","active_energy"]]
    meta_data=meta_data.set_index(["date"])
    tester=meta_data[-2880:]
    meta_train=[]
    meta_target=[]
    for i in range(120,meta_data.shape[0]):
        meta_train.append(meta_data.values[i-120:i])
        meta_target.append(meta_data.values[i])
    return meta_train,meta_target
def load_the_model(model_path):
    loaded_model= pickle.load(open(model_path, 'rb'))
    return loaded_model
def looper(current_data,model):
    #model1=load_the_model(model_path)
    test,target =test_convertor(meta_data)
    l1=[]
    l1.append(model.predict(test[0])[-1])
    #print(model.predict(test[0])[-1],"---",target[0])
    l1.append(model.predict(test[1])[-1])
    #print(model.predict(test[1])[-1],"----",target[1])
    df1=pd.DataFrame({"main":l1})
    print(df1)
    for i in range(2,len(test)):
        pred=[model.predict(test[i])[-1]]
        #print(pred[-1],"---",target[i])
        df2=pd.DataFrame({"main":pred})
        df1=pd.concat([df1,df2],ignore_index=True,axis=0)
        print(df1)
        #IngesttoRedshift(df1,"table_name")
        time.sleep(59)
model=load_the_model(model_path)
looper(meta_data,model)
def IngesttoRedshift(pandas_df, table_name):
    try:
        # build the sqlalchemy URL
        url = sa_url.URL(
        drivername='postgresql+psycopg2', # indicate redshift_connector driver and dialect will be used
        host='dev-datarangers-final.cwmgpuwjy8xr.us-east-1.redshift.amazonaws.com', # Amazon Redshift host
        port='5439', # Amazon Redshift port
        database='dev', # Amazon Redshift database
        username='root', # Amazon Redshift username
        password='D' # Amazon Redshift password
        )
        conn = create_engine(url)
        pandas_df.to_sql(table_name, conn, index=False, if_exists='replace')
    except Exception as e:
        print("Error occured in IngesttoRedshift() with Exception as ",e)
