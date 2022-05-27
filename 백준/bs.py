# arr=[]
# for i in range(10):
#     arr.append(int(input()))

# arr.sort()

## arr = [1,2,3,4,5]
## 3의 인덱스 찾아야함 2


arr = [1,2,3,4,5,6]

target = 6
s=0
e=max(arr)
result=0
while s<=e:

    mid = (s + e) // 2

    if arr[mid] == target:
        result = mid
        break

    elif arr[mid] > target:
        e = mid - 1

    elif arr[mid] < target:
        s = mid + 1

print(result)

     


