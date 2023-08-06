### Problem **8: Initialize dictionary with default values**
# In Python, we can initialize the keys with the same values.


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# **Expected output:**{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}

d={}

for i in employees:
    d[i]=defaults
print(d)     