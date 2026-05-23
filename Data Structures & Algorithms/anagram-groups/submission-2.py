class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # thinking list of dictionaries (letter counts)
        # check length of this list, then go through list that is given
        # if we exceed the length of our new list, make a new entry
        anagrams = [[]]
        dictList = []
        for i, word in enumerate(strs):
            if i == 0:
                anagrams[0].append(strs[0])
                dictList.append(dict())
                for letter in word:
                    if letter in dictList[i].keys():
                        dictList[i][letter] = dictList[i][letter] + 1
                    else:
                        dictList[i][letter] = 1
            else:
                success = False
                temp_dict = dict()
                for letter in word:
                    if letter in temp_dict.keys():
                        temp_dict[letter] = temp_dict[letter] + 1
                    else:
                        temp_dict[letter] = 1
                for j in range(len(anagrams)):
                    if temp_dict == dictList[j]:
                        anagrams[j].append(strs[i])
                        success = True
                        break
                if not success:
                    dictList.append(temp_dict)
                    anagrams.append([word])
                        
        return anagrams

                            
                            
                    
