word=input("Enter the word: ")
fg=0
while (fg==0):
    word1=""
    fg1=0
    x=0
    while(x<len(word)):
        #assade
        #abccbccba
        #print(word)
        if (x==0):
            if (word[x]==word[x+1]):
                 #print(word1)
                 fg1=1
            else:
                word1+=word[x]
                #print(word1)
        elif (x!=len(word)-1):
            if ((word[x]==word[x+1])or (word[x]==word[x-1])):
               #word1+='0'
                #print(word[x])
                #print(word1)
                fg1=1
            else:
                word1+=word[x]
                #print(word1)
                
        else:
            if(word[x]==word[x-1]):
                #word1+='0'
                fg1=1
                #print(word1)

            else:
                word1+=word[x]
                #print(word1)

        x+=1
    if (fg1==0):
        fg=1
    else:
        word=word1
print("final:" ,word)       
        
