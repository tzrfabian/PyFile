import array

x = array.array('i',[1,2,3,4,5])
print(x)
print(type(x))

# nilai = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

# print(nilai)
# print(nilai[0])

# var_list = [1,2,3]
# for elemen in var_list:
#     print(id(elemen))

# var_arr = [0 for i in range(10)]
# for i in range(10):
#     var_arr[i] = i

# print(var_arr)

var_arr = [1,2,3,4,5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
    
    print(f"Current element: {current_element}, Next element: {next_element}")
