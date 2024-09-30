"""
https://leetcode.com/problems/mini-parser/description/?envType=problem-list-v2&envId=string&favoriteSlug=&difficulty=MEDIUM
"""


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        num, sign = None, 1  # assuming sign is positive

        for char in s:
            if char == '[':
                # start of a nested integer
                stack.append(NestedInteger())
            elif char == ']':
                # end of a nested integer
                if num is not None:
                    stack[-1].add(NestedInteger(num * sign))
                    num = None
                    sign = 1
                if stack:
                    # sort out hierarchy in stack
                    nested = stack.pop()
                    if stack:
                        stack[-1].add(nested)
                    else:
                        # base case, return stack content
                        return nested
            elif char == ',':
                # next element in list (can append current integer)
                if num is not None:
                    stack[-1].add(NestedInteger(num * sign))
                    num = None  # restart
                    sign = 1
            elif char == '-':
                sign = -1
            else:
                if num is not None:
                    num = num * 10 + int(char)
                else:
                    num = int(char)
        if num is not None:
            return NestedInteger(num * sign)
        return None
