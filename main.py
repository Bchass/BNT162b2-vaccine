
import csv

def read_csv(filename):
    records = []
    with open(filename, 'rt') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        for x, row in enumerate(reader):
            if x > 0:
                records.append(row)

    return records

codons = read_csv('codon-table-grouped.csv')
tictac = read_csv('side-by-side.csv')

cd = {}
for c in codons:
    cd[c[1]] = c[0]
print(cd)

match = 0
mismatch = 0

for element in tictac:
    tic = element[1]
    tac = element[2]

    ac = tic
    print(ac)

    if tic[2] == 'G' or tic[2] == 'C':
        print("Codon is G/C")
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
        print('No mismatch' + '\n')

print ("{0:.0f}%".format(1 + float(mismatch) + 100*match/len(tictac)))