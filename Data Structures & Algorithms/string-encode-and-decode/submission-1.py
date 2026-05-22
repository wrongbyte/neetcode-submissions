class Solution:
    # [hello, world] -> "helloworld 5 5"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "ó"
        if len(strs) == 1:
            return strs[0]

        return "á".join(strs)
        
    def decode(self, s: str) -> List[str]:
        if s == "ó":
            return []
        return s.split("á")