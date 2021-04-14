def reverseArray(arr):
    result = arr[::-1]
    for en, a in enumerate (result):
	    print (f'[{en}] : {a}')

    return result

arr = [9,7,8,6,5,4,3,2,1]

print(reverseArray(arr))