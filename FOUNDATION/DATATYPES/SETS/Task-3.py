event_a = {
    "Abu",
    "Ali",
    "Ahmed",
    "Sara",
    "Zaid"
}

event_b = {
    "Ahmed",
    "Sara",
    "John",
    "Karan",
    "Abu"
}

# Question - 1 Is Students participating in both events.

stu_participating_in_both_events = event_a & event_b

print(f"Students Who Have Participate In Both Events :- {stu_participating_in_both_events}")

# Question - 2 Is Students participating only in Event A.

stu_only_participate_in_event_a = event_a - event_b

print(f"Students Who Have Participate In Event A Only :- {stu_only_participate_in_event_a}")


# Question - 3 Is Students participating only in Event B.

stu_only_participate_in_event_b = event_b - event_a

print(f"Students Who Have Participate In Event B Only :- {stu_only_participate_in_event_b}")


# Question - 4 Total unique participants across both events.

unique_participants = event_a | event_b

print(f"Unique Names Across Both Events :- {unique_participants}")


# Question - 5 Print whether the two events have at least one common participant.

# Output should be either:

# Yes, both events have common participants.

# or

# No common participants.

if event_a.isdisjoint(event_b) == False:
    print("Yes, both events have common participants.")
else :
    print("No common participants.")