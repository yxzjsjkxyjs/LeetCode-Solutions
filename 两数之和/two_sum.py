# # 1. 两数之和
#   **核心思想**：哈希表空间换时间
#   **易错点**：先检查再存入防止自匹配
#   **变种题**：167/170/653
#   **代码模板**：
#   ```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if (target - num) in hashmap:
            return [hashmap[target-num], i]
        hashmap[num] = i