data = list(range(1, 101))
result = []

def prime_number(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
        
    return True

for num in reversed(data):
    if prime_number(num):
        continue
    elif num % 3 == 0 and num % 5 == 0:
        result.append('FooBar')
    elif num % 3 == 0:
        result.append('Foo')
    elif num % 5 == 0:
        result.append('Bar')
    else:
        result.append(str(num))

print(" ".join(result))