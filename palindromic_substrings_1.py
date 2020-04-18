# Python3 program to count special 
# Palindromic substring 

# Function to count special 
# Palindromic susbstring 
def CountSpecialPalindrome(str): 
	n = len(str)

	# store count of special 
	# Palindromic substring 
	result = 0

	# it will store the count 
	# of continues same char 
	sameChar=[0] * n

	i = 0

	# traverse string character 
	# from left to right 
	while (i < n): 

		# store same character count 
		sameCharCount = 1

		j = i + 1

		# count smiler character 
		while (j < n): 
			if(str[i] != str[j]): 
				break; 
			sameCharCount += 1 
			j += 1
		
		# Case : 1 
		# so total number of substring 
		# that we can generate are : 
		# K *( K + 1 ) / 2 
		# here K is sameCharCount 
		result += int(sameCharCount *
					(sameCharCount + 1) / 2)

		# store current same char 
		# count in sameChar[] array 
		sameChar[i] = sameCharCount

		# increment i 
		i = j

	# Case 2: Count all odd length 
	# Special Palindromic substring 
	for j in range(1, n): 
		
		# if current character is equal 
		# to previous one then we assign 
		# Previous same character count 
		# to current one 
		if (str[j] == str[j - 1]): 
			sameChar[j] = sameChar[j - 1]

		# case 2: odd length 
		if (j > 0 and j < (n - 1) and
		(str[j - 1] == str[j + 1] and
			str[j] != str[j - 1])): 
			result += (sameChar[j - 1] 
					if(sameChar[j - 1] < sameChar[j + 1]) 
					else sameChar[j + 1])

	# subtract all single 
	# length substring 
	return result-n

# Driver Code 
str = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
print(CountSpecialPalindrome(str))
print(CountSpecialPalindrome("aabbaa"))


# This code is contributed by mits. 
