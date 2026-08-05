attendance = ['P', 'A', 'P', 'P', 'A', 'P', 'A']
absent_count = 0

for record in attendance:
    if record == 'A':
        absent_count = absent_count + 1

print("Total Absences:", absent_count)
