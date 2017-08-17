# coding=UTF-8

def read_dict(dict_file):
    dict = set()
    file = open(dict_file, 'r')

    for line in file:
        dict.add(line.rstrip())

    return dict

def match(dict, target_file, match_file, unmatch_file):
    in_file = open(target_file, 'r')
    match = open(match_file, "w")
    unmatch = open(unmatch_file, "w")
    for line in in_file:
        line = line.rstrip()
        toks = line.split('\t')
        digest = toks[0]
        if digest in dict:
            match.writelines(line + '\n')
        else:
            unmatch.write(line + '\n')

if __name__ == "__main__":
    dict_file = "dict"
    target_file = "todo"
    match_file = "match.out"
    unmatch_file = "unmatch.out"
    dict = read_dict(dict_file)
    match(dict, target_file, match_file, unmatch_file)
