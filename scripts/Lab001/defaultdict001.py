from collections import defaultdict

x = {'a': 1, 'b': 2}
print(x['c'])

x = defaultdict(int)
x['a'] = 1
x['b'] = 2
print(x['a'])
print(x['c'])
