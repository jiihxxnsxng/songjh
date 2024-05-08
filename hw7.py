shopping_bag = {} 
while True:
    item = input('상품명은?')
    
    if item=='':
        break
    n=input('수량은?')    
    print('장바구니에',item, n + '개가 담겼습니다')
    
    shopping_bag[item]=n
print('장바구니보기:',shopping_bag)

item=input("확인하고 싶은상품은?")
print(item+'은(는)',shopping_bag.get(item)+'개 담겼습니다')
