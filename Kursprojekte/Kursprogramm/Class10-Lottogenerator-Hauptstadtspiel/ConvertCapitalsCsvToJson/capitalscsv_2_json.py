"""
Capitals file downloaded from:
http://www.downloadexcelfiles.com/wo_en/download-excel-file-list-national-capitals#.WJmxhFUrJaQ
"""

import pandas as pd
# read csv and get important columns
capitals = pd.read_csv('capitals.csv', usecols=['Country', 'Capital City'])
# drop lines with nan entry
capitals.dropna(inplace=True)
# set inedx
capitals.set_index('Country', inplace=True)
# delete additional info in parenthesis after
capitals['Capital City'] = capitals['Capital City'].apply(lambda x: x.split('(')[0].strip())
capDict = capitals.to_dict()['Capital City']
print capDict
# save to json
capitals['Capital City'].to_json('capitals.json')
