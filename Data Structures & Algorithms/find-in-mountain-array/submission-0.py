class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        arr_len = mountainArr.length()
        peak = self._find_peak(mountainArr)
        first_half = self._search(target, mountainArr, 0, peak, True)
        if first_half is None:
            second_half = self._search(target, mountainArr, peak+1, arr_len-1, False)
            if second_half is None:
                return -1
            return second_half
        return first_half

    def _search(self, target: int, mountainArr: 'MountainArray', low, high, is_ascend=True) -> int:
        while low <= high:
            mid = (low + high) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                return mid
            elif mid_value < target:
                if is_ascend:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if is_ascend:
                    high = mid - 1
                else:
                    low = mid + 1


    def _find_peak(self, mountainArr: 'MountainArray') -> int:
        arr_len = mountainArr.length()
        low, high = 0, arr_len - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low += 1
            elif mid == arr_len - 1:
                high -= 1
            else:
                mid_val = mountainArr.get(mid)
                prev_val = mountainArr.get(mid-1)
                next_val = mountainArr.get(mid+1)

                if prev_val < mid_val > next_val:
                    return mid
                elif prev_val < mid_val < next_val:
                    low = mid + 1
                else:
                    high = mid - 1