n = 3
mean_val = sum([int(input()) for _ in range(n)]) / n
print(mean_val)
if mean_val >= 60.0:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
