#merging dict

dict1 = {}
dict2 = {}

n1 = int(input("Enter number of elements for first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("Enter number of elements for second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)




# matrix transpose

rows = int(input(" number of rows: "))
cols = int(input(" number of columns"))
matrix = [list(map(int, input().split())) for s in range(rows)]
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
for row in transpose:
    print(*row)



#max and min in matrix
rows = int(input(" number of rows: "))
cols = int(input(" number of columns"))
matrix = [list(map(int, input().split())) for s in range(rows)]
max_value = max(max(col) for col  in matrix)
min_value = min(min(col) for col in matrix)
print(max_value)
print(min_value)



#probability
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
probability_dict = {}
for i in range(2, 13):  
    c = 0
    for j in [(d1, d2) for d1 in dice1 for d2 in dice2]:
        if i == sum(j):
            c += 1
    probability_dict[i] = c / 36  
R = int(input())  
player1_wins = 0
player2_wins = 0
def get_probability(sum_value):
    return probability_dict[sum_value]
for _ in range(R):
    P1_d1, P1_d2, P2_d1, P2_d2 = map(int, input().split())
    
    P1_sum = P1_d1 + P1_d2
    P2_sum = P2_d1 + P2_d2
    P1_prob = get_probability(P1_sum)
    P2_prob = get_probability(P2_sum)
    
    if P1_prob < P2_prob:
        player1_wins += 1
    elif P2_prob < P1_prob:
        player2_wins += 1
if player1_wins > player2_wins:
    print("Player 1 wins")
elif player2_wins > player1_wins:
    print("Player 2 wins")
else:
    print("It's a draw")







#frequency count
a = [1,22,43,22,22,33,65,61,6,1,6,1]
b = {}
for c in a:
   if c in b:
     b[c] += 1
    
   else:
     b[c] = 1
print(b)









