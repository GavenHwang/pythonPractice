# -*- coding:utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            j = 0
            for i in range(len(nums)):
                if nums[i] != nums[j]:
                    j += 1
                    nums[j] = nums[i]
        print(nums)
        return j+1

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        new_price = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        print(new_price)
        return sum([x if x > 0 else 0 for x in new_price])


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))