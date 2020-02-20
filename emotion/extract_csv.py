import pandas as pd
import json
from constant import Constant
from common_utility import Commonutility


filename = 'jsons/20200214_2_213005.307_220002.307.json'
with open(filename,'r') as f:
    data = json.load(f)

# print(data)
cmt = Commonutility()
df =  cmt.prepare_metadata(data,'roi',0.0)

df.to_csv('csvs/20200214_2_213005.307_220002.307.csv',index=None)