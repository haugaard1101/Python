def party_planner(invited_friends, rsvp_friends):
    # Find friends who have not RSVP'd
    not_rsvped = invited_friends - rsvp_friends

    # Find friends who were not invited but RSVP'd
    not_invited_but_rsvped = rsvp_friends - invited_friends

    # Find friends who are common in both lists
    common_friends = invited_friends & rsvp_friends

    return not_rsvped, not_invited_but_rsvped, common_friends

# test data
invited_friends = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
rsvp_friends = {'Alice', 'Charlie', 'Frank', 'Grace', 'David'}

not_rsvped, not_invited_but_rsvped, common_friends = party_planner(invited_friends, rsvp_friends)

print("Friends who have not RSVP'd:")
for friend in not_rsvped:
    print(friend)

print("\nFriends who were not invited but RSVP'd:")
for friend in not_invited_but_rsvped:
    print(friend)

print("\nFriends who are common in both lists:")
for friend in common_friends:
    print(friend)
