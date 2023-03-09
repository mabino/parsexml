from lxml import objectify

input_file = 'example.xml'
namespace = 'http://example.com'
element_name = 'example'

root = objectify.parse(input_file).getroot()
namespace_map = {'ns': namespace}
elements = root.xpath('.//ns:%s' % (element_name), namespaces=namespace_map)

print(len(elements))
