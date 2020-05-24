import math

def triplet_sum_close_to_target(arr, target):
    for i in range(len(arr)):
        target_sum = target - arr[i]


def find_pair(arr, target):
    for i in range(len(arr)):
        target_num = target - arr[i]
        if target_num in arr:
            return target, target_num