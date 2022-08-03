# Needleman Wunsch Algorithm implementation

#Using the following scores: match +1 mismatch -1 gap -2


match_score = lambda x,y,i,j: -1 if x[i] != y[j] else 1
# Calculation of the match/mismatch score  S(i-1, j-1), S stands for similarity

def align(x, y, gap_penalty=-2):
    # Returns score matrix SM and trace(path) matrix TM

    m = len(x)
    n = len(y)
#creating an empty score matrix  and traceback of an approaprite size
    SM = [[0 for i in range(n + 1)] for j in range(m + 1)]
    TM = [[0 for i in range(n + 1)] for j in range(m + 1)]

# Filling the score matrix
# Step 1: Initialisation
# SM(i,0) = i, SM(O,j) = j

    # Fill out the first column
    for i in range (0, m+1):
        SM[i][0] = gap_penalty * i
        TM[i][0] = 2
    # Fill out the first row
    for j in range(0, n+1):
        SM[0][j] = gap_penalty * j
        TM[0][j] = 1

        # Step 2: Filling the score matrix
        for i in range(1, m+1):
            for j in range(1, n+1):

                match = SM[i - 1][j - 1] + match_score(x,y,i-1, j-1)
                delete = SM[i - 1][j] + gap_penalty
                insert = SM[i][j - 1] + gap_penalty

                # Record the maximum value from the three possible scores calculated above
                value = max(match, delete, insert)
                SM[i][j] = value

                # Filling the traceback matrix
                if value == match:
                    TM[i][j] = 0
                elif value== insert:
                    TM[i][j] = 1
                elif value == delete:
                    TM[i][j] = 2
            print(TM[i][j])

    #getting the align score
    AS = SM[-1][-1]
    return SM, TM, AS

def traceback(path_matrix, x, y, score):
    # Returns alignment
    align_top = ""
    matches = ""
    align_bottom = ""

    i = len(x) - 1
    j = len(y) - 1

    # Deducing the optimal alignment from the traceback matrix
    while (i, j) != (-1, -1):
        path = path_matrix[i + 1][j + 1]
        species1 = x[i]
        species2 = y[j]
        match = " "
        if path == 0:
            i -= 1
            j -= 1
            if species1 == species2:
                match = "|"
        elif path == 1:
            species1 = "-"
            j -= 1
        else:
            species2 = "-"
            i -= 1
        align_top = species1 + align_top
        align_bottom = species2 + align_bottom
        matches = match + matches
    return f"{align_top}\n{matches}\n{align_bottom}\nscore: {score}"



if __name__ == '__main__':

    seq1 = input("Enter or paste sequence 1:")
    seq2 = input("Enter or paste sequence 2:")
    solution = []

    score_matrix, trace_matrix, alignment_score = align(seq1, seq2)

    print(traceback(trace_matrix, seq1, seq2, alignment_score))