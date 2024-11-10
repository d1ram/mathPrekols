def game(x):
    values = [x]
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = (x * 3) + 1
        values.append(x)

    return values

x = (2**17)
list = game(x)
print(f"List for {x} is {list}. Highest number is {max(list)}. List is {len(list)} numbers long.")