# Given an array nums and a value val, remove all instances of that value in-place 
# and return the new length. Do not allocate extra space for another array, you 
# must do this by modifying the input array in-place with O(1) extra memory. The 
# order of elements can be changed. It doesn't matter what you leave beyond the 
# new length.

def remove_element(nums, val)
   nums.delete(val) 
   nums.compact!
end

def remove_element2(nums, val)
  return nums.size if nums.size <= 1
  done = false
  i=0 
  while not done do
    if nums[i] == val then nums.delete_at(i)
    else i+=1 
    end
    done = true if i == nums.size      
  end
  i
end

nums = [1,2,3,4,3,1,6,3,5]
puts remove_element2(nums, 3)