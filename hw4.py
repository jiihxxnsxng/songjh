def  rep_char(nstr) :
    print("-"*nstr)




def draw_line_string():
    name=str(input("영어이름을 입력하세요:"))
    msg1="Hello "+name
    msg2="Welcome to seoul"
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)


    rep_char(nstr)
    print(msg1+"\n"+msg2)
    rep_char(nstr)
    


draw_line_string()
