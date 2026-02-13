
def check():
    with open("check_no_line_strat_vowel.txt","r") as f1:
        x=f1.readlines()
        c=0
        for i in x:
            if i[0].lower() in "aeiou":
                c+=1
        print(c)
check()
