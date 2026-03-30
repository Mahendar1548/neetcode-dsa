class TimeMap:

    def __init__(self):
        self.key_wise_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_wise_values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        data = self.key_wise_values[key]
        print(data, timestamp)
        low = 0
        high = len(data)
        
        ans = -1
        while low < high:
            mid = (low + high) // 2
            if data[mid][0] <= timestamp:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
            
        return data[ans][1] if ans != -1 else ""
