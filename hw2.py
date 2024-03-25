def get_integer():
    amount = int(input("금액을 입력하시오:"))
    return amount

def exchange(amount):
    c500 = amount // 500
    amount %= 500

    c100 = amount // 100
    amount %= 100

    c50 = amount // 50
    amount %= 50

    c10 = amount // 10

    print("500원:", c500, "개")
    print("100원:", c100, "개")
    print("50원:", c50, "개")
    print("10원:", c10, "개")

amount = get_integer()
exchange(amount)
