def my_abs(x):
    if x >=0:
        return x
    else:
        return -x
    

#print (my_abs(-99))

def my_pkg(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#print (power(6,5))
 
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#print([L[0],L[1],L[2]])
print(L[2:3])

