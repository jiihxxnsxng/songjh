def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    result=r*r*3.14
    return result

r=get_radius('반지름 입력')
print('원의 넓이는:',get_circle_area(r))
