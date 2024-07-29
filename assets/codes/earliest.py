class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        seeds = list(zip(plantTime, growTime))
        
        seeds.sort(key=lambda x: -x[1])
        
        current_time = 0
        latest_bloom_day = 0
        
        for plant, grow in seeds:
            current_time += plant
            bloom_day = current_time + grow
            latest_bloom_day = max(latest_bloom_day, bloom_day)
        
        return latest_bloom_day

# # Exemplos de uso
# sol = Solution()
# plantTime1 = [1, 4, 3]
# growTime1 = [2, 3, 1]
# plantTime2 = [1, 2, 3, 2]
# growTime2 = [2, 1, 2, 1]
# print(sol.earliestFullBloom(plantTime1, growTime1))
# print(sol.earliestFullBloom(plantTime2, growTime2))