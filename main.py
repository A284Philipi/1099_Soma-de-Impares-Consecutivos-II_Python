casos = int(input())
for x in range (0, casos):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    soma = int(0)
    if (a > b):
        z = int(b)
        b = a
        a = z
    a = a + 1
    while a < b:
        if (a%2 == 1):
            soma = soma + a
        a = a + 1
    print(soma)