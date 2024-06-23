import csv

'''
Dataset: 'Cyber Security Attacks' from Kaggle, found here: https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks
'''

def processCSV(filename, desired_column):
    file = open(filename, 'r')
    reader = csv.reader(file, delimiter=',')

    outfile = open('./output.txt', 'w')

    desired_index = None
    available_columns = next(reader)
    for i in range(len(available_columns)):
        curr_col = available_columns[i].lower()
        if curr_col in desired_column:
            desired_index = i
    
    col_value_to_freq = {}

    SEPARATOR = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'

    outfile.write(SEPARATOR)

    for row in reader:
        outfile.write(','.join(row))
        outfile.write('\n' + SEPARATOR)

        col = row[desired_index]

        if col in col_value_to_freq:
            col_value_to_freq[col] += 1
        else:
            col_value_to_freq[col] = 1

    max_col = max(col_value_to_freq, key=col_value_to_freq.get)

    print(col_value_to_freq)

    return 'The most common ' + desired_column + ' is: ' + max_col

'''
file = open('./archive/cybersecurity_attacks.csv', 'r')
output = open('results.txt', 'w')

reader = csv.reader(file, delimiter=',')

# first line tells us what each column represents
first_line = next(reader)
#print(first_line)

# find indices of attack type & protocol columns
attack_type_idx = None   
protocol_type_idx = None
for i in range(len(first_line)):
    curr_col = first_line[i].lower()
    if 'attack type' in curr_col:
        attack_type_idx = i
    elif 'protocol' in curr_col:
        protocol_type_idx = i

attack_list = []    # exhaustive list of all attacks
protocol_list = []

# mapping attacks & protocols to their respective counts
attack_to_freq = {} 
protocol_to_freq = {}

# read through the csv file
SEPARATOR="-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
for row in reader:
    attack = row[attack_type_idx]
    protocol = row[protocol_type_idx]

    output.write(SEPARATOR)
    output.write(attack + ' - ' + protocol + '\n')

    if attack not in attack_list:
        attack_list.append(attack)
    if protocol not in protocol_list:
        protocol_list.append(protocol)
    
    if attack in attack_to_freq:
        attack_to_freq[attack] += 1
    else:
        attack_to_freq[attack] = 1

    if protocol in protocol_to_freq:
        protocol_to_freq[protocol] += 1
    else:
        protocol_to_freq[protocol] = 1

for a in attack_list:
    print(a)
for p in protocol_list:
    print(p)

print(attack_to_freq, protocol_to_freq)

# how below works: returns item in dictionary s.t. that the key function dict.get returns the largest value
max_attack = max(attack_to_freq, key=attack_to_freq.get)
max_protocol = max(protocol_to_freq, key=protocol_to_freq.get)

print(max_attack, max_protocol)

# close files

file.close()
output.close()
'''
