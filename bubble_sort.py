#!/home/davidgae/src/amber18/miniconda/bin/python

def bubblemod():
  list2 = [0,1,2,3,4,5,6,7,8,9,10]
  list1 = [0,1,2,3,4,5,6,7,8,9,10]
  #if using range than count start of array position.
  for i in range(0,11):
  #if it is list value then array element is fixed.
  	list2[i] = list1[10-i]
  #return at fixed start of the array element
  return list2

def reverse():
    result = 0
    for y in range(0,11):
        #value 0..n
        # dividle the value to get the reminder result
        #  result = 0 * 11/10 = 1'
	result = result * 10 + y % 10 
	y /=10
        #for each string, join value with a comma
    	result2 = (',').join(str(result))
    return result2

if __name__ == '__main__':
   for i in range(0,1000000):
   	print(bubblemod())
   for i in range(0,1000000):
   	print(reverse())
