#function to get array value
def arrayshift(arr):
    for i in range(0, len(arr)):
        print(arr[i])


#initial values in the array
given_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print statement of intial values. 
#print('Given Array :')
#print the current array.
#print(arrayshift(given_arr))


#access array 3 times. 
n=3

#loop through the array, in this case, access the array 3 times.
for i in range(0, n):
    #current array, access 8th position.
    last_element = given_arr[-1]
    #change the values as the element goes to the beginning.
    #eg.   9th values, -3 = 6th position. 
    #eg.   8th values, -3 = 5th position.
    #eg.   7th values, -3 = 4th position.
    for j in range(len(given_arr) -1, -1, -1 ):
    #eg.   current 6th - 1 = 5th, store this value in given_arr[j]
        given_arr[j] = given_arr[j - 1]
    #eg. 0 equal to 9th position
    #eg. 1st equal to 8th position.
    given_arr[0] = last_element

if __name__ == "__main__":
	#print  result
        print('Result:')
	print(arrayshift(given_arr))
