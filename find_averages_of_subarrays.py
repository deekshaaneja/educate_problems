

def find_averages_of_subarrays(k, arr):
    result = []
    window_start, window_end = 0, 1
    window_avg = 0
    while window_end < window_start:
        
