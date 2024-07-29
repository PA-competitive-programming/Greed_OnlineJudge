class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        max_sum = 0
        current_sum = 0
        for s in satisfaction:
            current_sum += s
            if current_sum > 0:
                max_sum += current_sum
            else:
                break
        return max_sum
        
# # Exemplos de uso
# sol = Solution()
# print(sol.maxSatisfaction([-1, -8, 0, 5, -9]))
# print(sol.maxSatisfaction([4, 3, 2]))
# print(sol.maxSatisfaction([-1, -4, -5]))