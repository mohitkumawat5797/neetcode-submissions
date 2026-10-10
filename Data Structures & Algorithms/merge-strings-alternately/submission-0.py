class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newstr = ""

        for i in range(len(word1)):
            newstr = newstr + word1[i]

            if i < len(word2):
                newstr = newstr + word2[i]

        if len(word2) > len(word1):
            newstr = newstr + word2[len(word1):]

        return newstr