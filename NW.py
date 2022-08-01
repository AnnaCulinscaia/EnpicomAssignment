'''The Needleman-Wunsch Algorithm
 '''
#Ask the user to imput the sequences
#x = input("Enter or paste sequence 1:")
#y = input("Enter or paste sequence 2:")

#calculation of the score  S(i-1, j-1), S stands for similarity
align_score = lambda x,y,i,j: 1 if x[i] != y[j] else 0

def find_solution(SM, m, n):

    if m == 0 or n == 0:
        return

    insert = SM[m][n-1] + 1
    align = SM[m-1][n-1] + align_score(x,y,m-1, n-1)
    delete = SM[m-1][n] + 1

    best_choice = min(insert, align, delete)

    if best_choice == insert:
        solution.append('insert_'+str(y[n-1]))
        return find_solution(SM, m, n-1)

    elif best_choice == align:
        solution.append('align_'+str(y[n-1]))
        return find_solution(SM, m-1, n-1)

    elif best_choice == delete:
        solution.append('delete_'+str(x[m-1]))
        return find_solution(SM, m-1, n)


def alignment(x, y):
    n = len(y)
    m = len(x)

#creating an empty matrix of an approaprite size
    SM = [[0 for i in range(n + 1)] for j in range(m + 1)]

# Filling the score matrix
# Step 1: Initialisation
# SM(i,0) = i, SM(O,j) = j
    for i in range (1, m+1):
        SM[i][0] = i

    for j in range(1, n+1):
        SM[0][j] = j

        #Step 2: Filling the matrix
        #Recursion, based on the principle of optimality
        for i in range(1, m+1):
            for j in range(1, n+1):
            #min of align, delete, or insert
                SM[i][j] = min(SM[i-1][j-1] + align_score(x,y,i-1, j-1), SM[i-1][j] + 1, SM[i][j-1] +1)
    #Step 3: Determine the number of optimal edit steps and Traceback
    find_solution(SM, len(x), len(y))



    return SM[m][n], solution[::-1], SM

if __name__ == '__main__':
    x = 'SEND'
    y = 'AND'
    solution = []

    opt_edit_steps, solution, matrix = alignment(x, y)
    print(str(opt_edit_steps))
    print(str(solution))
    seqX = ""
    seqY = ""
    i = len(x)
    j = len(y)
    SM = matrix
    while (i > 0 and j > 0):
        # if align
        if (i > 0 and j > 0 and SM[i][j] == SM[i - 1][j - 1] + + align_score(x, y, i - 1, j - 1)):
            seqX = x[i - 1] + seqX
            seqY = y[j - 1] + seqY

            i = i - 1
            j = j - 1

        elif (i > 0 and SM[i][j] == SM[i - 1][j] + 1):
            seqX = x[i - 1] + seqX
            seqY = '-' + seqY

            i = i - 1
        else:
            seqX = '-' + seqX
            seqY = y[j - 1] + seqY

            j = j - 1
    print(seqX)
    print(seqY)
