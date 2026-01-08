#Check number is Aramstrong or Not 
n = int(input('Enter any Postive Number : '))
orignal = n
lod=int(len(str(n)))
total = 0
while (n > 0):
    ld = n % 10
    total = total + (ld ** lod)
    n = n // 10
if (orignal == total):
    print('Armstrong Number')
else:
    print('Not Aramstrong')


