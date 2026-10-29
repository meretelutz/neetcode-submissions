class Solution:

    def encode(self, strs: List[str]) -> str:
        secret = ""
        for s in strs:
            secret = secret + str(len(s)) + '#' + s
        return secret

    def decode(self, s: str) -> List[str]:
        secrets = []

        while len(s) > 0:
            marker = s.index('#')
            set_len = int(s[:marker])
            secrets.append(s[marker+1:marker+1+set_len])
            s = s[marker+1+set_len:]

        return secrets