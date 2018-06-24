import os

MAIN_DIRECTORY = os.path.dirname(os.path.dirname(__file__))
ICONS_DIRECTORY = os.path.join(MAIN_DIRECTORY, 'wxpython2/icons/')
XML_DIRECTORY = os.path.join(MAIN_DIRECTORY, 'wxpython2/xmlschemes/')
def get_fullpath(*path):
    return os.path.join(MAIN_DIRECTORY, *path)

def get_icon(*file_name):
    return os.path.join(ICONS_DIRECTORY, *file_name)

def get_xml_scheme_path(*file_name):
    res = os.path.join(XML_DIRECTORY, *file_name)
    return res