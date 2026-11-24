class Solution:
    def maxLength(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_len = 0
        n = len(nums)

        for start in range(n):
            product = 1
            current_gcd = 0
            current_lcm = 1

            for end in range(start, n):
                value = nums[end]

                product *= value

                if current_gcd == 0:
                    current_gcd = value
                else:
                    current_gcd = gcd(current_gcd, value)

                current_lcm = current_lcm * value // gcd(current_lcm, value)

                if product == current_gcd * current_lcm:
                    max_len = max(max_len, end - start + 1)

        return max_len