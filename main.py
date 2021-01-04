import csv

def read_csv_file(filename):
    with open(filename, 'rt') as fn:
        reader = csv.reader(fn, delimiter=',')
        next(reader)
        return list(reader)

codons = read_csv_file('codon-table-grouped.csv')
tictac = read_csv_file('side-by-side.csv')

cd = {c: codon for codon, c in codons}
print(cd)

match = 0
mismatch = 0

for(_, tic, tac) in tictac:

    ac = tic
    print(ac)

    if tic[2] in ['G','C']:
        print("Codon is already G or C")
    else:
        result = tic[:2] + "C"
        print("Replacing with C, result: " + result)
        
        if cd[tic] == cd[result]:
            ac = result
        else:
            result = tic[:2] + "G"

            if cd[tic] == cd[result]:
                ac = result

    if tac == ac:
        match +=1
    
    if tac != ac:
        print('Mismatch' + '\n')
        mismatch = 1
    else:
        print('Match' + '\n')

print ("Codon match: ""{0:.1f}%".format(1 + float(mismatch) + 100*match/len(tictac)))