class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_mapping = {'(': ')', '[': ']', '{': '}'}
        isvalid = True
        for bracket in s:
            if bracket in bracket_mapping.keys():
                stack.append(bracket)
            else:
                if not stack:
                    isvalid = False
                    break
                last_bracket_in_stack = stack.pop()
                if bracket_mapping[last_bracket_in_stack] == bracket:
                    continue
                else:
                    isvalid = False
                    break
        return len(stack) == 0 and isvalid


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(]"))

    # "()"
    # "()[]{}"
    # "(]"
    # "([)]"
    # "{[]}"
    #
    # true
    # true
    # true
    # false
    # true
