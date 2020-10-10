
k = input('Enter a number, I will make my calculation below that number')
k = int(k)
a = input('Enter a number to see its multiples below first number')
b = input('Enter a number to see its multiples below first number')
a = int(a)
b = int(b)
x= range(1, k, 1)
f = []
for n in x:
    if n % a == 0 or n % b == 0:
        f.append(n)
if len(f) <= 20:
    print(f)

sum(f)


