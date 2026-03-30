class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        num_wise_count = Counter(hand)

        for num in hand:
            if not num_wise_count[num]:
                continue
            start = num
            while start - 1 in num_wise_count and num_wise_count[start-1]:
                start -= 1

            while start <= num:
                for i in range(start, start+groupSize):
                    if i not in num_wise_count or not num_wise_count[i]:
                        return False
                    num_wise_count[i] -= 1
                while start in num_wise_count and not num_wise_count[start]:
                    start += 1

        return True
