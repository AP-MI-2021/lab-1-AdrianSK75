'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if n == 1:
        return 0

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return 0
        divisor+=1

    return 1

def test_is_prime():
    n = int(input())
    if is_prime(n) == 1:
        print(1)
    else:
        print(0)

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    product = 1
    for element in lst:
        product *= element

    return product

def init_elem_prod():
    length = int(input())
    lst = []
    for i in range(length):
        lst.append(int(input()))

    print(get_product(lst))


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def init_elem_cmmdc(problem):
    x = int(input())
    y = int(input())

    if problem == "3":
        print(get_cmmdc_v1(x, y))
    else:
        print(get_cmmdc_v2(x, y))

def main():
    problem = input("Choose the problem:")
    
    if problem == "1":
        test_is_prime()
    elif problem == "2":
        init_elem_prod()
    elif problem == "3" or problem == "4":
        init_elem_cmmdc(problem)
        
if __name__ == '__main__':
    main()
