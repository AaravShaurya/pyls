import argparse

parser = argparse.ArgumentParser(
    prog= 'Argparser',
    description= 'test my understanding of argparse',
    epilog= 'Thats it')

parser.add_argument("firstone")
parser.add_argument('-f','--flag',
                    help ="Just a flag to raise",
                    action = 'store_true')
args = parser.parse_args()
print(args)

