from sys import stdin
from sys import stdout


def solution(nums):
    """
    This method solves the problem of getting through canyon
    """
    if not nums:
        return False
    path = [-1 for _ in nums]
    last_index = 0
    max_reach = 0
    for i in range(len(nums)):
        if max_reach < i:
            return False
        if i + nums[i] > max_reach:
            max_reach = i + nums[i]
            for j in range(last_index, min(len(nums), max_reach + 1)):
                path[j] = i
            if max_reach >= len(nums) - 1:
                return getPath([], path, len(path) - 1)
            last_index = max_reach + 1


def getPath(res, path, index):
    """
    This method gets hero's path
    """
    res.append(index)
    while index != 0:
        index = path[index]
        res.append(index)
    res.reverse()
    return res


def main():
    """
    This main method input data and output results
    """
    nums = []
    for line in stdin:
        nums.append(int(line))
    res = solution(nums)
    if not res:
        stdout.write("failure\n")
    res_out = ""
    for i in range(len(res)):
        res_out += str(res[i]) + ', '
    res_out += 'out'
    stdout.write(res_out)


main()
