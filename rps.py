import random
a={1:'r',2:'p',3:'s'}
c=a[random.randint(1,3)]
u=input("enter rock paper or siscor")
if(u==c):
	print("tie")
if(u=='s' and c=='p' or u=='p' and c=='r' or u=='s' and c=='r'):	
	print("user wins")
else:
	print("computer wins")


