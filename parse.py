import xml.etree.ElementTree as ET

input_file = 'example.xml'
namespace = 'http://example.com'
element_name = 'example'

tree = ET.parse(input_file)
root = tree.getroot()
element_search = '{%s}%s' % (namespace, element_name)
elements = root.findall('.//%s' % (element_search))

print(len(elements))
