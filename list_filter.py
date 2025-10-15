ages = [10, 22, 32, 12, 16]
names = ['Marvin', 'Michael', 'Maxwell', 'Phillip']

# ages less than 18
less_than_18 = list(filter(lambda num: num < 18, ages))

m_begin_names = list(filter(lambda name: name.startswith('M') , names))

print(m_begin_names)

print(less_than_18)