import xml.etree.ElementTree as ET
from lxml import etree
from support import get_xml_scheme_path



class xml_class:
    def __init__(self,xmlpath):
        self.filepath = xmlpath
        self.schemepath = get_xml_scheme_path('schema_table.xsd')
        self.tree = None
        self.root = None

    def xml_parse(xml_file):
        print("OK")

class Validator:
    def __init__(self, xsdpath):
        xmlschema_doc = etree.parse(xsdpath)
        self.xmlschema - etree.XMLSchema(xmlschema_doc)

    def validate(self, xmlpath):
        xml_doc = etree.parse(xmlpath)
        result = self.xmlschema.validate(xml_doc)
        return result


