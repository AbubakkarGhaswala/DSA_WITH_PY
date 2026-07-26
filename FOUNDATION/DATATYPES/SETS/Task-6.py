required_skills = {
    "Python",
    "SQL",
    "Git",
    "Docker",
    "Linux",
    "AWS",
    "Communication"
}

candidate_a = {
    "Python",
    "SQL",
    "Git",
    "Docker",
    "Communication"
}

candidate_b = {
    "Python",
    "Java",
    "Git",
    "Linux",
    "AWS",
    "HTML",
    "CSS"
}

print("------------------- Candidate A -----------------")
# For Candidate A
# Question 1
# Matched Skills
# Example:
# Matched Skills:
# Python
# SQL
# Git
# Docker
# Communication


match_skills = candidate_a & required_skills
print(f"Matched Skills For Candidate A :- {match_skills}")


# Question 2
# Missing Skills
# Example:
# Missing Skills:
# Linux
# AWS


missing_skills = required_skills - candidate_a  
print(f"Missing Skills :- {missing_skills}")



# Question 3
# Extra Skills
# Skills candidate knows but company doesn't require.
# Example:
# Extra Skills:
# None
# or
# Extra Skills:
# HTML
# CSS



extra_skills_a = candidate_a - required_skills
if not extra_skills_a:
    print("None")
else :
    print(f"Extra Skills :- {extra_skills_a}")




# Question 4
# Match Percentage
# Formula:
# Matched Skills
# ------------------------ × 100
# Required Skills
# Don't hardcode.


count_required_skills = len(required_skills)



count_match_skills_a = len(match_skills)



match_percentage_a = (count_match_skills_a / count_required_skills) * 100
print(f"Match Percentage Of A {round(match_percentage_a)}%")



# Question 5
# Eligibility
# Rules:
# If percentage >= 80
# Eligible for Interview
# Else
# Not Eligible


if match_percentage_a >= 80:
    print("Eligible for Interview")
else :
    print("Not Eligible")



print("------------------- Candidate B -----------------")


# For Candidate B
# Question 1
# Matched Skills
# Example:
# Matched Skills:
# Python
# SQL
# Git
# Docker
# Communication


match_skills_b = candidate_b & required_skills
print(f"Matched Skills For Candidate B :- {match_skills_b}")


# Question 2
# Missing Skills
# Example:
# Missing Skills:
# Linux
# AWS


missing_skills_b = required_skills - candidate_b  
print(f"Missing Skills Of B:- {missing_skills_b}")



# Question 3
# Extra Skills
# Skills candidate knows but company doesn't require.
# Example:
# Extra Skills:
# None
# or
# Extra Skills:
# HTML
# CSS




extra_skills_b = candidate_b - required_skills
if not extra_skills_b:
    print("None")
else :
    print(f"Extra Skills :- {extra_skills_b}")




# Question 4
# Match Percentage
# Formula:
# Matched Skills
# ------------------------ × 100
# Required Skills
# Don't hardcode.



count_match_skills_b = len(match_skills_b)



match_percentage_b = (count_match_skills_b / count_required_skills) * 100
print(f"Match Percentage Of A {round(match_percentage_b)}%")



# Question 5
# Eligibility
# Rules:
# If percentage >= 80
# Eligible for Interview
# Else
# Not Eligible


if match_percentage_b >= 80:
    print("Eligible for Interview")
else :
    print("Not Eligible")




# Question 6
# Who has more matched skills?
# Print:
# Candidate A
# or
# Candidate B
# or
# Tie

print(f"Number Of Match Skills Candidate A Have :- {len(match_skills)}")

print(f"Number Of Match Skills Candidate B Have :- {len(match_skills_b)}")


if len(match_skills) == len(match_skills_b):
    print("Tie")
elif len(match_skills) > len(match_skills_b):
    print("Candidate A Have More Match Skills Then Candidate B")
elif len(match_skills) < len(match_skills_b):
    print("Candidate B Have More Match Skills Than Candidate A")




# Question 7
# Who has more extra skills?
# Remember:
# Extra skills are skills not required by the company.

if len(extra_skills_a) == len(extra_skills_b):
    print("Both Candidate A And Candidate B Have Same Number Of Extra Skills...")
elif len(extra_skills_a) > len(extra_skills_b):
    print("Candidate A Have More Extra Skills Then Candidate B...")
elif len(extra_skills_a) < len(extra_skills_b):
    print("Candidate B Have More Extra Skills Then Candidate A..")


# Question 8

# Which candidate is closer to the company's requirements?

# Think carefully.

# Don't compare total skills.

# Compare the requirement match.

len_of_require_skill = len(required_skills)

len_of_match_skill_of_can_a = len(match_skills)

len_of_match_skill_of_can_b = len(match_skills_b)

distance_from_a = len_of_require_skill - len_of_match_skill_of_can_a

distance_from_b = len_of_require_skill - len_of_match_skill_of_can_b



if distance_from_a < distance_from_b:
    print("Candidate A Is More Closer To Company's Required Skills...")
elif distance_from_b < distance_from_a:
    print("Candidate B Is More Closer To Company's Required Skills...")
