import prepdata as prep
import xml.etree.ElementTree as et
from initxml import getXML, getRootXML


def setDerogations(root, userIdentity = 'TestGovt', country = 'XX'):
    userIdentity = str(input('userIdentity: ') or userIdentity) #none given --> default
    country = str(input('country: ') or country) #none given --> default
    
    root.set('userIdentity', userIdentity)
    root.set('country', country)
    return root

def setDirective(root, directive = 'http://rod.eionet.europa.eu/obligations/268'):
    for entry in root.findall('derogation'):
        entry.set('directive', directive)
    return root 

def setStatus(root, status = 'complete'):
    for entry in root.findall('derogation'):
        entry.set('status', status)
    return root 

def setDirectiveDerogation(derogation, directive = 'http://rod.eionet.europa.eu/obligations/268'):
    return derogation.set('directive', directive)

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

