def solution(N):
    # Find the highest factor of N that's 26 or less
    for num_letters in range(26, 0, -1):
        if N % num_letters == 0:
            break
    
    # Calculate repetitions per letter
    repetitions = N // num_letters
    
    # Construct the string
    result = ''
    for i in range(num_letters):
        result += chr(97 + i) * repetitions  # 97 is ASCII for 'a'
    
    return result

