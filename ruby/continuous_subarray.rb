=begin

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


=end

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)

  a = b = nums[0]
  1.upto(nums.size-1) do |i| 
  	a = [a+nums[i], nums[i]].max
    b = [a, b].max
  end
  return b
end


nums = [-2,1,-3,4,-1,2,1,-5,4] 
puts max_sub_array(nums)