#Code solution for Huawei
from icecream import ic


class Solution:
    def dailyTemperatures(self, temperatures) :
        L = len(temperatures)
        i, j = 0, 0
        result = [0] * L
        # O(n^2)
        while i < L:
            a = temperatures[i]
            j = i + 1
            while j < L:
                b = temperatures[j]
                if a < b:
                    result[i] = j - i
                    break
                j += 1
            i += 1

        return result

    def run(self, temperatures):
        L = len(temperatures)
        result = [0] * L
        lstack = []
        rstack = []
        for val in temperatures:
            lstack.append(val)

        while len(lstack) > 0:
            rstack.append(lstack.pop())
        # O(n^2)
        for i in range(L):
            val = rstack.pop() # get the first element
            lstack.append(val)

            while len(rstack) > 0:
                temp = rstack.pop()
                lstack.append(temp)
                if temp <= val:
                    pass
                else:
                    result[i] = len(lstack) - 1
                    while len(lstack) > 0:
                        rstack.append(lstack.pop())
                    break

            if len(lstack) != 0:
                while len(lstack) > 0:
                    rstack.append(lstack.pop())
            rstack.pop() # pop the last element

        return result




if __name__ == '__main__':
    solution = Solution()
    ic(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    ic(solution.run([73, 74, 75, 71, 69, 72, 76, 73]))