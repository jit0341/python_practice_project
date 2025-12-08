def make_call_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_running_total():
    total = 0
    def adder(num):
        nonlocal total
        total += num
        return total
    return adder

def make_output_cache():
    cache = []
    def cacher(value):
        nonlocal cache
        cache.append(value)
        if len(cache) > 3:
            cache.pop(0)
        return cache
    return cacher

# Example usage:
if __name__ == "__main__":
    # Call counter
    count_calls = make_call_counter()
    print(count_calls())  # 1
    print(count_calls())  # 2
    print(count_calls())  # 3

    # Running total
    running_total = make_running_total()
    print(running_total(5))   # 5
    print(running_total(10))  # 15
    print(running_total(3))   # 18

    # Output cache
    cache_outputs = make_output_cache()
    print(cache_outputs(1))  # [1]
    print(cache_outputs(2))  # [1, 2]
    print(cache_outputs(3))  # [1, 2, 3]
    print(cache_outputs(4))  # [2, 3, 4]
