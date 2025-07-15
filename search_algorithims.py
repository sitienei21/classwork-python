arr = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 99
start = 0
end = len(arr) - 1
found = False

# for i in arr:
#     if arr[i] == key:
#        print("Found")
#        break
#     else:
#         print("Not found")

while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
        print("Found Element at pos:", mid)
        found = True
        break
    elif key < arr[mid]:
        end = mid - 1
    elif key > arr[mid]:
        start = mid + 1

if not found:
    print(f"{key} not found in the list!")