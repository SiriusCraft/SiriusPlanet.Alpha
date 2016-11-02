"""
Fast Inverse Square Root
Newton's method
http://blog.csdn.net/dawnbreak/article/details/3308413
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x
        while t*t > x:
            t = int(t/2.0 +x/(2.0*t))
        return t

if __name__ == '__main__':
    s = Solution()
    ans = s.mySqrt(2147395600)
    print(ans)