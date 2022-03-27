from statszcw.stats import read_data_sets

from sys import argv

if __name__ == "__main__":
    z = read_data_sets(argv[1:])   # file read
    print("files",z)