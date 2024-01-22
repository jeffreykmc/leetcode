#70. Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/?source=submission-noac


#fail as Time Limit Exceed
class Solution:
    def climbStairs(self, n: int) -> int:
        #https://realpython.com/fibonacci-sequence-python/
        def fib(n):
            if n in {0,1}:
                return n

            return fib(n-1)+fib(n-2)
        return fib(n)
        

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables for Fibonacci sequence.
        #https://leetcode.com/problems/climbing-stairs/solutions/4584785/beats-100-3-approaches-explained-java-c-python-rust-javascript
        a=0
        b=1
        ways=0

        # Iterate to calculate ways using Fibonacci logic.
        for i in range(1, n + 1):
            ways = a + b  # Calculate current ways.
            a, b = b, ways  # Update a and b.
            print(i,a,b,ways)

        # Return total ways to climb the stairs.
        return ways

class Solution:
    def climbStairs(self, n: int) -> int:
        
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
        