import os,sys
import random

def FDI(num,a):
	#https://scripbox.com/pf/fdi-vs-fpi/
	#stable
    value = a*(num)
    return value
def FPI(num,b):
	#https://scripbox.com/pf/fdi-vs-fpi/
	#volatile
    value = b*(num)
    return value
def debt(num):
	value = -(num)
	return value

if __name__ == "__main__":
	num = 10000
	a = random.choice([100, 1])
	b = 1
	print("direct investment",FDI(num,a))
	print("indirect investment",FPI(num,b))
	print("debt",debt(num))
	if a == 100:
		print("stable capital mobility",FDI(num,a)+FPI(num,b)+debt(num)+2000)
	if a == 1:
		print("volatile capital mobility",FDI(num,a)+FPI(num,b)+debt(num)+1)
	
