import os
items = os.listdir("C:\\Users\\tanne\\Documents\\python_projects")



newlist = []
path = os.path.join
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print (newlist)

time = os.path.getmtime(items)
print(time)





