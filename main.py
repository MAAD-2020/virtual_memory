import sys
from algoriphm_application import step_of_alg, alg_ap
sys.stdout = open("slovo_and_alg.out", "w")
file_in = open("slovo_and_alg.in")
file_out = open("slowo_and_alg.out", "w")
strings_of_file = file_in.read().rstrip().split("\n")
word_of_alg = strings_of_file[0]
strings_of_alg = strings_of_file[1:]
strings_of_alg = [command.split() for command in strings_of_alg]
print(alg_ap(word_of_alg, strings_of_alg))