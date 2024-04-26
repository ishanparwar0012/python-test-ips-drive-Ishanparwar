def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 

    char_set = set()
    
    left = 0
    
    max_length = 0
    
    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)
    print(max_length)
    return max_length

pass

