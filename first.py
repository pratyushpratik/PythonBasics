

'''
numbers
'''
print(3 + 4)
print(3 * 4)
print(12 / 4)
print(8 + 4 * 10) #bodmas
print((3 + 4) * 10)
print(18 / 4)
print(18 // 4)
print(18 % 4)
print(5 * 5 * 5)
print(5 ** 3)


'''
variables
'''
tuna = 5
print(3 + tuna)
bacon = 18
print(bacon/tuna)


'''
Strings
'''
print("Pratyush Pratik")
print('Pratyush Pratik')
print("I don't think she is 18")
print('she said "hey"')
print('I don\'t think she is 18')
print('C:\Bucky\nudePics')
print(r'C:\Bucky\nudePics')

firstName = "pratyush "
print(firstName + "pratik")
print(firstName * 5)


'''
Slicing Up Strings
'''
user = "pratyush pratik"
print(user[0])
print(user[-1])
print(user[-3])
print(user[2:10])
print(user[:10])
print(user[2:])
print(user[:])
print(len(user))


'''
Lists
'''
players = [29,58,66,71,87]
print(players[2])
players[2] = 68
print(players)
playerss = players + [90,91,98]
print(playerss)
players.append(120)
print(players)
print(players[:2])
players[:2] = [0,0]
print(players)
players[:2] = []
print(players)
players[:] = []
print(players)


'''
if elif else
'''
age = 27

if age > 29:
    print("alcohol allowed")
elif age is 27:
    print("ok")
else:
    print("alcohol not allowed")


'''
for
'''
food = ['chicken','mutton','chickenBiryani','fish','fishFry']

for f in food:
    print(f)
    print(len(f))

for f in food[:2]:
    print(f)
    print(len(f))

'''
range
'''
for x in range(10):
    print(x)

for x in range(5,12):
    print(x)


for x in range(10,40,5):
    print(x)


'''
while
'''
buttcrack = 5

while buttcrack < 10 :
    print(buttcrack)
    buttcrack += 1


'''
comments and break
'''
#hey

'''
while buttcrack < 10 :
    print(buttcrack)
    buttcrack += 1
'''

magicNumber = 26
print(9, "pratyush")

for n in range(100):
    if n == magicNumber:
        print(n,"magic number")
        break
    else:
        print(n,"nonmagicnumber")

'''
continue
'''
numberTaken = [2,5,12,13,17]
print("here are number still available")

for n in range(1,20):
    if n in numberTaken:
        continue
    print(n)

'''
function
'''
def show():
    print("heyyy its showing toast")

show()

def add(a,b):
    print(a+b)

add(5,4)

def arithmetic(a,b):
    return a+b,a-b,a*b,a/b

arith = arithmetic(5,4)

print(arith)
print(arith[3])

def gender(gen='Unknown'):
    if gen is 'm':
        gen = 'Male'
    elif gen is 'f':
        gen = 'Female'
    print(gen)

gender('m')
gender('f')
gender()

def datingGirlsAge(myAge):
    return (myAge/2 + 7)

print(datingGirlsAge(23))
print(datingGirlsAge(22))

'''
keyword argument
'''
def eat(name='pratyush',food='chicken'):
    print(name,"loves",food)

eat()
eat(name='pratik')
eat(food='mutton')


'''
flexible number of argument
'''
def addNumber(*args):
    total = 0
    for t in args:
        total += t

    print(total)

addNumber(10)
addNumber(10,20,30,40,50)


'''
unpacking argument
'''