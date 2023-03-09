from lxml import etree

input_file = 'example.xml'
namespace = 'http://example.com'
element_name = 'example'

tree = etree.parse(input_file)
namespace_map = { 'ns' : namespace }
elements = tree.xpath('.//ns:%s' % (element_name), namespaces=namespace_map)

print(len(elements))
