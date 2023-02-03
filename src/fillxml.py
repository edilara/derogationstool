import prepdata as prep
import xml.etree.ElementTree as et
from initxml import getXML, getRootXML


def setDerogations(root, userIdentity = 'TestGovt', country = 'XX'):
    userIdentity = str(input('userIdentity: ') or userIdentity) #none given --> default
    country = str(input('country: ') or country) #none given --> default
    
    root.set('userIdentity', userIdentity)
    root.set('country', country)
    return root

#in the tags
def setDirective(root, directive = 'http://rod.eionet.europa.eu/obligations/268'):
    for entry in root.findall('derogation'):
        entry.set('directive', directive)
    return root 

def setStatus(root, status = 'complete'):
    for entry in root.findall('derogation'):
        entry.set('status', status)
    return root 