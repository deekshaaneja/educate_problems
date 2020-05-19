# Python3 program to find the longest palindrome by removing 
# or shuffling characters from the given strring 

# Function to find the longest palindrome by removing 
# or shuffling characters from the given strring 
def findLongestPalindrome(strr): 
	
	# to stores freq of characters in a strring 
	count = [0]*256

	# find freq of characters in the input strring 
	for i in range(len(strr)): 
		count[ord(strr[i])] += 1

	# Any palindromic consists of three parts 
	# beg + mid + end 
	beg = "" 
	mid = "" 
	end = "" 

	# solution assumes only lowercase characters are 
	# present in strring. We can easily extend this 
	# to consider any set of characters 
	ch = ord('a') 
	while ch <= ord('z'): 
		
		# if the current character freq is odd 
		if (count[ch] & 1): 
			
			# mid will contain only 1 character. It 
			# will be overridden with next character 
			# with odd freq 
			mid = ch 

			# decrement the character freq to make 
			# it even and consider current character 
			# again 
			count[ch] -= 1
			ch -= 1

		# if the current character freq is even 
		else: 
		
			# If count is n(an even number), push 
			# n/2 characters to beg and rest 
			# n/2 characters will form part of end 
			# strring 
			for i in range(count[ch]//2): 
				beg += chr(ch) 
		ch += 1

	# end will be reverse of beg 
	end = beg 

	end = end[::-1] 

	# return palindrome strring 
	return beg + chr(mid) + end 


  
s = "adskassda"
print(findLongestPalindrome(s))
