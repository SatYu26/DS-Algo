# python3
import sys


# def compute_min_refills(distance, miles, n, stops):
#     numRefills = currentRefill = 0
#     limit = miles

#     while limit < distance:
#         # While the destination cannot be reached with current fuel
#         if currentRefill >= n or stops[currentRefill] > limit:
#             # Cannot reach the destination nor the next gas station
#             return -1

#         while (currentRefill < n-1) and stops[currentRefill + 1] <= limit:
#             currentRefill += 1

#         numRefills += numRefills
#         limit = stops[currentRefill] + miles  # Fill up the tank
#         currentRefill += 1

#     return numRefills

def compute_min_refills(distance, tank, stops):

    numrefill, currentrefill = 0, 0
    # include the start and end points in the stops list
    stops = [0] + stops + [distance]
    if distance <= tank:
        return 0
    else:
        while currentrefill < len(stops)-1:
            lastrefill = currentrefill
            #print(currentrefill, lastrefill, len(stops))
            while currentrefill < len(stops)-1 and stops[currentrefill+1] - stops[lastrefill] <= tank:

                currentrefill += 1

            if currentrefill == lastrefill:
                return -1
            if currentrefill < len(stops)-1:
                numrefill += 1

        # print(numrefill)

        return numrefill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
