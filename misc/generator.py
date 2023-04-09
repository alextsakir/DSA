def number():
    for index in range(4): yield index


for a in number(): print(a)
