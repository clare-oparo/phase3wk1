def digit_sum(n):
    # Calculate the sum of digits of a number
    return sum(int(digit) for digit in str(n))

def solution(A):
    # Group numbers by their digit sum
    groups = {}
    for number in A:
        sum_of_digits = digit_sum(number)
        if sum_of_digits not in groups:
            groups[sum_of_digits] = []
        groups[sum_of_digits].append(number)
    
    # Find the overall maximum sum among all groups
    max_sum = -1
    for group in groups.values():
        if len(group) >= 2:
            group.sort(reverse=True)
            # Calculate the maximum sum for this group.
            group_max_sum = group[0] + group[1]
            max_sum = max(max_sum, group_max_sum)
    
    # Return the result
    return max_sum

