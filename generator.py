
'''
如果数据量太大，用列表推导式会占用大量的内存，导致程序崩溃。
此时采用生成器表达式
'''
filename = "test.txt"
it = (len(x) for x in open("test.txt"))
print(it)

print(next(it))
print(next(it))

'''
连锁生成器表达式
生成器表达式之间互相结合，嵌套;
外围的迭代器每次前进时，都会推动呢不那个迭代器，这就产生了连锁效应，是的执行循环、评估条件表达式、对接输入和输出等逻辑都组合在了一起。
'''
#调用上面的it
roots = ((x, x**0.5) for x in it)
print(next(roots))
print(next(roots))



