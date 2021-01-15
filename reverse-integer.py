class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = abs(x)
        reversed_num = 0
        while num > 0:
            digit = num % 10
            reversed_num = (reversed_num * 10) + digit
            num = num // 10
        if x < 0:
            reversed_num = reversed_num * -1
        if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 - 1:
            reversed_num = 0
        return reversed_num


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1234))
