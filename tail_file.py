# coding=UTF-8

def tail(input_file, output_file, skip_line):
    in_file = open(input_file, 'r')
    out_file = open(output_file, "w")

    read_line = 0
    for line in in_file:
        if read_line <= skip_line:
            read_line += 1
            continue

        out_file.writelines(line)

if __name__ == "__main__":
    input_file = "in"
    output_file = "out.out"
    tail(input_file, output_file, skip_line)
