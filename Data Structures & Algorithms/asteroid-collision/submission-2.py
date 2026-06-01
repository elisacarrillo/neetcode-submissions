class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []

        for a in asteroids:
            alive = True
            while q and alive and a < 0 and q[-1] > 0:
                if (-a > q[-1]):
                    q.pop()
                    continue
                elif (-a == q[-1]):
                    q.pop()
                alive = False
            
            if (alive):
                q.append(a)
        return q