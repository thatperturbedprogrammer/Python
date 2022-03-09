#list, for loop quiz
#print elements which are int and > 6 from given list

list1 = [1, "sid", 2, "sensei", 22, "stoic", 200, "neitzsche"]
print("list1 =",  list1, '\n')


print("Elements which are int and > 6 from given list: ")
for i in list1:
    if type(i) is int and i > 6:
        print(i,"is int and > 6")
