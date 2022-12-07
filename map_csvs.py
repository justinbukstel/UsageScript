import csv
# define the input and output file names
input_file_1 = "input1.csv"
input_file_2 = "input2.csv"
output_file = "output.csv"
# read the first input file and create a dictionary mapping the "account name" to the "usage score"
account_to_score = {}
with open(input_file_1, encoding="utf8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        account_to_score[row["account name"]] = row["usage score"]
# open the second input file and the output file
with open(input_file_2, encoding="utf8") as infile, open(output_file, "w") as outfile:
    # create a CSV writer for the output file
    writer = csv.writer(outfile)
    # write the header row to the output file
    writer.writerow(["account name", "usage score"])
    # read each row of the second input file
    reader = csv.DictReader(infile)
    for row in reader:
        # get the "account name" and "usage score" from the current row
        account_name = row["account name"]
        usage_score = row["usage score"]
        # if the "usage score" in the current row is less than the value in the first input file,
        # write the "account name" and "usage score" to the output file
        if usage_score < account_to_score[account_name]:
            writer.writerow([account_name, usage_score])