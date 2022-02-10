n =  int(input())

like_set = set()
dislike_set = set()
# main code
for _ in range(n):
    likes = set(input().split(" ")[1:])
    dislikes = set(input().split(" ")[1:])
    like_set = like_set.union(likes)
    dislike_set = dislike_set.union(dislikes)

common = like_set.intersection(dislike_set)
ingredients = like_set.difference(common)

out_str = " ".join(ingredients)
print(f"{len(ingredients)} {out_str}")