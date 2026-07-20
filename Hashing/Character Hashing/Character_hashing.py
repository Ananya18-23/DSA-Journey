s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

# Frequency array
hash_list = [0] * 26

# Store frequency of each character
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value-97
    hash_list[index] += 1
    
for ch in q:
    ascii_value = ord(ch)
    index = ascii_value-97
    print(hash_list[index])
    
print(hash_list)        