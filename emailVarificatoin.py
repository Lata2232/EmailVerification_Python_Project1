email=input("Enter your email id : ")
k,l,m=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if (email[-4] ==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            l=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else :
                        m=1
                if(k==1 or l==1 or m==1):
                    print("Wrong email id as it contains space or upper case alphabet .")
                else:
                    print("Correct email id.")
            else:
                print("Wrong email id as it contains dot symbol not in positon -4 or -3")
        else:
            print("Wrong email id as it contains >1 @ symbol ")
        
    else:
        print("Wrong email id as not starting with an alphabet.")
else:
    print("Wrong email id as it's length is <6. ")