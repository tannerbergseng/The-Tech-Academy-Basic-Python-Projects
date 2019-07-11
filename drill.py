import os
items = os.listdir("C:\\Users\\tanne\\Documents\\python_projects")

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print (newlist)
