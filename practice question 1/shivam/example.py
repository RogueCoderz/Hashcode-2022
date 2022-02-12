with open("input_data/a_an_example.in.txt", 'r') as f:
    lines = f.readlines()
    lines = [element.replace("\n", "") for element in lines]
    
clients = lines[0]
like_ingredients = set()
dislike_ingredients = set()

for line1, line2 in zip(lines[1::2], lines[2::2]):
    like_ingredients.update(set(line1.strip().split(' ')[1:]))
    dislike_ingredients.update(set(line2.strip().split(' ')[1:]))
    
ingredients = set(sorted(like_ingredients)) - set(sorted(dislike_ingredients))
ingredients = sorted(list(ingredients))
print(f"{len(ingredients)} " + ' '.join(list(ingredients)))

