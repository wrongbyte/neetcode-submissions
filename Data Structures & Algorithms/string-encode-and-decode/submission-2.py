class Solution:
    # "helloworld 5 5 10"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"

        letters_count = 0
        word_lens = []

        for word in strs:
            word_len = len(word)
            print(f"word len is {word_len}")
            word_lens.append(word_len)
            letters_count += word_len

        concatenated = "".join(strs)
        for l in word_lens:
            concatenated += f" {l}"
        concatenated += f" {letters_count}"
        print(f"concatenated is {concatenated}")
        return concatenated

    def decode(self, s: str) -> List[str]:
        # kind of workaround
        if s == "empty":
            return []

        # split on last ocurrence of whitespace. this will be the number containing
        # how many letters the concatenated words have
        rest, letters_count = s.rsplit(" ", 1)
        letters_count = int(letters_count)

        # s[:0] returns an empty string so we cannot use it
        letters = s[:letters_count] if letters_count > 0 else s

        # get everything after the concatenated letters, excluding the first 
        # whitespace
        word_lens = s[letters_count + 1:] 
        word_lens = word_lens.split(" ")
        word_lens.pop() # the last el is the len of all letters

        print(f"letters {letters} word_lens {word_lens}")

        words = []

        for word_len in word_lens:
            print(f"word len {word_len}")
            word_len = int(word_len)
            # if it is an empty char, we add the emtpy char to the words list
            # and do not split the string
            if word_len == 0:
                words.append("")
            else:
                word = letters[:word_len]
                words.append(word)
                letters = letters[word_len:]
    
        print(f"words is {words}")
        return words

