# Task 1 — Count Vowels
# Input:
# name = "Abubakkar"
# Output:
# Vowels = 4
# Rules:
# ❌ Don't use count() multiple times.
# Use:
# traversal
# condition
# counter


name = "Abubakkar"

vowels = "aeiouAEIOU"

vowels_count = 0

for ch in name:
    if ch in vowels:
        vowels_count = vowels_count + 1
    
print(vowels_count)