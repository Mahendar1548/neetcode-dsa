class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp_list = sorted(zip(position, speed), reverse=True)
        mon_stack = []
        for pos, sp in pos_sp_list:
            time_to_reach = (target - pos) / sp
            if not mon_stack or mon_stack[-1] < time_to_reach:
                mon_stack.append(time_to_reach)
        
        return len(mon_stack)
