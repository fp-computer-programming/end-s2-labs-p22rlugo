# Ryan Lugo: RJl 1/25/22

def solution(nums):
    if not nums:
        return []
    return sorted(nums)

print(solution([1,2,3,10,5]) == [1,2,3,5,10])
print(solution([20,2,10]) == [2,10,20])
print(solution(None) == [])