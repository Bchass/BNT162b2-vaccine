import python_codon_tables as pct
import csv

def read_csv_file(filename):
    with open(filename, 'rt') as fn:
        reader = csv.reader(fn)
        next(reader)
        return list(reader)

tictac = read_csv_file('side-by-side.csv')

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
 
tables = most_freq('m_musculus_10090')

ac = tables
print("Comparing m_musculus_10090 table: ", ac, '\n')

mismatches = 0
match = 0
for(_, tic, tac) in tictac:
    ac = tables[tic]
    if tac == ac:
        match +=1
    else:
        if tac != ac:
            mismatches = 0

print ("Codon match: ""{0:.1f}%".format(1 - (mismatches) + 100*match/len(tictac)))
