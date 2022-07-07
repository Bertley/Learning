'''
Non-critical requests for a transaction system are routed through a throttling gateway to ensure that the
network is not choked by non-essential requests.

The gateway has the following limits:
- The number of transactions in any given second cannot exceed 3.
- The number of transactions in any given 10 second period cannot exceed 20. A ten-second period
includes all requests arriving from any time max(1, T-9) to T (inclusive of both) for any valid time T.
- The number of transactions in any given minute cannot exceed 60. Similar to above, 1 minute is from
max(1, T-59) to T.

Any request that exceeds any of the above limits will be dropped by the gateway. Given the times at which
different requests arrive sorted ascending, find how many requests will be dropped.

Note: Even if a request is dropped it is still considered for future calculations. Although, if a request is to be
dropped due to multiple violations, it is still counted only once.

Example
n = 27
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11 ]

'''
import re


def solution(requestTime):
    '''
    The number of transactions in any given second cannot exceed 3.
    max(1, T9) to T: The number of transactions in anu given 10 seconds cannot exceed 20.
    max(1, 59) to T: The number of transactions in any given minute cannot exceed 60
    '''

    one_sec = []
    ten_sec = []
    sixty_sec = []

    output = 0

    for i in range(len(requestTime)):
        # remove all elements that roll of time window
        req = requestTime[i]

        while one_sec and req - one_sec[0] >= 1:
            one_sec.pop(0)
        while ten_sec and req - ten_sec[0] >= 10:
            ten_sec.pop(0)
        while sixty_sec and req - sixty_sec[0] >= 60:
            sixty_sec.pop(0)

        # add the new request
        one_sec.append(req)
        ten_sec.append(req)
        sixty_sec.append(req)

        # do the tests, only add a packet once, even if it qualifies
        if len(one_sec) > 3 or len(ten_sec) > 20 or len(sixty_sec) > 60:
            output += 1

    return output


print(solution([1, 1, 1, 1, 2, 2, 2, 3, 3,
      3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]))
print(solution([1, 1, 1, 1, 2]))
