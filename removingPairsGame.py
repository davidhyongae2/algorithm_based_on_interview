def removingPairsGame(a,b) :

    #run two loop one start at 0
    for i in range(0, len(a)):
        print("Iteration # : ", i + 1)
        #run second loop start at 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                print("Outer loop value : ", a[i], " Inner loop value : ", a[j])
                #remove repeat
                a.pop(j)
                print(a)
                break

    #run two loop one start at 0
    for i in range(0, len(b)):
        print("Iteration # : ", i + 1)
        #run second loop start at 1
        for j in range(i + 1, len(b)):
            if b[i] == b[j]:
                print("Outer loop value : ", b[i], " Inner loop value : ", b[j])
                #remove repeat
                b.pop(j)
                print(b)
                break

    #for j in range(1, len(a)):
    #    key = a[j]
    #    i = j - 1
    #    while i > 0 and a[i] > key:
    #        a[i + 1] = a[i]
    #        i = i - 1
    #    a[i + 1] = key
    #if a == key:
    #    a.pop()
    #print(a)

     #Check who won
    if len(a) < len(b):
       print("alice WON!");
    else :
       print("bob WON?");
         

if __name__ == "__main__" :
    a = [5, 2, 6, 6, 1, 3]
    b = [1, 3, 2, 5, 6, 4];
    removingPairsGame(a,b);

