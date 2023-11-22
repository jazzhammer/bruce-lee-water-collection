import math


# i call this solution "the bruce lee". ie: i had to think like water.
# ___.                             __                                    _____       .__                   .___
# \_ |__   ____   __  _  _______ _/  |_  ___________     _____ ___.__. _/ ____\______|__| ____   ____    __| _/
#  | __ \_/ __ \  \ \/ \/ /\__  \\   __\/ __ \_  __ \   /     <   |  | \   __\\_  __ \  |/ __ \ /    \  / __ |
#  | \_\ \  ___/   \     /  / __ \|  | \  ___/|  | \/  |  Y Y  \___  |  |  |   |  | \/  \  ___/|   |  \/ /_/ |
#  |___  /\___  >   \/\_/  (____  /__|  \___  >__| /\  |__|_|  / ____|  |__|   |__|  |__|\___  >___|  /\____ |
#      \/     \/                \/          \/     )/        \/\/                            \/     \/      \/
# https://www.youtube.com/watch?v=V4A37PDduls

# https://python-fiddle.com/saved/PH3XpQkYpc37BvmNcRgS

def collectRain(walls):
    if not walls or len(walls) < 2:
        return 0

    left, right = 0, len(walls) - 1
    max_left, max_right = walls[left], walls[right]
    total_water_collected = 0

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            max_left = max(max_left, walls[left])
            total_water_collected += max_left - walls[left]
        else:
            right -= 1
            max_right = max(max_right, walls[right])
            total_water_collected += max_right - walls[right]

    return total_water_collected

# Corrected test cases
if __name__ == '__main__':
    wall_expectations = [
        ([], 0),
        ([0], 0),
        ([1], 0),
        ([9991], 0),
        ([0, 1], 0),
        ([1, 0], 0),
        ([1, 1], 0),
        ([0, 0], 0),
        ([0, 0, 0], 0),
        ([1, 0, 0], 0),
        ([0, 1, 0], 0),
        ([0, 0, 1], 0),
        ([1, 1, 0], 0),
        ([1, 0, 1], 1),
        ([0, 1, 1], 0),
        ([1, 1, 1], 0),
        ([100, 1, 1], 0),
        ([1, 100, 1], 0),
        ([1, 1, 100], 0),
        ([3, 1, 100], 2),
        ([3, 10, 0], 0),
        ([4, 10, 2], 0),
        ([3, 10, 0, 8], 8),
        ([3, 0, 10, 0], 3),
        ([0, 0, 10, 8], 0),
        ([0, 10, 0, 8], 8),
        ([0, 0, 12, 0, 0], 0),
        ([0, 11, 12, 0, 0], 0),
        ([0, 12, 12, 0, 0], 0),
    ]

    for walls, expected in wall_expectations:
        actual = collectRain(walls)
        assert actual == expected, f"Failed for {walls}: expected {expected}, got {actual}"

    print("All tests passed!")
