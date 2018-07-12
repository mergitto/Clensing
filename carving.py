import linecache
import random
import sys

random.seed(42)
filename = sys.argv[1]
save_file = sys.argv[2]
LIMIT_BYTES = 100000000 # 100,000,000B = 100,000KB = 100MB


def get_byte_num(s):
    return len(s.encode('utf-8'))


if __name__ == '__main__':
    num_lines = sum(1 for line in open(filename))
    print(num_lines)
    indices = list(range(num_lines))
    print(indices)
    random.shuffle(indices)

    with open(save_file, 'w') as f:
        count_byte = 0
        for i in indices:
            print('{} bytes'.format(count_byte))
            text = linecache.getline(filename, i)
            f.write(text)
            count_byte += get_byte_num(text)
            if count_byte >= LIMIT_BYTES:
                break

