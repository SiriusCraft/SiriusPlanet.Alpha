# Enter your code here. Read input from STDIN. Print output to STDOUT
# [5, 6, 0, 4, 2, 4, 1, 0, 0, 4]
# [0, 5, 9, out]

import sys

class Dragon():

    def solution(self):
        """

        :return:
        """
        nums = sys.stdin.read()
        if not nums:
            return False
        path = [-1 for _ in nums]
        path[0] = 0
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
                if max_reach >= len(nums) - 1:
                    path[-1] = i
                    # print(path)
                    return self.getPath([], path, len(path) - 1)
                else:
                    path[max_reach] = i

    def getPath(self,res, path, index):
        """
        This method gets the path for hero across the canyon
        :param res:
        :param path:
        :param index:
        :return:
        """
        res.append(index)
        while index != 0:
            index = path[index]
            res.append(index)
        res.reverse()
        res.append('out')
        sys.stdout.write(res)
        return res


if __name__ == '__main__':
    nums = [5, 6, 0, 4, 2, 4, 1, 0, 0, 4]
    d = Dragon()
    # print(d.solution(nums))
    print (d.solution())