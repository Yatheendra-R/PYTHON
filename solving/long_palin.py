word=input("Enter the word: ")
max_pali=""
max_len=0
start_ind=-1
end_ind=-1
for i in range(len(word)):
    par_word=""
    for j in range(i,len(word)):
        par_word+=word[j]
        if (par_word==par_word[::-1]):
            if (len(par_word)>max_len):
                start_ind=i
                end_ind=j
                max_len=len(par_word)
                max_pali=par_word
print(max_pali)
print(max_len)
print(start_ind," ",end_ind)

