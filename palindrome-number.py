class Solution(object):
    def isPalindrome(self, x):
        x_string = str(x)
        x_string_reverse = x_string[::-1]
        return x_string == x_string_reverse


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(5))
    print(s.isPalindrome(1234554321))
    print(s.isPalindrome(123454321))
