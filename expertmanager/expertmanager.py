# This script takes user input and triages the query to one of two or
# more dapp agents on the iExec cloud.

import argparse
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument('input_words', metavar='N', type=str, nargs='+')
input = parser.parse_args()
input_string = ' '.join(input.input_words)

command1 = "iexec submit 'python3 /examples/nlp/dime_algo.py' --dapp 0x25412143e4c5392dea108c2834008985507410f2"
command1 = command1.split(' ')
command2 = "iexec submit 'python oneturn.py how are you' --dapp 0x2e785496d4f66BF1e2dDFba1a7755eb2EbF75d2C"
command2 = command2.split(' ')
# Pseudocode
if input_string == 'En que piensa Cervantes?':
    print('Raising Cervantes from his grave...')
    run(command1)
else:
    print('Waiting for Athina\'s response')
    run(command2)
