import os
localPath = "C:\\Users\\tanne\\Documents\\python_projects"
items = os.listdir(localPath)



path = os.path.join(localPath) 
for names in items:
    if names.endswith(".txt"):
        time = os.path.getmtime(localPath)
        print (names, time)









