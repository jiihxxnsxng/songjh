shopping_bag = {}

def buy(shopping_bag):
    while True:
        item = input('상품명은? : ')
        if item == '':
            break
        num = input('수량은? ')
        print(f'장바구니에 {item} {num}개가 담겼습니다')
        shopping_bag[item]=num

def show(shopping_bag):
    print('장바구니 보기:', shopping_bag)

def find(shopping_bag):
    item = input("확인하고 싶은 상품은? ")
    if item in shopping_bag:
        print(f"{item}은(는) {shopping_bag[item]}개 담겼습니다")
    else:
        print(f"장바구니에 {item}은(는) 없습니다.")

buy(shopping_bag)
show(shopping_bag)
find(shopping_bag)
