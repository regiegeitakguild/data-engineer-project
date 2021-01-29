'''
Production Company Details:

budget per year
revenue per year
profit per year
releases by genre per year
average popularity of produced movies per year


Movie Genre Details:

most popular genre by year
budget by genre by year
revenue by genre by year
profit by genre by year
'''


#Package Import
import pandas as pd
import ast
import json
import logging

#Load Data
#crdts = pd.read_csv('the-movies-dataset/credits.csv')
#crdts_js = pd.read_csv('the-movies-dataset/credits.csv',converters={'location':json.loads})
#kywrds = pd.read_csv('the-movies-dataset/keywords.csv')
#lnks = pd.read_csv('the-movies-dataset/links.csv')
#lnks_sm = pd.read_csv('the-movies-dataset/links_small.csv')
mv_meta = pd.read_csv('the-movies-dataset/movies_metadata.csv')
logging.info(mv_meta.info)
#rtngs = pd.read_csv('the-movies-dataset/ratings.csv')
#rtngs_sm = pd.read_csv('the-movies-dataset/ratings_small.csv')

#Everything Else?
#print(crdts)
#type(crdts)
#crdts.head()
#crdts.columns()
#print(crdts.cast[0])
#js_test = json.loads(crdts.cast[0])
#print(js_test)
mv_meta_tr = (mv_meta.transpose())


for i in mv_meta.genres:
    #try:
        mv_meta[i] = mv_meta[i].fillna('[]').apply(ast.literal_eval)
    #except:
        #pass
    #print(i)
    #print(mv_meta[i][0])
    #print(type(mv_meta[i][0]))
#mv_meta['production_countries'] = mv_meta['production_countries'].fillna('[]').apply(ast.literal_eval)
#print(type(mv_meta.production_countries[0][0]))

'''
mv_meta['production_countries'] = mv_meta['production_countries'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

s = mv_meta.apply(lambda x: pd.Series(x['production_countries']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'countries'

print(s.head())
'''