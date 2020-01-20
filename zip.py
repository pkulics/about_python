
'''
python3中使用zip，由于python2中的zip函数不是生成器,会占用大量内存，故python2中使用izip
若不确定zip所封装的两个列表是否等长，可以使用zip_longest函数(python2中为izip_longest)
'''

#names和letters 存在关联
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(max_letters)

