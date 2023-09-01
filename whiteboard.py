# “Four People and a Bridge” Challenge:
# Challenge: Four people need to cross a bridge at night. They have only one flashlight, and the bridge is too dangerous to cross without it. The bridge can only hold two people at a time. The four people walk at different speeds: one can cross in 1 minute, another in 2 minutes, the third in 5 minutes, and the slowest in 10 minutes. When two people cross the bridge together, they must go at the slower person’s pace. What’s the fastest time they can all get across?
# Coding/Real-Life Connection: This problem teaches the importance of strategic planning and prioritization. In coding, it’s akin to optimizing processes by prioritizing tasks based on their weights or importance. In real-life situations, this skill is essential in project management or any scenario where resources (like time) are limited.


# info:
# four people
# 1 flashlight
# bridge can hold 2 people at a time and requires flashlight to cross
# jerry = 1 min
# sally = 2 min
# ben = 5 min
# edna = 10 min
# when 2 people cross, must go at slowest person's pace


# want:
# what is the fastest time we can get everyone across?

# they need to take flashlight back so someone must return. The fastest person should always be in the group of 2 so that they can make the return trip back.

# trips:
# jerry + sally = 2 min
# jerry back = 1 min
# jerry + ben = 5 min
# jerry back = 1 min
# jerry + edna = 10 min

# total: 19 min

# jerry + sally = 2 min
# jerry back = 1 min
# ben + edna = 10 min
# sally back = 2 min
# jerry + sally = 2 min

# total = 17 min

# Bridge Crossing Coding Challenge

# Problem Statement

# Four people need to cross a bridge at night. They have only one flashlight, and the bridge is too dangerous to cross without it. The bridge can only hold two people at a time. Each of the four people walks at a different speed: one can cross in 1 minute, another in 2 minutes, the third in 5 minutes, and the slowest in 10 minutes. When two people cross the bridge together, they must go at the slower person's pace.

# Write a Python function to determine the minimum total time for all four people to cross the bridge.

# Constraints
# - The list of speeds will always have exactly 4 elements, representing the 4 people's speeds.

# Function Signature


def min_crossing_time(speeds):
    total_time = 0
    speeds.sort()
    # trip 1 (two fastest)
    total_time += speeds[1]
    # trip back 1 (fastest back)
    total_time = total_time + speeds[0]
    # trip 2 (two slowest)
    total_time = total_time + speeds[3]
    #  trip back 2 (second fastest back)
    total_time = total_time + speeds[1]
    # trip 3 (final trip with two fastest)
    total_time = total_time + speeds[1]
    return total_time

# Testing the function
print(min_crossing_time([4, 7, 2, 10]))  # Should return 17