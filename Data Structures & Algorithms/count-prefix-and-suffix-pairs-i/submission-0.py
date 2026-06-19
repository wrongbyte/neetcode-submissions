class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
            prefix = str2[:len(str1)]
            suffix = str2[-len(str1):]
            # print(f"prefix of {str2} is {prefix}, suffix is {suffix}")
            if prefix == str1 and suffix == str1:
                return True
            return False

        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                # print(f"checking {word} and {words[j]}")
                if isPrefixAndSuffix(word, words[j]):
                    # print(f"{word} is prefix and suffix of {words[j]}")
                    count += 1


        return count