#DICE
import random

while True:
	i=input("enter'n'to stop")
	if(i=='n'):
		print("BYE!")
		exit()
	else:
		print("you got",random.randint(1,6))