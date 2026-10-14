
marks = [45, 20, 80, 35, 60]

print("Original marks:", marks)

# Linear Search
key = int(input("Enter marks to search: "))
found = False

for i in range(len(marks)):
    if marks[i] == key:
        print("Marks found at position", i + 1)
        found = True
        break

if not found:
    print("Marks not found")

# Bubble Sort
for i in range(len(marks)):
    for j in range(len(marks) - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Sorted marks:", marks)
