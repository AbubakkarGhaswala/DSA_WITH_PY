my_friends = {"Ali", "Ahmed", "Sara", "Zaid"}

friend_friends = {"Sara", "John", "Ahmed", "Karan"}

# Find Mutual Friends :- 

mutual_friends = my_friends & friend_friends

print(f"Mutual Friends :- {mutual_friends}")


# Find Only My Friends :-

only_my_friend = my_friends - friend_friends

print(f"Only My Friends :- {only_my_friend}")


# Find That Friends Which My Friend Have And i Don't :- 

friend_friends_only = friend_friends - my_friends

print(f"Friends Which My Friend Have And I Don't :- {friend_friends_only}")