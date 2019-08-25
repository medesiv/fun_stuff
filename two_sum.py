#Two Sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

# Approach 0
arr = [ 11, 15 , 7 , 2, 1, 9 , 8 ]
d = {}
target = 10

for i in range(len(arr)):
	d[arr[i]] = i
print(d)

for i in arr:
	pair = target - i
	print(pair)
	try:
		index = d.get(pair)
		if(index is not None):
			break
	except(KeyError):
		continue

if(index is not None):
	print(d.get(i),index)  
else:
	print("No indices found")


# Approach 1
'''
arr = [2, 7, 11, 15]
target = 18
index = None
for i in arr:
	pair = target - i
	try:
		index = arr.index(pair)
		break
	except(IndexError):
		pass
	except(ValueError):
		pass

if(index is not None):
	print("The indices are %s and %s" % (arr.index(i),index))
else:
	print("There are no such indices")

'''
#Approach 2
'''
def search_pair(arr,pair):

	if(len(arr)>=1):
		mid = (0 + (len(arr) -1))/2
		
		if(pair == arr[mid]):
			index = mid
			return index
		elif(pair > arr[mid]):
			search_pair(arr[mid:len(arr)-1],pair)
		elif(pair < arr[mid]):
			search_pair(arr[0:mid],pair)
		else:
			return None
	else:
		return None

arr = [ 11, 15 , 7 , 2, 1, 9 , 8 ]
new_arr = sorted(arr)
d = {}
for i in range(len(arr)):
	d[arr[i]] = i
print(d)

target = 19
for i in new_arr:
	pair = target - i
	print("Pair that I'm searching for is",pair)
	index = search_pair(new_arr,pair)
	if(index is not None):
		break

if(index is not None):
	print(new_arr[index])
	print("The indices are %s and %s" % (d.get(i),d.get(pair)))
else:
	print("There are no such indices")

'''


