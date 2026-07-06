class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        isprime = [True] * n
        isprime[0] = isprime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if isprime[i]:
                for j in range(i * i, n, i):
                    isprime[j] = False

        count = 0
        for val in isprime:
            if val:
                count += 1

        return count        
                