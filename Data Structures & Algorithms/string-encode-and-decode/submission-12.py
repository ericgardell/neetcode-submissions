class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            code += (f"{len(string)}#{string}")
        return code

    def decode(self, s: str) -> List[str]:
        char = 0
        numString = ""
        strs = []
        print(s)
        while char < len(s):
            print(char, s[char])
            if s[char] != "#":
                numString += s[char]
                char += 1
            else:
                numChars = int(numString)
                string = s[char +1 : char + numChars+1]
                print(string, "appended")
                strs.append(string)
                numString = ""
                char += numChars + 1
        return strs