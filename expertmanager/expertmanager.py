# This script takes user input and triages the query to one of two or
# more dapp agents on the iExec cloud.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_words', metavar='N', type=str, nargs='+')
input = parser.parse_args()
input_string = ' '.join(input.input_words)

# Pseudocode
if input_string == 'En que piensa Cervantes?':
    print('calling Cervantes')
#   then iexec submit 'python3 /examples/nlp/dime_algo.py' --dapp 0x25412143e4c5392dea108c2834008985507410f2
#   else: input goes to tinychat iexec submit 'python oneturn.py %inputstring --dapp 0x2e785496d4f66BF1e2dDFba1a7755eb2EbF75d2C</p>
else:
    print('Message sent to Athina tinychat')

