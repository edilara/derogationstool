import pandas as pd
import json 

def importExcel(pathdata):
    return pd.read_excel(pathdata, keep_default_na= False)

def replaceTrueFalse(df):
    return df.replace('No', 'false').replace('Yes', 'true')

def addDummyCols(df):
    df['licensed'] = ''
    df['actuallyTaken'] = ''
    return df

def loadTranslations(path = 'translations.json'):
    with open(path, 'r+') as tr:
        transdict= json.loads(tr.read())
    return transdict

def transformCols(df, transdict):
    return df.rename(transdict, axis=1, inplace=True)

def enforceDates(df):
    for col in df:
        if col.dtype == 'datetime64[ns]':
            df[col] = pd.to_datetime(df[col].dt.strftime('%d-%m-%y'))
        else:
            continue
    return df

def dfToDict(df):
    return df.fillna('').to_dict(orient = 'records')

def getTags(root):
    taglist = []
    for d in root.find('derogation'):
        for x in d:
            taglist.append(x.tag)
    return taglist

