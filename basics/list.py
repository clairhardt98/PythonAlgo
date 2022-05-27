x=['apple','banana','grape','kiwi']
print('scanning array using index')
for i in range(len(x)):
    print(x[i])

print('scanning array using enumerate')
for i, name in enumerate(x):
    print(name)

print('scanning array using enumerate2')
for i, name in enumerate(x,1):
    print(name)

print('scanning array not using index')
for i in x:
    print(i)