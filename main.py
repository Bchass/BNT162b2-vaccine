import python_codon_tables as pct
import csv

def read_csv_file(filename):
    with open(filename, 'rt') as fn:
        reader = csv.reader(fn, delimiter=',')
        next(reader)
        return list(reader)

# https://gist.github.com/sanxiyn/fddd1f18074076fb47e04733e6b62865
def most_freq(species):
    tables = {}
    codons_table = pct.get_codons_table(species)
    for ac in codons_table:
        freq_table = codons_table[ac]
        codons = sorted(freq_table)
        max_freq = 0
        most_freq_cd = None
        for codon in codons:
            frequency = freq_table[codon]
            if frequency > max_freq:
                max_freq = frequency
                most_freq_cd = codon
        for codon in codons:
            tables[codon] = most_freq_cd
    return tables

tictac = read_csv_file('side-by-side.csv')
tables = most_freq('m_musculus_10090')

match = 0
mismatch = 0

for(_, tic, tac) in tictac:
    ac = tables[tic]

    if tac == ac:
        match +=1

    if tac != ac:
        mismatch = 1
        
print ("Codon match: ""{0:.1f}%".format(1 + float(mismatch) + 100*match/len(tictac)))