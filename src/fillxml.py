import prepdata as prep
import xml.etree.ElementTree as et
from initxml import getXML, getRootXML, getCopyEntry


def setDerogations(root, userIdentity = 'TestGovt', country = 'XX'):
    userIdentity = str(input('userIdentity: ') or userIdentity) #none given --> default
    country = str(input('country: ') or country) #none given --> default
    
    root.set('userIdentity', userIdentity)
    root.set('country', country)
    return root

def getDirective(datapoint):
    return datapoint['directive']
   
def setStatus(root, status = 'complete'):
    for entry in root.findall('derogation'):
        entry.set('status', status)
    return root 

def setDirectiveDerogation(derogation, directive, urls = ['http://rod.eionet.europa.eu/obligations/276', 'http://rod.eionet.europa.eu/obligations/268']):
    if directive == 'Birds':
        derogation.set('directive', urls[0])
    else:
        derogation.set('directive', urls[1])
    return derogation

def setStatusDerogation(derogation, status = 'complete'):
    return derogation.set('status', status)

def fillAttribKeys(dictkey, dict, element):
    return element.set(dictkey, str(dict[dictkey]))

def fillFirstLevel(dictkey, dict, element):
    for elem in element.findall(dictkey):
        elem.text = str(dict[dictkey])
        return element 

def fillSecondlevelPrefix(prefixlist, dictkey, dict, element):
    for n in prefixlist:
        if dictkey == n:
            for elem in element.findall(n.split('_')[0]):
                for nelem in elem.findall(n.split('_')[1]):
                    nelem.text = str(dict[n])
        else:
            continue
    
    return element

def fillSecondLevelCodes(codesdict, dictkey, dict, element):
    for elem in element.findall(dictkey):
        nestedcopy = getCopyEntry(elem, codesdict[dictkey])

        if ',' in str(dict[dictkey]):
            codes = str(dict[dictkey]).split(',')
        else:
            codes = str(dict[dictkey])
        
        if type(codes) is list:
            elem.clear()
            for c in codes:
                nest = et.SubElement(elem, nestedcopy.tag)
                nest.text = str(c)
        else:
            for nelem in elem:
                nelem.text = str(codes)
    
    return element

