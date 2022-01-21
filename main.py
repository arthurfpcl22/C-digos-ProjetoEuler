"""
#Quadratic primes
import sympy
e=0
a_r=0
b_r=0
c=0
maior=0
for a in range (-1000,1000):
    for b in range (-1000,1001):
        for i in range (50):
            e=i*i + a*i + b
            while sympy.isprime(e):
                c=c+1
            if c>maior:
                a_r=a
                b_r=b




print(a_r)
print(b_r)

#fibonnaci 1
ant=1
i=2
vet=[]
for x in range(1000):

    v=i+ant
    if v>4000000:
        break
    if v%2==0:
        vet.append(v)
    ant=i
    i=v
soma=sum(vet)+2
print(soma)

#fibonnaci 2
ant=1
i=2
vet=[]
index=0
for x in range(10000):

    v=i+ant
    digits = len(str(v))
    vet.append(v)
    if digits == 1000:
        index=x
        break
    ant=i
    i=v
print(index+4)

import sympy

vet=[]
vetf=[]
c=0
ref=7
for b in range(10):
    for i in range(10):
        for j in range(10):
            for x in range(10):
                for h in range(10):
                    a = int(str(h)+str(b)+str(h)+str(j)+str(x)+str(i))
                    vet.append(a)
                    if sympy.isprime(a) and len(str(a))>4:
                        c=c+1

                if c==8:
                    vetf=vet
                    break
                c=0
                vet=[]
            if c == 8:
                break
        if c == 8:
            vetf = vet
            break
    if c == 8:
        vetf = vet
        break

print(vetf)
for g in vetf:
    if sympy.isprime(g):
        print(g)

vet=[]
vetf=[]
c=0
ref=7
for b in range(10):
    for i in range(10):
        for j in range(10):
            for x in range(10):
                for h in range(10):
                    a = int(str(b)+str(i)+str(j)+str(x)+str(h))
                    vet.append(a)

for i in vet:
    z=str(i)
    b=int(z[0])
    i=int(z[1])
    j=int(z[2])
    x=int(z[3])
    h=int(z[4])
    
print(vet)

#sum prime
import sympy
primos=[]
soma=0
soma_r=[]
for i in range(10000):
    if sympy.isprime(i):
        primos.append(i)

for i in primos:
    soma = soma+i
    if sympy.isprime(soma) and soma < 1000000:
        soma_r.append(soma)
print(soma_r)

#permutes multiples
import numpy as np
vet=0
um=[]
dois=[]
tres=[]
quatro=[]
cinco=[]
seis=[]
def ordenar(valor,vet):
    for i in valor:
        vet.append(int(i))
    vet.sort()
    return vet
for i in range (100000000):
    um=ordenar(str(i),um)
    dois=ordenar(str(2*i),dois)
    tres=ordenar(str(3*i),tres)
    quatro=ordenar(str(4*i),quatro)
    cinco=ordenar(str(5*i),cinco)
    seis=ordenar(str(6*i),seis)

    if i>100 and np.array_equal(um,dois) and np.array_equal(dois,tres) and np.array_equal(tres,quatro) and np.array_equal(quatro,cinco) and np.array_equal(cinco,seis):
        vet=i
        break
    um=[]
    dois=[]
    tres=[]
    quatro=[]
    cinco=[]
    seis=[]

print(vet)
print(um)
print(dois)
print(tres)
print(quatro)
print(cinco)
print(seis)

#palindrome
import numpy as np

mult=0
normal=[]
invertido=[]
polid=0

for i in range (1000):
    for x in range (1000):
        mult=i*x
        for a in str(mult):
            normal.append(a)

        invertido=np.flip(normal)
        if mult>polid and np.array_equal(normal,invertido):
            polid=mult
        normal=[]
        invertido=[]


print(polid)

#prime factor
import sympy
i=3
max = 1
num =600851475143
while i<=num:
  if sympy.isprime(i) and num%i==0:
    max=i
    print(max)
  i=i+1

print(max)

#smallest multiple
for i in range(1000000000000):
    if i!=0 and i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0 and i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:
        print(i)
        break

#sum square
squares=0
squares_of_the_sum=0
for i in range (101):
    if i>0:
        squares=i*i + squares
        squares_of_the_sum=i+squares_of_the_sum
        print(squares_of_the_sum)

squares_of_the_sum=squares_of_the_sum*squares_of_the_sum
print(squares_of_the_sum-squares)

#10001st prime
import sympy
primos=[]
for i in range(1000000000):
    if sympy.isprime(i):
        primos.append(i)
    if len(primos)>10002:
        break

print(primos[10000])

#triangle
vet=[]
a=0
b=0
c=0
for i in range (1000):
    for j in range (1000):
        for z in range (1000):
            if z>j and j>i and z*z == i*i + j*j:
                a=i
                b=j
                c=z
                print(a,b,c)
                if a+b+c==1000:
                    vet=[a,b,c]
                    break
        if a + b + c == 1000:
            vet = [a, b, c]
            break
    if a + b + c == 1000:
        vet = [a, b, c]
        break
print(vet[0]*vet[1]*vet[2])

#Largest product in series
n=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
vet=[]
vet_f=[]
index=0
x=0
mul=1
mul_f=0
for i in str(n):
    vet.append(int(i))
    x=x+1
    if x>13:
        for i in range (13):
            mul=mul*vet[index-i]
        if mul>mul_f:
            mul_f=mul
            vet_f=[]
            for i in range(13):
                vet_f.append(vet[index - i])

    index=index+1
    mul=1
print(vet)
print(vet_f)
print(mul_f)


import numpy as np
import sympy
vet=[]
for i in range(10):
    if sympy.isprime(i):
        vet.append(i)

print(np.sum(vet))
#1179908154

#triangle numbers obs:programa demora muito para compilar
#concluido
c=1
c2=0
for i in range(100000):
    if i>1:
        c=c+i
    for x in range(1, c + 1):
        if c%x == 0:
            c2 = c2 + 1
            print(c)
        if c2 > 500:
            break
    if c2 > 500:
        print(c)
        break
    c2=0

"""
























