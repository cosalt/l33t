class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums, count = set(nums), 1
        while count in nums:
            count += 1
        return count








# slow & unoptimized
def solution(A):
    A = list(set(A))
    A.sort()
    #print(A)
    count = 1
    for i in range(len(A)):
        print(f'count: {count}')
        print(f'A[i]: {A[i]}')
        if A[i] < 1:
            continue
        
        if count != A[i]:
            return count 
        else:
            count += 1
    return count
