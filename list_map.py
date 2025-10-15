ages = [1,2,3,4]
alpha = ['animal', 'bag', 'coat', 'dobber']

# ages in 10 years time
ages_plus_ten= list(map(lambda num: num + 10, ages))

capital_alpha = list(map(str.capitalize, alpha))

print(ages_plus_ten)
print(capital_alpha)