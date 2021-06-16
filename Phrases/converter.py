import copy
import csv

with open("sdtest.txt") as inputfile:
    with open("sdtestout.txt", mode='w') as csvout:
        csv_writer = csv.writer(csvout, delimiter = '\t')

        for line in inputfile:
            line = copy.copy(line).rstrip()
            elements = line.split(" .@")
            if elements[1] == "positive":
                elements[1] = 1
            elif elements[1] == "neutral":
                elements[1] = 0.5
            else:
                elements[1] = 0
            csv_writer.writerow(elements)
