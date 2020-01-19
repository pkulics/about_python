
'''
步进,stride
'''
#对ascii可用
x = b'success'
y = x[::-1]
print(y)

#对unicode字符(utf-8)
w = "你好,我们都是大好人"
#x = w.encode('utf-8')
y = w[::-1]
print(y)
#z = y.decode("utf-8")



'''
利用步进stride,将列表中偶数索引和技术索引分别提取
'''
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(a)
print(odds)
print(evens)

