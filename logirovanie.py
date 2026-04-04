def analyze(lst):
    max_val = max(lst)
    avg = sum(lst) / len(lst)
    evens = [x for x in lst if x % 2 == 0]

    return max_val, avg, evens


nums = [1, 2, 3, 4, 5, 6]

m, avg, evens = analyze(nums)

print("Максимум:", m)
print("Среднее:", avg)
print("Чётные:", evens)