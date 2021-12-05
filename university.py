n = int(input())
m = int(input())

applicants = [input().split() for _ in range(n)]
sorted_apps = sorted(applicants, reverse=True, key=lambda x: x[2])

print("Successful applicants:")
for i in range(m):
    print(f"{sorted_apps[i][0]} {sorted_apps[i][1]}")
