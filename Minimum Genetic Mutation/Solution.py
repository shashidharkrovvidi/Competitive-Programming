#https://leetcode.com/problems/minimum-genetic-mutation/description/
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank_set = set(bank)
        visited = set(startGene)
        queue = deque([startGene])
        mutations = 0
        alphabets = "ACGT"
        while queue:
            for _ in range(len(queue)):
                curr_string = queue.popleft()
                if curr_string == endGene:
                    return mutations
                for i in range(len(curr_string)):
                    for c in alphabets:
                        next_word = curr_string[:i] + c + curr_string[i+1:]
                        if next_word not in visited and next_word in bank_set:
                            queue.append(next_word)
                            visited.add(next_word)
            mutations += 1
        return -1
        