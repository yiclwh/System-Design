"""
Implement a web logger, which provide two methods:

hit(timestamp), record a hit at given timestamp.
get_hit_count_in_last_5_minutes(timestamp), get hit count in last 5 minutes.
the two methods will be called with non-descending timestamp (in sec).

Example
    hit(1);
    hit(2);
    get_hit_count_in_last_5_minutes(3);
    >> 2
    hit(300);
    get_hit_count_in_last_5_minutes(300);
    >> 3
    get_hit_count_in_last_5_minutes(301);
    >> 2
"""

class WebLogger:
    
    def __init__(self):
        # do intialization if necessary
        self.timestamps = []
        self.counter = 0
    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.counter += 1
        if len(self.timestamps) > 0 and self.timestamps[-1][0] == timestamp:
            self.timestamps[-1] = (self.timestamps[-1][0], self.timestamps[-1][1] + 1)
        else:
            self.timestamps.append((timestamp, 1))
    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        while len(self.timestamps) > 0 and self.timestamps[0][0] + 300 <= timestamp:
            self.counter -= self.timestamps[0][1]
            self.timestamps.pop(0)

        return self.counter