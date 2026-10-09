# grade_reporter.py

scores = [92, 85, 74, 61, 58, 100, 78, 88, 45, 91]

# Running total and counters
total_score = 0
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

print("--- INDIVIDUAL GRADE REPORT ---")

# Loop through each score in the list
for score in scores:
    total_score += score  # Running total

    # Grade determination using if / elif / else
    if score >= 90:
        grade = "A"
        count_a += 1
    elif score >= 80:
        grade = "B"
        count_b += 1
    elif score >= 70:
        grade = "C"
        count_c += 1
    elif score >= 60:
        grade = "D"
        count_d += 1
    else:
        grade = "F"
        count_f += 1

    print(f"Score: {score:3d} | Grade: {grade}")

# Calculate summary stats
total_students = len(scores)
average_score = total_score / total_students if total_students > 0 else 0

print("\n--- CLASS SUMMARY ---")
print(f"Total Students : {total_students}")
print(f"Class Average  : {average_score:.2f}")
print(f"Grade Counts   : A: {count_a} | B: {count_b} | C: {count_c} | D: {count_d} | F: {count_f}")