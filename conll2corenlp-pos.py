import sys,os
import fileinput

f1 = open("output_training.txt", "a")
sentence = []
train_sentence = []
doc = []

with open (sys.argv[1], "r") as f:
#with open ("talbanken-stanford-test.conll", "r") as f:
    for line in f:
        #print line
        tokenized = line.split("\t")
        print tokenized
        doc.append(tokenized[1] + "\t" + tokenized[4] + "\n")
        if len(doc) == 500:
            f1.write("".join(doc))
            doc = []
f1.close()