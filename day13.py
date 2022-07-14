# list = ['Rishabh', 'Sachin', 'Dheeraj', 'Shubham']
# # print(list[-1][-1])


# list2 = list
# list3 = list2
# list4 = list3
# list4[3] = 'Ikram'

# print(list)
# -------------------------------------------------

# list2 = list*2
# print(list2)

# -------------------------------------------------

# print(list("hello"))
#  ------------------------------------------------

# num = [3, 4, 5, 6]
# sum = 0
# for i in num:
#     sum+=i

# avg = sum/len(num)
# print(avg)

# -------------------------------------------------

# num = 12
# num_reversed = list(str(num))
# print(int(f"{num_reversed[1]}{num_reversed[0]}"))

# -------------------------------------------------

# num = 69
# digits = list(str(num))
# print(int(digits[0]) + int(digits[1]))

# -------------------------------------------------

# a=int(input("Enter number: "))
# k=0
# for i in range(2,a//2+1):
#     if(a%i==0):
#         k=k+1
# if(k<=0):
#     print("Number is prime")
# else:
#     print("Number isn't prime")

# -------------------------------------------------

# num = 496
# sum = 0
# for i in range(1, num):
#     if num%i==0:
#         sum+=i

# if sum == num:
#     print('perfect')
# else:
#     print('not perfect')

# -------------------------------------------------

# sum1=0
# num=int(input("Enter a number:"))
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     print(r)
#     while(i<=r):
#         f=f*i
#         i=i+1
#     sum1=sum1+f
#     num=num//10
# if(sum1==temp):
#     print("The number is a strong number")
# else:
#     print("The number is not a strong number")

# -------------------------------------------------

# a = [2, 3, 1, 5, 7]
# a.sort()

# print(a[-2])
# print(a[::-1])

# -------------------------------------------------

# s1 = 'abcd'
# s2 = 'bcde'

# b = list(set(s1)&set(s2))

# for i in b:
#     print(i)

# -------------------------------------------------