
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = list(word)

        l = 0
        r = word.find(ch)

        if r== -1:
            return word

        while l< r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1

        return "".join(s)
