# Given a sorted numsay and a target value, return the index if the target is 
# found. If not, return the index where it would be if it were inserted in 
# order. You may assume no duplicates in the numsay.

def search_insert(nums, target)
  return -1 if nums.nil?
  from = 0
  to = nums.size-1
  while from <= to 
    mid = (from + to)/2 
    if nums[mid] == target then return mid
    elsif target < nums[mid] then to = mid - 1
    else from = mid + 1
    end
  end
  return from
end

def search_insert_recursive(nums, target, from=0, to=nil)
  to = nums.size-1 if to.nil?
  return from if from > to 
  mid = (from + to)/2
  if nums[mid] < target then search_insert_recursive nums, target, mid+1, to
  elsif nums[mid] > target then search_insert_recursive nums, target, 0, to-1
  else mid
  end
end

nums = [0,1,2,4,6,9,12,14,16,17,19,24]
puts search_insert_recursive(nums, 4)


