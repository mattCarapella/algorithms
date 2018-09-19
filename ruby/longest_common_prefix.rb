# Find the longest common prefix in a set of strings

def longest_common_prefix(strs)
	return '' if strs.empty?
	min, max = strs.minmax
	idx = min.size.times{ |i| break i if min[i] != max[i] }
	min[0...idx]
end

words = ["AAABC", "AAAC", "AAABF", "AAA"]
puts longest_common_prefix(words)