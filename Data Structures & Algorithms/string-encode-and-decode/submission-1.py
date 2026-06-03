class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        ptr = 0
        while ptr < len(s):
            length = s[ptr]
            i = 1
            while s[ptr+i] != "#":
                length += s[ptr+i]
                i += 1
            str_len = int(length)
            decoded.append(s[ptr+1+len(length):ptr+str_len+1+len(length)])
            ptr += str_len+1+len(length)
        return decoded