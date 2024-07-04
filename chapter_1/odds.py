from datetime import datetime
datetime.today().minute
odd = []
for nums in range(1, 60):
    if nums%2 == 1:
        odd.append(nums)
rightThisMinute = datetime.today().minute
if rightThisMinute in odd:
    print('this seems a little odd.')
else:
    print('not an odd minute.')