def countWords():
    fileName=input("Enter a file name")
    print(fileName)
    file=open(fileName,"r")
    total=0
    for line in file:
        print(line)
        word=line.split()
        print(word)
        print("The number of words in this line are",len(word))
        total=len(word)+total
    print("Total number of words are",total)
countWords()