"""
https://leetcode.com/problems/count-and-say/description/?envType=problem-list-v2&envId=string&favoriteSlug=&difficulty=MEDIUM"""


def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
    return s
