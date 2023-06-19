def changing_direction(elements: list[int]) -> int:
    if len(elements) < 3:
        return 0;
    changes = 0
    direction = None
    for i in range(1, len(elements)):
        if elements[i] > elements[i - 1]:
            new_direction = "increase"
        elif elements[i] < elements[i - 1]:
            new_direction = "decrease"
        else:
            new_direction = direction
        if direction is not None and new_direction != direction:
            changes += 1
        direction = new_direction

    return changes


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
