
def threeSum(nums):
    #Your Code Here
    my_sum = None
    solution_set = set()
    result = []
    if len(nums) > 2:
        for ind1 in range(len(nums)):
            for ind2 in range(1, len(nums)):
                for ind3 in range(2, len(nums)):
                    if int(nums[ind1]) + int(nums[ind2]) + int(nums[ind3]) == 0:
                        solution_set.add((ind1, ind2, ind3))
        for item in solution_set:
            result.append((nums[item[0]], nums[item[1]], nums[item[2]]))
        return set(result)


print(threeSum(['-7', '0', '0', '7']))
