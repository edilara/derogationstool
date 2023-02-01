import xmlschema
from src.initxml import getXML

def load_xsd(path = 'derogations.xsd'):
    return xmlschema.XMLSchema(path)

def validate(xsd, xml = 'empty.xml'): 
    return xmlschema.validate(xml, xsd)

def main():
    return validate(xsd = load_xsd(), xml = validate(getXML()))