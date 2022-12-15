import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = 5
lines = [""] * (2 * n - 1)

# construction de la ligne centrale
for i in range(n):
    lines[n - 1] += letters[i]

for j in range(n - 1):
    lines[n - 1] += letters[n - 2 - j]

# construction des autres lignes
for i in range(n - 1):
    lines[(n - 1) - (i + 1)] = lines[n - 1 - i].replace(letters[n - i - 1], letters[n - i - 2])
    lines[(n - 1) + (i + 1)] = lines[n - 1 - i].replace(letters[n - i - 1], letters[n - i - 2])

# affiche les lignes du tableau
for i in lines:
    sys.stdout.write(i)
    sys.stdout.write("\n")