import pandas as pd
import json 

def importExcel(path):
    return pd.read_excel(path, keep_default_na= False)

def getLength(dataDerogations):
    return len(dataDerogations)

def loadTranslations(path = 'translations.json'):
    with open('translations.json', 'r+') as tr:
        transdict= json.loads(tr.read())
    return transdict

def transformCols(df, transdict):
    return df.rename(transdict, axis=1, inplace=True)

def getTags(root):
    taglist = []
    for d in root.find('derogation'):
        for x in d:
            taglist.append(x.tag)
    return taglist