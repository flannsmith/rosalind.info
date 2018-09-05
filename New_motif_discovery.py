#ProSite database is used to find motifs in known proteins
#To find or discover a novel candidate motifs, tools such as MEME and GLAM2 are needed.

#One of the most widely used programs for discovering motifs in a collection of homologous DNA or protein sequences is MEME. MEME takes as input a collection of DNA/protein sequences and outputs motifs exceeding a user-specified statistical confidence threshold.

#MEME cannot discover motifs that exhibit indels, because it does not take gaps into consideration. This limitation is overcome by another program from the MEME Suite called GLAM2. Discovering motifs containing gaps is intrinsically more difficult than discovering ungapped motifs, because there are vastly more possible gapped motifs than ungapped ones.
#Each motif in MEME is assigned an expected value(E), which is the likelihood of it occurring by chance. This denotes the statistical significance of the motif. GLAM2 assigns scores instead of e-values: the score favours alignment of similar residues, and disfavours insertions and deletions.

#Given: A set of protein strings in FASTA format that share some motif with minimum length 20.

#Return: Regular expression for the best-scoring motif.

# 1) Go to MEME site: http: // meme-suite.org/tools/meme
# 2) Enter email address(and re-enter)
# 3) Upload dataset
# 4) Click "Start search"
# 5) Click the link next to "You can view your job results at:"
# 6) Solution is next to "Regular Expression"
