import xml.etree.ElementTree as et
from copy import deepcopy
import re
from prepdata import importExcel, getLength
from requests import get 

def getXML(pathxml = 'habides-derogations-instance.xml'):
    return et.parse(pathxml)

def retrieveInstance(urlpath = 'http://dd.eionet.europa.eu/schemas/habides-2.0/habides-derogations-instance.xml'):
    response = get(urlpath)
    return et.fromstring(response.content)

def getRootXML(tree):
    return tree.getroot()

def getCopyEntry(root, entry = 'derogation'):
    derogation = root.find(entry)
    return deepcopy(derogation)

def appendElement(root, lenDataDerogations, copy):
    i = 1
    while i != lenDataDerogations:
        i += 1
        root.append(copy)
    return root


def writeToXMLFile(tree, filename = 'empty.xml'):
    tree.write(filename, encoding = 'UTF-8', xml_declaration = True) 

    