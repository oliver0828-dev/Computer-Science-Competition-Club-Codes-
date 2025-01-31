arr1 = list(input())
arr2 = list(input())
# print(arr1)
# print(arr2)

point1 = 0
for i in arr1:
    if i == "A" or i=="R":
        point1+=1
    elif i == "O" or i == "G":
        point1+=3
    elif i == "B":
        point1+=6

point2 = 0
for i in arr2:
    if i == "A" or i=="R":
        point2+=1
    elif i == "O" or i == "G":
        point2+=3
    elif i == "B":
        point2+=6

# print(point1)
# print(point2)
#
# if point1 > point2 :
#     print(point1, point2)
# else:
#     print(point2, point1)


print(max(point1,point2), min(point1,point2))