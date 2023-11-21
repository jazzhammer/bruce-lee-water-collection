import math


# i call this solution "the bruce lee". ie: i had to think like water.
# ___.                             __                                    _____       .__                   .___
# \_ |__   ____   __  _  _______ _/  |_  ___________     _____ ___.__. _/ ____\______|__| ____   ____    __| _/
#  | __ \_/ __ \  \ \/ \/ /\__  \\   __\/ __ \_  __ \   /     <   |  | \   __\\_  __ \  |/ __ \ /    \  / __ |
#  | \_\ \  ___/   \     /  / __ \|  | \  ___/|  | \/  |  Y Y  \___  |  |  |   |  | \/  \  ___/|   |  \/ /_/ |
#  |___  /\___  >   \/\_/  (____  /__|  \___  >__| /\  |__|_|  / ____|  |__|   |__|  |__|\___  >___|  /\____ |
#      \/     \/                \/          \/     )/        \/\/                            \/     \/      \/
# https://www.youtube.com/watch?v=V4A37PDduls

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


def expect(walls, actual, expected):
    if (actual != expected):
        print(f"rainGorithm fails for wall config: {walls}, expected {expected}, calculated {actual}")

if __name__ == '__main__':
    # simple zeros & 1s:
    expect([], collectRain([]), 0)
    expect([0], collectRain([0]), 0)
    expect([1], collectRain([1]), 0)
    expect([9991], collectRain([9991]), 0)

    # simple 2s:
    expect([0, 1], collectRain([0, 1]), 0)
    expect([1, 0], collectRain([1, 0]), 0)
    expect([1, 1], collectRain([1, 1]), 1)
    expect([0, 0], collectRain([0, 0]), 0)

    # the rest:
    wall_expectations = [
        ([0, 0, 0], 0),
        ([1, 0, 0], 0),
        ([0, 1, 0], 0),
        ([0, 0, 1], 0),
        ([1, 1, 0], 1),
        ([1, 0, 1], 2),
        ([0, 1, 1], 1),
        ([1, 1, 1], 2),
        ([100, 1, 1], 2),
        ([1, 100, 1], 2),
        ([1, 1, 100], 2),
        ([3, 1, 100], 6),
        ([3, 10, 0], 3),
        ([4, 10, 2], 6),
        ([3, 10, 0, 8], 19),
        ([3, 0, 10, 0], 6),
        ([0, 0, 10, 8], 8),
        ([0, 10, 0, 8], 16),
        ([0, 0, 12, 0, 0], 0),
        ([0, 11, 12, 0, 0], 11),
        ([0, 12, 12, 0, 0], 12),
    ]
    for expectation in wall_expectations:
        expect(expectation[0].copy(), collectRain(expectation[0]), expectation[1])
