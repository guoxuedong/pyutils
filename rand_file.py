from random import Random

def random_str(randomlength = 8):
    string = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789#-_+='
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        string += chars[random.randint(0, length)]

    return string


def random_file(num = 1):
    for i in xrange(num): 
        rand_file = open('file%s.txt' % (i+ 1), 'w')

        for j in xrange(100):
            string = random_str(32)
            rand_file.write(string)
            rand_file.write('\n')

        rand_file.close()

if __name__ == "__main__":
    random_file(10)
    
