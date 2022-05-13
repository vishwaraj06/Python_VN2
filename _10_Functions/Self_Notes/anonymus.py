nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 == 0, nums))
print("Map:", odds)

print("*************************")
'''import functools
nums1= [1, 2, 3, 4, 5]
summ = nums1(reduce(lambda x, y: x + y, nums))
print(("reduce:",summ))
print("***************************")'''

seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))



