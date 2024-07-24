def sentence(string:str):
    words=string.split()
    index=0
    while index<len(words):
        yield words[index]
        index+=1
    

for x in sentence("Happy Birthday to you"):
    print(x)