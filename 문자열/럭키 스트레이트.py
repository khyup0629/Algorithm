num = input()

left, right = 0, 0
for i in range(len(num)//2):
    left += int(num[i])

for i in range(len(num)//2, len(num)):
    right += int(num[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
