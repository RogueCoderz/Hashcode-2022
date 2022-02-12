with open("input_data/e_elaborate.in.txt", "r") as f:
    input_str = f.read().split()[1:]

like_set = set()
dislike_set = set()

like = True
index = 0
indexing = True

while indexing:

    if like:
        n = int(input_str[index])
        if n != 0:
            for i in range(index+1, index+n+1):
                like_set = like_set.union({input_str[i]})
        like = False
        index = index + n + 1

    else:
        n = int(input_str[index])
        if n != 0:
            for i in range(index+1, index+n+1):
                dislike_set = dislike_set.union({input_str[i]})
        like = True
        index = index + n + 1

    if index == len(input_str):
        indexing = False

common = like_set.intersection(dislike_set)
ingredients = like_set.difference(common)
ingredients = set(sorted(ingredients))

out_str = " ".join(ingredients)
print(f"{len(ingredients)} {out_str}")