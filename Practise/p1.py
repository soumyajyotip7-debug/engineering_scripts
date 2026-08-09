# age = int(input("age! = "))
# print(age)
# if age >=18:
#     print("you are an adult!")
# else:
#     print("you are too young!")
    
    
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i  + 1):
#         print(j, end='')
#     print('')
    
# rows = 5
# b = 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end='')
#     print('\r')
    
rows = 5
b = rows
for i in range(rows, 0, -1):
    # b -= 1
    for j in range(0, i):
        print(b, end='')
    print('\r')