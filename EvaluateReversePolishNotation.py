"""
150. Evaluate Reverse Polish Notation
local right
but leetcode does not pass
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return None
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operaters = {'+', '-', '*', '/'}
        for tocken in tokens:
            if tocken not in operaters:
                stack.append(int(tocken))
            else:
                calculate_us = []
                calculate_ans = 0
                calculate_us.append(stack.pop())
                calculate_us.append(stack.pop())
                if tocken is '+':
                    calculate_ans = calculate_us[1] + calculate_us[0]
                if tocken is '-':
                    calculate_ans = calculate_us[1] - calculate_us[0]
                if tocken is '*':
                    calculate_ans = calculate_us[1] * calculate_us[0]
                if tocken is '/':
                    if calculate_us[1] * calculate_us[0] < 0:
                        calculate_ans = -((-calculate_us[1]) / calculate_us[0])
                    else:
                        calculate_ans = calculate_us[1] / calculate_us[0]
                stack.append(int(calculate_ans))
        return stack.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["3","-4","+"]))
