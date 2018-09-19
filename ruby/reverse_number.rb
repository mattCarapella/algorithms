# Given a 32-bit signed integer, reverse digits of an integer.
# Return 0 if out of range.

def reverse(x)
  sign = (x < 0) ? -1 : 1
  x2 = x.abs
  reversed = 0
  until x2 == 0 do
    reversed = (reversed * 10) + x2%10
    x2 = x2/10
  end
  reversed *= sign
  two_pow_31 = (2 ** 31) 
  ((reversed < two_pow_31 -1) && (reversed > two_pow_31 = (2 ** 31)*-1)) ? reversed : 0
end

puts reverse(336469)
			 