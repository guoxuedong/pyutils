# coding=UTF-8
import os


def read_dict_map(dict_file):
    kv_dict = dict()
    in_file = open(dict_file, 'r')

    count = 0
    for line in in_file:
        toks = line.rstrip().split('\t')
        if len(toks) != 4:
            print "invalid line:" + line
            continue

        if toks[1] < 100:
            print "unexpected state:" + line
            continue

        kv_dict[toks[0]] = toks[3]
        count += 1

    in_file.close()

    print "init dict done, item count:" + str(count)

    return kv_dict

def update_file(dict_kv, in_file_path, out_file_path):
    in_file = open(in_file_path, 'r')
    out_file = open(out_file_path, 'w')

    for line in in_file:
        line = line.rstrip()
        if line.endswith("DONE"):
            toks = line.split('\t')
            userid = toks[0]
            if userid in dict_kv:
                time = dict_kv[userid]
                line = "{}\t{}\t{}\t{}\t{}".format(toks[0], toks[1], toks[2], time, toks[3])
                print "update line to:" + line
            else:
                print userid + "not in dict"

        out_file.write(line + "\n")

    in_file.close()
    out_file.close()


def update_dir_file(dict_file, dir_path):
    dict_kv = read_dict_map(dict_file)

    files = os.listdir(dir_path)
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        out_file_path = os.path.join("./tmp/", file_name)
        update_file(dict_kv, file_path, out_file_path)


if __name__ == "__main__":
    update_dir_file("time.log", "src")
