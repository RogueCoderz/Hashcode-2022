with open("input_data/d_difficult.in.txt", "r") as f:
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

# to dump the output to a file inside output_data folder
# with open("output_data/d_difficult.out.txt", "w") as f:
#     f.write(f"{len(ingredients)} {out_str}")