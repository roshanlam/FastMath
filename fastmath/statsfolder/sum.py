def sum(nums):
    current_sum = 0
    error_comp = 0
    corrected_current_v = 0
    next_sum = 0

    if type(nums) in [int, float]:
        return nums
    elif type(nums) in [list, tuple]:
        for ii, _ in enumerate(nums):
            correcred_current_v = nums[ii]
            next_sum = current_sum + corrected_current_value
            error_comp = next_sum - current_sum - corrected_current_v
            current_sum = next_sum

            return round(current_sum, 3))
        else:
            raise TypeError("sum() expects a int, list or a tuple.")
