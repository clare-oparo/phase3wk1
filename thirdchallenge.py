def solution(N):
    # Maximum number of unique letters I can use
    max_unique_letters = 26
    
    # Determine how many times each letter should be repeated
    # and how many unique letters to use
    for num_letters in range(max_unique_letters, 0, -1):
        if N % num_letters == 0:
            repeat_count = N // num_letters
            break
    
    # Construct the string
    result = []
    for i in range(num_letters):
        letter = chr(ord('a') + i)  # Get the ith letter
        result.append(letter * repeat_count)
    
    return ''.join(result)


