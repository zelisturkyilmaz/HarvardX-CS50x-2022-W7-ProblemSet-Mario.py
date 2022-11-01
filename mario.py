from cs50 import get_int

# Check for given conditions
while True:
    # Prompt user
    h = get_int("Height: ")
    # If not in range prompt again
    if h in range(1, 9):
        break

for i in range(h):
    # Print " " without new line
    print(" " * (h-i-1), end="")
    # Print # without new line
    print("#" * (i+1), end="")
    # Print 2 unit space w/out nl
    print("  ", end="")
    # Print # with new line
    print("#" * (i+1))

