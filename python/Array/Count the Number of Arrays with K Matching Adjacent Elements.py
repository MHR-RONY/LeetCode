class Solution:
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7

        if k >= n:
            return 0
        if k == 0:
            return (m * pow(m-1, n-1, MOD)) % MOD

        def mod_comb(n, k):
            if k > n or k < 0:
                return 0
            if k == 0 or k == n:
                return 1

            num = 1
            den = 1
            for i in range(k):
                num = (num * (n - i)) % MOD
                den = (den * (i + 1)) % MOD

            return (num * pow(den, MOD-2, MOD)) % MOD

        ways_to_choose = mod_comb(n-1, k)
        ways_to_fill = (m * pow(m-1, n-1-k, MOD)) % MOD

        return (ways_to_choose * ways_to_fill) % MOD