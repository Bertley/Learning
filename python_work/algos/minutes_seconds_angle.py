"""

Find the angle between the minute hand and the second hand in a given time. 
"""
def angle(minute, second):
    diff = max(minute, second) - min(minute, second)
    print(diff * 6)

angle(0, 60)