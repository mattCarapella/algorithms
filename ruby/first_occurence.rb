# Return the index of the first occurrence of needle in haystack, or -1 if needle 
# is not part of haystack. Return 0 for empty strings.
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

def nihs(haystack, needle)
    return 0 if needle.empty?
    return -1 if not haystack.include?(needle)
    return haystack.index(needle)
end


haystack = "HELLO"
needle = "LL"
nihs(haystack, needle)

puts haystack.index(needle)