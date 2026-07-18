n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

hash_list=[0] * 11  # Assuming the maximum value in n is less than 100

for num in n:
    hash_list[num] += 1

for x in m:
    if x<1 or x>10:
        print(0)
    else:
        print(hash_list[x])    
print(hash_list)