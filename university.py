from collections import defaultdict

department_names = ['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering']
department_names.sort()
n = int(input())
fname = "applicants.txt"


class Student:
    def __init__(self, name, last, phy, chem, math, cs, first, second, third):
        self.name = name
        self.last = last
        self.options = {"first": first, "second": second, "third": third}
        self.scores = {"Physics": (float(phy) + float(math))/2,
                       "Chemistry": float(chem),
                       "Mathematics": float(math),
                       "Engineering": (float(cs) + float(math))/2,
                       "Biotech": (float(chem) + float(phy))/2}
        self.full_name = f"{self.name} {self.last}"


class Department:
    def __init__(self, name, _n):
        self.name = name
        self.needed = _n
        self.accepted = []

    def admit(self, candidates):
        rejected = []
        candidates = self.sort(candidates)
        if len(candidates) <= self.needed:
            self.accepted += candidates
            self.needed -= len(candidates)
        else:
            for i in range(self.needed):
                self.accepted += [candidates[i]]
            rejected = candidates[self.needed:]
            self.needed = 0
        self.accepted = self.sort(self.accepted)
        return rejected

    def sort(self, _students):
        return sorted(_students, key=lambda x: (-x.scores[self.name], x.name, x.last))


departments = {x: Department(x, n) for x in department_names}
applicants = []
with open(fname, 'r') as f:
    for line in f:
        applicants.append(Student(*line.split()))

for option in ['first', 'second', 'third']:
    dep_candidates = defaultdict(list)
    for app in applicants:
        dep_candidates[app.options[option]].append(app)
    applicants = sum([departments[dep].admit(dep_candidates[dep])
                      for dep in department_names], [])

for dep in department_names:
    with open(f"{dep.lower()}.txt", "w") as f:
        for applicant in departments[dep].accepted:
            f.write(f"{applicant.full_name} {applicant.scores[dep]}\n")

