#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
#return the length of last word in the string. If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space characters only.


# @param {String} s
# @return {Integer}
def length_of_last_word(s)
  val = 0
  rev = s.reverse!
  rev.each_char { |c|
    if c == ' ' then return val if val != 0
    else val+=1
    end
  }
  val
end

s = "Hello  "
puts length_of_last_word(s)