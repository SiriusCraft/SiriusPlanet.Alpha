def solution(nums):
    if not nums:
        return False
    path = [-1 for _ in nums]
    last_index = -1
    max_reach = 0
    for i in range(len(nums)):
        if max_reach < i:
            return False
        if i + nums[i] > max_reach:
            last_index = i
            max_reach = i + nums[i]
            if max_reach >= len(nums) - 1:
                path[-1] = i
                return getPath([], path, len(path) - 1)
            else:
                path[max_reach] = i
        else:
            path[i] = last_index

def getPath(res, path, index):
    res.append(index)
    while index != 0:
        index = path[index]
        res.append(index)
    res.reverse()
    return res

def main():
    nums = []
    data = input()
    while data:
        try:
            nums.append(int(data))
        except ValueError:
            print("failure\n")
        data = input()
    res = solution(nums)
    if not res:
        print("failure\n")
    res.append("out")
    print(res)

main()