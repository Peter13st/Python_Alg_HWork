import random
li= []
r = int(input('how many array items?: '))
for i in range(r):
    li.append(random.randint(-100, 99))
print('native array')
print(li)

n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] < li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
print('sort descend')  
print(li)

n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
print('sort ascend')     
print(li)

