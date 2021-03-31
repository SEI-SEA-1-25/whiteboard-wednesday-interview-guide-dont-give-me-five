num1, num2 = input("What range should we cover? (separate the numbers with a space)").split()
num1 = int(num1)
num2 = int(num2)

# main solution
for num in range(num1, num2 + 1):
  if ("5" in str(num)) == False:
    print(num)

# using while loop instead of range
num = num1
while num <= num2:
  if ("5" in str(num)) == False:
    print(num)

  num += 1

# using `not` instead of `== False`
for num in range(num1, num2 + 1):
  if not "5" in str(num):
    print(num)

# with fancy inline number conversions (doesn't need lines 2-3)
for num in range(int(num1), int(num2) + 1):
  if ("5" in str(num)) == False:
    print(num)
