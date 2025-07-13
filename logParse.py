import os

files = []
for file in os.listdir(path='/Users/omerdartar/VsCode/Bootcamp6weeks/log'):
    if file.endswith('.log') and os.path.isfile(file):
        files.append(file)
print(files)






































