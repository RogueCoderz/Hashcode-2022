clients = int(input())

like_ingredients = set()
dislike_ingredients = set()

for _ in range(clients):
    like_ingredients.update(set(input().strip().split(' ')[1:]))
    dislike_ingredients.update(set(input().strip().split(' ')[1:]))

ingredients = list(set(sorted(like_ingredients)) - set(sorted(dislike_ingredients)))

print(f"{len(ingredients)} " + ' '.join(list(ingredients)))
