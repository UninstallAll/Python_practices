import glob

from main import number

myfiles = glob.glob('../files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

# for i in myfiles:
#     i = i.strip('../files\\')
#     myfiles.append(i)

myfiles = [i.strip('../files\\') for i in myfiles]
print(myfiles)