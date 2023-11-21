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
    if walls == None or len(walls) < 2:
        return 0
    # reduce, if necessary, to a maximum that occurs at least 2 times.
    total_water_collected = 0
    while max(walls) > 0:
        max_result = twoMaxesOrMaxIndex(walls)
        if isinstance(max_result, dict):
            # a distinct L max and R max
            # the higher max must be reduced because no water will be collected in the area of the difference between the 2
            if max_result['right_max'] > max_result['left_max']:
                walls[max_result['i_right_max']] = max_result['left_max']
            elif max_result['right_max'] < max_result['left_max']:
                walls[max_result['i_left_max']] = max_result['right_max']
            # regardless of whatever else we discover about walls,
            # we know that there are no higher walls between these 2 maxes.
            # we can confidently set to zero all walls in between them.
            for iz in range(max_result['i_left_max']+1, max_result['i_right_max']):
                walls[iz] = 0
            # a pool will collect between these 2 maxes. the width of which is:
            pool_width = max_result['i_right_max'] - max_result['i_left_max']
            # the total depth would be the value of these maxes, but we should calc only to the height of the next max
            # which we would know if we max() the walls with these 2 maxes removed.
            latest_max = walls[max_result['i_right_max']]
            walls[max_result['i_left_max']] = 0
            walls[max_result['i_right_max']] = 0
            new_max = max(walls)
            pool_layer_depth = latest_max - new_max
            water_layer_volume = pool_width * pool_layer_depth
            total_water_collected += water_layer_volume
            # reduce the 2 maxes to this new max
            walls[max_result['i_left_max']] = new_max
            walls[max_result['i_right_max']] = new_max
            # ready to find the next left & right maxes
        else:
            # one max
            # useless for collecting water
            # reduce this wall's height to the next max
            walls[max_result] = 0
            next_max = max(walls)
            walls[max_result] = next_max
            # ready to find the next left & right maxes
    return total_water_collected

def twoMaxesOrMaxIndex(walls):
    left_max = 0
    i_left_max = 0

    right_max = 0
    i_right_max = len(walls) - 1

    l = 0
    r = len(walls) - 1
    while l < r:
        if walls[l] > left_max:
            left_max = walls[l]
            i_left_max = l
        if walls[r] > right_max:
            right_max = walls[r]
            i_right_max = r
        l += 1
        r -= 1
    if l == r:
        # just happens to be odd walls.length
        # if center wall > either left_max or right_max, return this central max index
        if walls[l] > max(left_max, right_max):
            return l
        elif walls[l] > right_max:
            right_max = walls[l]
            i_right_max = l
        elif walls[l] > left_max:
            left_max = walls[l]
            i_left_max = l
    return {
        "left_max": left_max,
        "i_left_max": i_left_max,
        "right_max": right_max,
        "i_right_max": i_right_max
    }


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
