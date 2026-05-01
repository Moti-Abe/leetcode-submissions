class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.arr:
            # check overlap
            if startTime < e and endTime > s:
                return False
        
        self.arr.append((startTime, endTime))
        return True