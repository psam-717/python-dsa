# a list with 5 elements
nums = list(range(5))

# even numbers
even_nums = list(range(2,10,2))

# odd numbers
odd_nums = list(range(1,10,2))
print(odd_nums)

num = 8

# left angle triangle
print("\nLeft-angle triangle")  
for i in range(num):
    print('*' * i)
  
  
print("\n Right-angle triangle")
for i in range(num):
    print(" " * (num-i-1), "*" * i)


print("\nFull triangle")  
for i in range(num):
    print(" " * (num-i-1), '*' * (2*i-1))
    


