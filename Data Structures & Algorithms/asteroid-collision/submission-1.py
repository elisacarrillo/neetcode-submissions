class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        # q.append(asteroids[0])
        for a in asteroids:
            alive = True
            while alive and q and a < 0 and q[-1] > 0:
                
                print(f'prev: {q[-1]}, curr: {a}')
                if (-1 * a > q[-1]):
                    q.pop()
                    continue
                elif (-1 * a == q[-1]):
                    q.pop()
                
                alive = False

            if (alive):
                q.append(a)

                
        return q
            
        