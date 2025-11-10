# https://leetcode.com/problems/word-ladder/description/
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if endWord == beginWord:
            return 1
        word_set = set(wordList)
        visited = set([beginWord])
        queue = deque([beginWord])
        distance = 0 
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return distance + 1
                for i in range(len(curr_word)):
                    for c in alphabets:
                        next_word = curr_word[:i] + c + curr_word[i+1:]
                        if next_word not in visited and next_word in word_set:
                            queue.append(next_word)
                            visited.add(next_word)
            distance += 1
        return 0
