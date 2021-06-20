listone = [1,2,3,4]
listtwo = ['axe','bat','cat','dog']
listthree = listone + listtwo
print (list(listthree))
print(listthree[2])

listfour = zip(listone, listtwo)
print(list(listfour))

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(4,6)
print(a[x])
