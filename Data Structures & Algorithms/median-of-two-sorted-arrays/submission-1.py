class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        half = total_len // 2
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) -1
        while True:
            i = (l+r) // 2
            j = half - i - 2
            
            al = A[i] if i>= 0 else - float("infinity")
            ar = A[i + 1] if i+1 < len(A) else float("infinity")
            bl = B[j] if j >= 0 else - float("infinity")
            br = B[j+1] if j+1 < len(B) else float("infinity")
            
            if al <= br and bl <= ar:
                if total_len % 2:
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                r = i -1
            else:
                l = i + 1
