column1 = []
column2 = []

with open('day1.txt', 'r') as f:
    for row in f:
        first_col, second_col = row.strip().split()
        column1.append(int(first_col))
        column2.append(int(second_col))

column1.sort()
column2.sort()

distances = [abs(column1[i] - column2[i]) for i in range(len(column1))]

total_distance = sum(distances)

print(total_distance)

scores = [row * column2.count(row) for row in column1]

similarity_score = sum(scores)

print(similarity_score)


    

    

