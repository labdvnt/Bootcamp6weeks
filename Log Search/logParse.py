import os

log_dir = '/Users/omerdartar/VsCode/Bootcamp6weeks/log'
files = []

for file in os.listdir(path=log_dir):
    full_path = os.path.join(log_dir, file)
    if file.endswith('.log') and os.path.isfile(full_path):
        files.append(file)

out = open('total.log', 'w')

for file in files:
    full_path = os.path.join(log_dir, file)
    filename = file[:-4]  # dosya adından ".log" uzantısını çıkar
    with open(full_path, 'r') as f:
        for line in f:
            if line.find('RncFunction=1,IubLink=Iub_') > 0 and (line.find('DISABLED') > 0 or line.find('ENABLED') > 0):  
                out.write(filename+' '+line)
    f.close()
out.close()

with open ('total.log', 'r') as f:
    for line in f:
        print(line)