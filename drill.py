import os
items = os.listdir("C:\\Users\\tanne\\Documents\\python_projects")



path = os.path.join("C:\\Users\\tanne\\Documents\\python_projects") 
for names in items:
    if names.endswith(".txt"):
        time = os.path.getmtime("C:\\Users\\tanne\\Documents\\python_projects")
        print (names, time)









