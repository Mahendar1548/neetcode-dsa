class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        num_wise_count_c = Counter(hand)
        num_wise_count_c = dict(sorted(num_wise_count_c.items(), key=lambda x:x[0]))
        
        while num_wise_count_c:
            num_wise_count = num_wise_count_c.copy()
            print(num_wise_count)
            count = 0
            prev_key = None
            for key in num_wise_count:
                if prev_key is None:
                    prev_key = key - 1
                if key - prev_key != 1:
                    return False
                prev_key = key
                num_wise_count_c[key] -= 1
                if not num_wise_count_c[key]:
                    del num_wise_count_c[key]
                count += 1
                if count == groupSize:
                    break
            if count != groupSize:
                return False
        return True
