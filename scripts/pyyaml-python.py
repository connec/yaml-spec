import json, yaml
from collections import OrderedDict
from StringIO import StringIO

spec = json.load(open('../spec.json', 'r'), object_pairs_hook=OrderedDict)

for name, tests in spec.iteritems():
  io = StringIO()
  io.write('%s\n  ' % name)
  for test in tests:
    result = yaml.safe_load(test['yaml'])
    if result == test['json']:
      io.write('.')
    else:
      io.write('F')
      io.write('\n    yaml: %s' % test['yaml'])
      io.write('\n    expected: %s' % json.dumps(test['json']))
      io.write('\n    received: %s\n  ' % json.dumps(result))
  print io.getvalue()