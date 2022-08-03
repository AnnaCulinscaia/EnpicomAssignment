Hi!💻

#### **1. Error Correction**
* If we create a list of all reads including their reverse complements, incorrect reads and their reverse complements will appear in this list just once. Knowing that, we can determine correct and incorrect reads.
* Afterwards we correct the errors in incorrect reads by finding a correct read using the Hamming distance adn just comparing incorrect reads with correct ones (equal to 1)


#### **2. Maximum Matchings**
* A-U and G-C pairs can be represented as two bipartite subgraphs,
Then maximum number of perfect matchings would be the number of matchings in the first subgraph multiplied by that of the second subgraph.
* Factorial method is used as this problem is combinatorial, as first node (for instance, G) can pair with n complementary nodes (for instance, C), the second node can only pair with (n-1) nodes, etc.
The solution depends of which base has more counts, if there are n Gs and m Cs, and n>m, there will be m matchings with (n-m) subset . 

There are `n!/[(n-m)!*m!]` ways to select m bases from n bases and `m!` ways to form different pairs, the final number of options is `(n!/[(n-m)!*m!]) * m!`. Therefore, there are `n!/(n-m)!`  of G-C pairs in this case. Same applies to A-U pairs




#### **3. Needleman Wunsch algorithm**
I have implemented Needleman Wunsch algorithm, which is  a dynamic programming algorithm for finding the optimal alignment of
two strings.My implementation is suitable for alignment of DNA sequences.

The algorithm was implemented in the following three steps:
1. Initialising the score matrix **SM** and initialising traceback matrix **TM**
2. Filling the score matrix and a traceback matrix using the following recurrence relations*: 
`SM(i,j) = max[TM(i-1, j) + gap_penalty, SM(i, j-1) + gap_penalty, SM(i − 1, j − 1) + S(xj, yj )]`
3. Deducing the optimal alignment from the traceback matrix TM: start from bottom rigth cell of TM and follow the condition rules until reaching TM(1, 1)

_*The values in the score matrix depend on the chosen match/mismatch and gap penalties. I used +1 for a match, -1 for a mismatch and -2 for a gap. This is suitable for the alignment of DNA sequences. 
The values in the traceback matrix are either 0(for math/mismatch), 1(for insert) or 2 (for deletion)_



