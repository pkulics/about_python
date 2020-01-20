
'''
range在一系列整数上面迭代
'''
random_list = [] 
for i in range(64):
    random_list.append(i)
print(random_list)


flavor_list = ['vani', 'chocolate', 'pecan', 'strawberry']
#直接在列表上迭代
for flavor in flavor_list:
    print('%s is delicious ' % flavor)

#1、通过下标迭代,比较生硬，建议用enumrate取代range
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d:%s' % (i+1, flavor))

#enumerate
for i, flavor in enumerate(flavor_list):
    print('enumerate:%d:%s' % (i, flavor))

#指定计数时用的值
for i, flavor in enumerate(flavor_list, 1):
    print('enumerate:%d:%s' % (i, flavor))


