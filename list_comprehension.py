
'''
推荐:列表表达式
在列表推导中，最好不要使用两个以上的表达式。可以使用两个条件、两个循环、或一个条件搭配一个循环。如果要写的代码比这还要复杂，那就应该使用普通的if和for语句，并编写辅助函数。
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
squares = [x**2 for x in a]
print('squares:',squares)

#过滤可以被2整除的数
even_squares = [x**2 for x in a if x%2==0]
print('even_squares',even_squares)

#两个for循环的列表表达式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print("flat:",flat)
squared__matrix = [[x**2 for x in row] for row in matrix]
print("squared__matrix:",squared__matrix)

#多个for循环,(不够清晰)
my_lists = [
        [[1,2,3],[4,5,6]],
        [[2,2,4],[12,3,43]],
        [[5,4,2],[1,2,2]]
    ]
flat = [x for sublist1 in my_lists
            for sublist2 in sublist1
                for x in sublist2]
print("flat_my_lists:",flat)

#if 条件,可并列默认and形式
b = [x for x in a if x > 4 if x % 2 == 0 ]
c = [x for x in a if x > 4 and x % 2 ==0]
print("b:", b)
print("c:", c)

'''
繁琐:map
'''
map_squares = map(lambda x : x**2, a)
print('map_squares:',squares)

#滤可以被2整除的数
alt = map(lambda x:x**2,filter(lambda x:x%2 == 0, a))
assert even_squares == list(alt)
print("alt",alt)


'''
字典：dict
集合：set
'''
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

