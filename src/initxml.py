import xml.etree.ElementTree as et
from copy import deepcopy
import re
from prepdata import importExcel, getLength

def getXML(path = 'habides-derogations-instance.xml'):
    return et.parse(path)

def getRootXML(tree):
    return tree.getroot()

def getCopyEntry(root, entry = 'derogation'):
    derogation = root.find(entry)
    return deepcopy(derogation)

def duplicateElement(root, lenDataDerogations, copy):
    i = 1
    while i != lenDataDerogations:
        i += 1
        root.append(copy)
    return root

def toString(tree):
    return et.tostring(tree.getroot(), encoding = 'utf-8')

def writeToXMLFile(tree, filename = 'empty.xml'):
    tree.write(filename, encoding = 'UTF-8', xml_declaration = True) 

def main():
    dataDerogations = importExcel('testfile.xlsx')
    lenDataDerogations = getLength(dataDerogations)
    tree = getXML('habides-derogations-instance.xml')
    root = getRootXML(tree)
    copy = getCopyEntry(root, 'derogation')
    root = duplicateElement(root, lenDataDerogations, copy)

    writeToXMLFile(tree = tree)
    
    
if __name__ == '__main__':
    main()
    