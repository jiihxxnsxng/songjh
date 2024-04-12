def read_single_digit(n):
    if n==0:
        return "영"
    elif n==1:
        return '일'
    elif n==2:
        return '이'
    elif n==3:
        return '삼'
    elif n==4:
        return '사'
    elif n==5:
        return '오'
    elif n==6:
        return '육'
    elif n==7:
        return '칠'
    elif n==8:
        return '팔'
    elif n==9:
        return '구'
    
    

def read_number(num):
    n1=num//100
    n2=(num%100)//10  
    n3=num%10

    if n1==0:
        if n2==0:
           return (read_single_digit(n3)) 
        else:
            return (read_single_digit(n2)+read_single_digit(n3))
    else:
        return (read_single_digit(n1)+read_single_digit(n2)+read_single_digit(n3))
    
    

    

num=int(input("세 자리 이하 정수 입력:"))
print(read_number(num))
