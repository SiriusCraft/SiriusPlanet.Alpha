"""
does not pass leet code test actually
"123  345" not pass but works locally
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_neg = False
        num = 0
        list_str = list(str)
        base_num = ord('1')
        number_set = {'0','1','2','3','4','5','6','7','8','9'}
        space_set = {' '}
        operator_set = {'+','-'}
        for i in range(len(list_str)):
            if list_str[i] == ' ':
                pass
            if list_str[i] in operator_set and i+1<len(list_str) and list_str[i+1] in number_set.union(space_set):
                if list_str[i] == '-':
                    is_neg = True
                else:
                    is_neg = False
            if list_str[i] in operator_set and i + 2 < len(list_str) and list_str[i + 2] in number_set.union(space_set) and list_str[i+1] in operator_set:
                if list_str[i] != list_str[i+1]:
                    num = 0
                    break
            if list_str[i] in number_set:
                if num >0:
                    num = num*10+ord(list_str[i])-base_num +1
                else:
                    num = ord(list_str[i])-base_num +1
            if list_str[i] in number_set and i+1 < len(list_str) and not (list_str[i+1] in number_set.union(space_set)):
                break
            if list_str[i] =='0' and i+1 <len(list_str) and list_str[i+1] == ' ':
                break
        if num > 2147483647 and not is_neg:
            num = 2147483647
        if num >2147483648 and is_neg:
            num = 2147483648
        if is_neg and num > 0:
            num = -num
        print(num)
        return num

if __name__ == '__main__':
    s =Solution()
    s.myAtoi("123 234")