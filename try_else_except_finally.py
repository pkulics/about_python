
'''
以读文件操作来举例：
try:尝试可能发生异常的代码
except:捕获try中产生的异常
else:如果try语句没有异常，则执行else语句
finally:最后一定会执行
'''

filename = "test.txt"
def divide_json(path):
    handle = open(path, 'r+')
    try:
        print("try ...")
        data = handle.read()
    except:
        print("except ...")
        return UNDEFINED
    else:
        print("else ...")
        for line in data:
            print(line)
            break
    finally:
        print('finally ...')
        handle.close()
 
divide_json(filename)
