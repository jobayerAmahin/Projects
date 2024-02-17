print('Welcome to simple game!')

gaming=input("Do you wanna play?")

if gaming.lower() !="yes":
    quit()

print('OK. lets play')
score=0

ans=input('What does DOM stands for?')

if ans=='Document Object Model':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

ans1=input('What is Central Processing Unit short form?')

if ans1.upper() =='CPU':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

print('You got'+ str(score)+'quiestions correct')
print('You got'+str((score/4)*100)+'percentage %')