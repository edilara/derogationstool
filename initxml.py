import pandas as pd
import xml.etree.ElementTree as et
from copy import deepcopy
import re

def getXML(path = 'habides-derogations-instance.xml'):
    return et.parse(path)

def getRootXML(tree):
    return tree.getroot()

def getCopyEntry(root, entry = 'derogation'):
    derogation = root.find(entry)
    return deepcopy(derogation)


