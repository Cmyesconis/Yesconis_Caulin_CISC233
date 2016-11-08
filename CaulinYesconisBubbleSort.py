# x = [100,99]
# print(x)

# for i in range(5,1,-1)

# temp = x[0]
# x[0] = x[1]
# x[1] = temp
# print(x)


# FOR REVERSING A LIST
# x = [12,23,43,54,56,67]
# for i in range(len(x)-1,0,-1):
# 	print(i)
# 	for j in range(i):
# 		print ('j :',x[j])


# BUBBLE SORT ALGORITHM
def bubbleSort(alist):
# false = flag

	# if alist[i]>alist[i+1]:
		for passnum in range(len(alist)-1,0,-1):
			for i in range(passnum):
				if alist[i]>alist[i+1]:
					temp = alist[i]
					alist[i] = alist[i+1]
					alist[i+1] = temp
					for flag in(alist):
						if alist[i]>alist[i+1]:
							print(alist)



alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# Check
# False = flag
# for flag():
# 	for():
# 		if alist[i]>alist[i+1]
# 		print(alist)