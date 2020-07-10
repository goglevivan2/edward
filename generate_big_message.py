
somestring = 'wweddaadwaffrdnn'
for _ in range(100000//len(somestring)):
    with open('bigfile.txt','a') as file:
        file.write(somestring)


with open('bigfile.txt','r') as file:
    my_file=file.read()

print(len(my_file))