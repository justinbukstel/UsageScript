import csv
# define the input and output file names
input_file_1 = "first.csv"
input_file_2 = "second.csv"
output_file = "changed_usage.csv"
# read the first input file and create a dictionary mapping the "account name" to the "usage score" and "DAST score"
account_to_score = {}
with open(input_file_1, "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        account_to_score[row["Account Name (SFDC)"]] = {"usage_score": row["Usage Score"], "dast_score": row["DAST Score"]}
# open the second input file and the output file
with open(input_file_2, "r") as infile, open(output_file, "w") as outfile:
    # create a CSV writer for the output file
    writer = csv.writer(outfile)
    # write the header row to the output file
    writer.writerow(["account name", "CSE", "usage score", "score difference", "DAST score", "DAST score difference"])
    # read each row of the second input file
    reader = csv.DictReader(infile)
    for row in reader:
        # get the "account name", "CSE", "usage score", and "DAST score" from the current row
        account_name = row["Account Name (SFDC)"]
        cse = row["CSE"]
        usage_score = row["Usage Score"]
        dast_score = row["DAST Score"]
        # if the "CSE" in the current row equals "Justin Bukstel" and the "account name" exists in the first input file and the "usage score" and "DAST score" in the current row are valid integer literals,
        # calculate the differences between the "usage scores" and "DAST scores" and write the "account name", "CSE", "usage score", "score difference", "DAST score", and "DAST score difference" to the output file
        if cse == "Justin Bukstel" and account_name in account_to_score:
            # check if usage_score is a valid integer literal and remove the percent sign if it exists
            if usage_score.endswith("%"):
                usage_score = usage_score[:-1]
            if usage_score.isdigit():
                usage_score = int(usage_score)
            else:
            # if usage_score is not a valid integer literal, skip this row
                continue
        # check if dast_score is a valid integer literal and remove the percent sign if it exists
            if dast_score.endswith("%"):
                dast_score = dast_score[:-1]
            if dast_score.isdigit():
                dast_score = int(dast_score)
            else:
                # if dast_score is not a valid integer literal, skip this row
                continue
            # check if account_to_score[row["account name"]]["usage_score"] is a valid integer literal and remove the percent sign if it exists
            if account_to_score[row["Account Name (SFDC)"]]["usage_score"].endswith("%"):
                account_to_score[row["Account Name (SFDC)"]]["usage_score"] = account_to_score[row["Account Name (SFDC)"]]["usage_score"][:-1]
            if account_to_score[row["Account Name (SFDC)"]]["usage_score"].isdigit():
                account_to_score[row["Account Name (SFDC)"]]["usage_score"] = int(account_to_score[row["Account Name (SFDC)"]]["usage_score"])
            else:
                # if account_to_score[row["account name"]]["usage_score"] is not a valid integer literal, skip this row
                continue
            # check if account_to_score[row["account name"]]["dast_score"] is a valid integer literal and remove the percent sign if it exists
            if account_to_score[row["Account Name (SFDC)"]]["dast_score"].endswith("%"):
                account_to_score[row["Account Name (SFDC)"]]["dast_score"] = account_to_score[row["Account Name (SFDC)"]]["dast_score"][:-1]
            if account_to_score[row["Account Name (SFDC)"]]["dast_score"].isdigit():
                account_to_score[row["Account Name (SFDC)"]]["dast_score"] = int(account_to_score[row["Account Name (SFDC)"]]["dast_score"])
            else:
                # if account_to_score[row["account name"]]["dast_score"] is not a valid integer literal, skip this row
                continue
            # calculate the differences between the "usage scores" and "DAST scores"
            score_difference = usage_score - account_to_score[row["Account Name (SFDC)"]]["usage_score"]
            dast_score_difference = dast_score - account_to_score[row["Account Name (SFDC)"]]["dast_score"]
            # write the "account name", "CSE", "usage score", "score difference", "DAST score", and "DAST score difference" to the output file
            writer.writerow([account_name, cse, usage_score, score_difference, dast_score, dast_score_difference])
