class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestcommonprefix = ""
        if len(strs) > 1:
            longestcommonprefix = self.longestCommonPrefixInTwoStrings(strs[0], strs[1])
            for i in range(1, len(strs) - 1):
                longestcommonprefix = self.longestCommonPrefixInTwoStrings(longestcommonprefix, strs[i + 1])
                if longestcommonprefix == "":
                    break
        elif len(strs) == 1:
            longestcommonprefix = strs[0]
        return longestcommonprefix

    def longestCommonPrefixInTwoStrings(self, string1, string2):
        smallerstring = ""
        largerstring = ""
        if string1 >= string2:
            largerstring = string1
            smallerstring = string2
        else:
            smallerstring = string1
            largerstring = string2
        for i in range(len(smallerstring)):
            if smallerstring[i] != largerstring[i]:
                return smallerstring[:i]
            else:
                continue
        return smallerstring

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
