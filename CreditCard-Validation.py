# 1.Remove any '-' or ' '
# 2. Add all digits in the odd places from right left
# 3. Double every second digit from right to left
#        (If result is a two digit number,
#         Add the two digit number together to get a single digit)
# 4. sum the total of steps 2 & 3
# 5. If the sum is divisible by 10, the vredit card is # is valid

sum_odd = 0
sum_even = 0
total = 0

#Step 1
card_num = input("Enter your card number #: ")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]

#Step 2
for x in card_num[::2]:
    sum_odd += int(x)

#Step 3
for x in card_num[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even += (1 + (x % 10))
    else:
        sum_even += x

#Step 4
total = sum_odd + sum_even

#Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")