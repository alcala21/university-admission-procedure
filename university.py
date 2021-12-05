from collections import defaultdict

department_names = ['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering']
department_names.sort()
n = int(input())
fname = "applicants.txt"


class Student:
    def __init__(self, name, last, gpa, first, second, third):
        self.name = name
        self.last = last
        self.gpa = float(gpa)
        self.options = {"first": first, "second": second, "third": third}
        self.full_name = f"{self.name} {self.last}"

class Department:
    def __init__(self, name, n):
        self.name = name
        self.needed = n
        self.accepted = []

    def admit(self, candidates):
        rejected = []
        if len(candidates) <= self.needed:
            self.accepted += candidates
            self.needed -= len(candidates)
        else:
            for i in range(self.needed):
                self.accepted += [candidates[i]]
            rejected = candidates[self.needed:]
            self.needed = 0
        return rejected

    def sort(self):
        self.accepted = sorted(self.accepted, key=lambda x: (-x.gpa, x.name, x.last))


departments = {x: Department(x, n) for x in department_names}


applicants = []
with open(fname, 'r') as f:
    for line in f:
        applicants.append(Student(*line.split()))

for option in ['first', 'second', 'third']:
    applicants = sorted(applicants, key=lambda x: (-x.gpa, x.name, x.last))
    dep_candidates = defaultdict(list)
    for app in applicants:
        dep_candidates[app.options[option]].append(app)
    rejected = []
    for dep in department_names:
        rejected += departments[dep].admit(dep_candidates[dep])
    applicants = rejected[:]

for dep in department_names:
    print(departments[dep].name)
    departments[dep].sort()
    for applicant in departments[dep].accepted:
        print(f"{applicant.full_name} {applicant.gpa}")
    print()

