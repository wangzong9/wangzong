lst=['hello','world',98,100.5]
print(lst)



lst2=list('helloworld')
lst3=list(range(1,12,2))
print(lst2)
print(lst3)

print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o'))
print(lst2.index('o'))

lst4=[10,20,30]
print(lst4)
#删除列表
del lst4
print(lst4)