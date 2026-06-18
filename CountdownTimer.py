import time

hours = int(input("Enter hours: "))
seconds1 = hours*3600
# print(f"{hours}hr = {seconds1}secs")

mins = int(input("Enter minutes: "))
seconds2 = mins*60
# print(f"{mins}mins = {seconds2}secs")

secs = int(input("Enter seconds: "))

total_seconds = seconds1+seconds2+secs
print(f"Your timer is set for {total_seconds}secs")

for x in range(total_seconds, 0, -1):
    secs = x % 60
    seconds2 = int(x/60) % 60
    seconds1 = int(x/3600)
    print(f"{seconds1:02}:{seconds2:02}:{secs:02}")
    time.sleep(1)

print("TIMES UP!")