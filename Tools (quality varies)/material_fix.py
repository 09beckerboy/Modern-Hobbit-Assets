import os

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for filename in files:
        path = os.path.join(root, filename)
        if filename.endswith(".mtl"):
            with open(path, 'r') as file :
                filedata = file.read()
                print("Read "+filename)
            filedata = filedata.replace('.xbmp', '.png')
            print("Replaced text in "+filename)
            with open(path, 'w') as file:
                file.write(filedata)
                print("Wrote "+filename)