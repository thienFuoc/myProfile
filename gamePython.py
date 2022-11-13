from random import randint

print('Nhập Kéo, Búa, Bao')

player = input()
computer = randint(0,2)
if computer==0:
    computer = 'Búa'
if computer==1:
   computer = 'Kéo'
if computer==2:
   computer = 'Bao'

print('--------')
print('Bạn chọn:' + player)
print('Máy chọn:' + computer)
print('--------')

if player==computer:
   print('Hòa')

if player=='kéo':
   if computer=='Búa':
      print('Thua')
   if computer=='Bao':
      print('Thắng')
elif player=='búa':
   if computer=='Bao':
      print('Thua')
   if computer=='Kéo':
      print('Thắng')
elif player=='bao':
   if computer=='Kéo':
      print('Thua')
   if computer=='Búa':
      print('Thắng')
else:
   print('Nhập lại')