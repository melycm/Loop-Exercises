width = int(input("Width? "))
height = int(input("Height? "))

star = "*"

print('*' * width)
num_spaces = width -2 
spaces = ' ' * num_spaces
for i in range(height -2):
    print('*' + spaces + '*')


print('*' * width)
