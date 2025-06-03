# Ask the user to enter numbers separated by spaces (e.g. "1 65 1 16 5 6")
numbers = list(map(int, input("Enter numbers: ").split()))
# This list will store the leader numbers we find
leaders = []
# This keeps track of the biggest number we've seen so far, starting very small
max_so_far = -1
# Go through the list from right to left
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > max_so_far:
        leaders.append(numbers[i])
        max_so_far = numbers[i]
# We went right to left, so reverse the result to go back to left-to-right order
leaders.reverse()
# Print the leader numbers with a space between them
print(*leaders)