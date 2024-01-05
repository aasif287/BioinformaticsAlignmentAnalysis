import sys
linecount = 0
linecount1 = 0
linecount2 = 0
with open(sys.argv[1]) as f:
    with open('out.txt', 'w') as f1:
        for line in f:
            linecount = linecount +1
            if line.startswith('>'):
                continue
            f1.write(line)
z = 0
n = 0
totalnumberofseqline = int(linecount - 2) 
numberofline1 = int((totalnumberofseqline) / 2)
a_file = open('out.txt')
number_of1 = numberofline1
with open('bioinfo.txt','w') as x1:
    for i in range(number_of1):
        line = a_file.readline()
        x1.write(line)
with open('bioinfo.txt', 'r') as x:
    bleh = x.read()
    data = bleh.replace('\n', '')
with open('bioinfo.txt', 'w') as i:
  i.write(data)
with open('bioinfo1.txt','w') as x1:
    for i in range(number_of1,totalnumberofseqline):
        line = a_file.readline()
        x1.write(line)
with open('bioinfo1.txt', 'r') as x:
    bleh = x.read()
    data = bleh.replace('\n', '')
with open('bioinfo1.txt', 'w') as i:
  i.write(data)
with open('bioinfo.txt') as x:
    for line in x:
        linecount1 = linecount1 +1
        if linecount1 == 1:
            seq1 = line
with open('bioinfo1.txt') as x:
    for line in x:
        linecount2 = linecount2 +1
        if linecount2 == 1:
            seq2 = line
seq1 = seq1.strip()
seq2 = seq2.strip()
gap_open = -2
match_score = 1
mismatch = -1
len1 = len(seq1)  
len2 = len(seq2)
test1 = ''
test2 = ''


matrix = [[0 for i in range(len1 + 1)] for j in range(len2 +1)]
for i in range(0, len2 + 1):
    matrix[i][0] = gap_open + matrix[i-1][0]
for j in range(0, len1 + 1):
    matrix[0][j] = gap_open + matrix[0][j-1]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if seq1[j-1] == '-' or seq2[i-1] == '-':
            thing = gap_open
        if seq1[j-1] == seq2[i-1]:
            thing = match_score
        else:
            thing = mismatch
        match = matrix[i - 1][j - 1] + thing
        horizontal = matrix[i - 1][j] + gap_open
        vertical = matrix[i][j - 1] + gap_open
        matrix[i][j] = max(match, horizontal, vertical)
for i in range(len2):
    for j in range(len1):
        if seq1[j-1] == '-' or seq2[i-1] == '-':
            thing = gap_open
        if seq1[j-1] == seq2[i-1]:
            thing = match_score
        else:
            thing = mismatch
        if matrix[len2][len1] == matrix[len2-1][len1-1] + thing:
            test1 = test1 + seq1[len1-1]
            test2 = test2 + seq2[len2-1]
            len2 = len2 - 1
            len1 = len1 - 1
        else:
            if matrix[len2][len1] == matrix[len2][len1-1] + gap_open:
                test1 =test1 + seq1[len1-1]
                test2 = test2 + '-'
                len1 = len1 - 1
            else:
                if matrix[len2][len1] == matrix[len2-1][len1] + gap_open:
                    test1 = test1+ '-'
                    test2 = test2+ seq2[len2-1]
                    len2 = len2 - 1
def revalign00():
    return test1[::-1]
test1 = revalign00()
def revalign01():
    return test2[::-1]
test2 = revalign01()
new_seq1 = list(test1)
new_seq2 = list(test2)
count = 0
for i in range(len(new_seq1)):
    if new_seq1[i]==new_seq2[i]:
        count = count + 1
count1 = 0
for i in range(len(new_seq1)):
    if new_seq1[i]== '-':
        count1 = count1 + 1         
count2 = 0
for i in range(len(new_seq1)):
    if new_seq2[i]=='-':
        count2 = count2 + 1
count3 = 0
for i in range(len(new_seq1)):
    if not new_seq1[i]==new_seq2[i]:
        count3 = count3 + 1
match_count = count
gap_count = count2 + count1
mismatch_count = count3 - gap_count
score = match_count*match_score + gap_count*gap_open + mismatch_count*mismatch
score = str(score)
test1 = str(test1)
test2 = str(test2)
file = open('align_NW.txt', 'w')
file.write('Score = ' + score + '\n')
file.write('Q1    ' + test1 + '\n')
file.write('Q2    ' + test2)
file.close()