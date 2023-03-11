from datetime import time

# [('12:00AM', '12:00AM'), ('12:30AM', '12:30AM'), ....... ('11:30PM', '11:30PM')]

# for h in range(0, 24):
#     for m in (0, 30):
#         print(time(h, m).strftime('%I:%M %p'))

t = [(time(h, m).strftime('%I:%M %p'), time(h, m).strftime('%I:%M %p')) for h in range(0, 24) for m in (0, 30)]
print(t)