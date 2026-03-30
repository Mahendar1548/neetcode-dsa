class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for value in asteroids:
            while len(stack) > 0:
                if stack[-1] > 0 and value < 0:
                    if stack[-1] < abs(value):
                        stack.pop()
                    elif stack[-1] == abs(value):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(value)
                    break
            else:
                stack.append(value)
        
        return stack