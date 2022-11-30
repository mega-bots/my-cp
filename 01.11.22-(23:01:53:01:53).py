def solve(ind,summ,maxsum,nums):
    if ind<0:
        return maxsum
    if summ<0:
        return solve(ind-1,nums[ind],max(nums[ind],maxsum),nums)
    else:
        return solve(ind-1,summ+nums[ind],max(maxsum,summ+nums[ind]),nums)
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
print(solve(n-2,nums[-1],nums[-1],nums))
