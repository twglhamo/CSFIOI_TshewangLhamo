#Use a break statement to exit a while loop when a certain condition is met
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("Loop ended")
