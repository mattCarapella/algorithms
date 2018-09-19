# Find whether a string contains unique items. The string contains only lower case letters.

def uniq_chars?(str)
  str.downcase
  a = ("a".."z").all? {|c| str.count(c) <= 1}
end

puts uniq_chars?("abcde")

