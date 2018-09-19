# Given a string s and a non-empty string p, find all the start indices of p‘s anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will 
# not be larger than 20,100.
# The order of output does not matter.

class Anagram
  def initialize(word)
    @word = word
  end

  def display
    @word.chars.to_a.permutation.map(&:join).uniq.each do |i|
      puts i
    end
  end
end

anagram = Anagram.new('ant')
anagram.display