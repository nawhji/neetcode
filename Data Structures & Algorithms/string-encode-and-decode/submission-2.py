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
            start_idx = s.find("#", ptr) + 1
            length = int(s[ptr:start_idx-1])
            decoded.append(s[start_idx:start_idx+length])
            ptr = start_idx + length
        return decoded