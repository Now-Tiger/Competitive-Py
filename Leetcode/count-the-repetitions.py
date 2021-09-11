# ---------------------------------- Count The Repetitions ----------------------------------

# We define str = [s, n] as the string str which consists of the string s concatenated n times.

# For example, str == ["abc", 3] =="abcabcabc".
# We define that string s1 can be obtained from string s2 if we can remove some characters 
# from s2 such that it becomes s1.

# For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing 
# the bolded underlined characters.
# You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings 
# str1 = [s1, n1] and str2 = [s2, n2].

# Return the maximum integer m such that str = [str2, m] can be obtained from str1.
 
# Example 1:

# Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# Output: 2


# Example 2:

# Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# Output: 1


class ReadStream:
	def getWordsCount(self, stream, words):
		map_char_positions = {}
		for index,char in enumerate(stream):
			if char in map_char_positions:
				map_char_positions[char].append(index)
			else:
				map_char_positions[char] = []
				map_char_positions[char].append(index)

		map_word_count = {}
		stream_length = len(stream)-1
		for word in words:
			first_char = word[0]
			if first_char in map_char_positions:
				positions   = map_char_positions[first_char]
				length_word = len(word)
				count=0
				for position in positions:
					if stream[position:position+length_word] == word and position+length_word-1<=stream_length:
						count+=1
				map_word_count[word]=count
			else:
				map_word_count[word] = 0
		return map_word_count


if __name__ == '__main__' :
    stream = ReadStream()   
    print(stream.getWordsCount("acacabcatghhellomvnsdb", ["aca","cat","hello","world"]))

# $ python count-the-repetitions.py 
# {'aca': 2, 'cat': 1, 'hello': 1, 'world': 0} 



# ---------------------------------- Leetcode python3 solution ----------------------------------


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        for i in range(len(s2)):
            start = i
            cnt = 0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start += 1
                    if start == len(s2):
                        start = 0
                        cnt += 1
            dp.append((start,cnt))
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2


