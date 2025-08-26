'''Программа ищет все возможные варианты пар, где сумма равна какому-либо числу'''
def find_pairs(nums, target_sum):
    left_index = 0
    right_index = len(nums) - 1
    pairs = []
    while left_index < right_index:
        current_sum = nums[left_index] + nums[right_index]
        if current_sum == target_sum:
            pairs.append((nums[left_index], nums[right_index]))
            left_index += 1
            right_index -= 1
        elif current_sum < target_sum:
            left_index += 1
        else:
            right_index -= 1
    return pairs