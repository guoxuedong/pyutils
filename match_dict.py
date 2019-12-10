# coding=UTF-8

def read_dict(dict_file):
    set_dict = set()
    in_file = open(dict_file, 'r')

    for line in in_file:
        set_dict.add(line.rstrip())

    return set_dict

def read_dict_map(dict_file):
    kv_dict = dict()
    in_file = open(dict_file, 'r')

    for line in in_file:
        toks = line.rstrip().split('\t')
        if len(toks) != 4:
            print "invalid line:" + line
            continue

        if toks[1] < 100:
            print "unexpected state:" + line
            continue

        kv_dict[toks[0]] = toks[3]

    in_file.close()

    return kv_dict

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
    dict1 = read_dict(dict_file)
    match(dict1, target_file, match_file, unmatch_file)
