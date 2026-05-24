# AI = Pattern Recognition

user_history = ["Mirzapur", "Sacred Games"]

similar_user = ["Mirzapur", "Sacred Games", "Farzi"]

# Recommend unseen show
for show in similar_user:
    if show not in user_history:
        print("Recommended:", show)