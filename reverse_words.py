def reverse_words(s):
    # Reverse the entire string first
    s.reverse()
    
    # Reverse each word individually
    start = 0
    for i in range(len(s)):
        if s[i] == ' ':
            s[start:i] = reversed(s[start:i])
            start = i + 1
    
    # Reverse the last word (if there's only one word, this will reverse it)
    s[start:] = reversed(s[start:])
