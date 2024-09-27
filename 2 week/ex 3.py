def is_regular_palindrome(s):
    return s == s[::-1]
def is_mirrored_string(s):
    mirrored_chars = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M',
        'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1',
        '8': '8', 'E': '3', 'J': 'L', 'S': '2',
        'Z': '5', '3': 'E', 'L': 'J', '2': 'S',
        '5': 'Z'
    }  
    mirrored = []    
    for char in s:
        if char not in mirrored_chars:
            return False
        mirrored.append(mirrored_chars[char])   
    return ''.join(mirrored) == s[::-1]
def check_string(s):
    regular_palindrome = is_regular_palindrome(s)
    mirrored_string = is_mirrored_string(s)
    if regular_palindrome and mirrored_string:
        return f"{s} is a mirrored palindrome."
    elif mirrored_string:
        return f"{s} is a mirrored string."
    elif regular_palindrome:
        return f"{s} is a regular palindrome."
    else:
        return f"{s} is not a palindrome."
print(check_string(input()))
