def mostPopularFriend(d):
    friend_counts = {}
    
    # Iterate over each set of friends
    for friends in d.values():
        for friend in friends:
            friend_counts[friend] = friend_counts.get(friend, 0) + 1
    
    # Find the friend with the highest count
    most_popular_friend = max(friend_counts, key=friend_counts.get)
    
    return most_popular_friend

# Example usage:
d = dict()
d["fred"] = set(["wilma", "betty", "barney"])
d["wilma"] = set(["fred", "betty", "dino"])

print("Most popular friend:", mostPopularFriend(d))
