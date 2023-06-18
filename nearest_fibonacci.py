def nearestFibonacci(num):
	if (num == 0):
		print(0)
		return
	first = 0
	second = 1
	third = first + second
	while (third <= num):
		first = second
		second = third
		third = first + second
	if (abs(third - num) >
		abs(second - num)):
		ans = second
		print(ans)
	elif (abs(third - num) <
		abs(second - num)):
		ans = third
		print(ans)
	else:
	    print(second,end=" ")
	    print(third,end=" ")
if __name__ == '__main__':
	N = int(input())
	nearestFibonacci(N)