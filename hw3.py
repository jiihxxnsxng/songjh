def get_fixed_price(S_cost, discount):
    F_cost = S_cost * ((100 - discount) / 100)
    return F_cost

discount = int(input("할인률을 입력하세요(%) :"))
S_cost_A = int(input("A 상품의 할인된 가격은? "))
S_cost_B = int(input("B 상품의 할인된 가격은? "))


F_cost_A = get_fixed_price(S_cost_A, discount)
print("A 상품의 정가는:", F_cost_A)


F_cost_B = get_fixed_price(S_cost_B, discount)
print("B 상품의 정가는:", F_cost_B)
