class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        char_cnts = []

        for word in strs: # O(num of words * word len + O(num of words * word len * 나머지 word len))
            word_cnt = {}
            for c in word: 
                if word_cnt.get(c) is None:
                    word_cnt[c] = 1
                else:
                    word_cnt[c] += 1

            found = False
            for i, cd in enumerate(char_cnts):
                if len(word) != len(output[i][0]):
                    continue

                found = True

                for c in word_cnt:
                    if cd.get(c) != word_cnt[c]:
                        found = False
                        break
                if found:
                    output[i].append(word)
                    break
                continue
            if not found:
                output.append([word])
                char_cnts.append(word_cnt)
        return output