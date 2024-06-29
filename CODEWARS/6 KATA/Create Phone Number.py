def create_phone_number(n):
    str1 = ""
    str2 = ""
    str3 = ""
    for i in range(len(n)):
        if 0 <= i < 3: 
            str1 += str(n[i])
        elif 3 <= i < 6:
            str2 += str(n[i])
        else:
            str3 += str(n[i])
    return "("+str1+") "+str2+"-"+str3