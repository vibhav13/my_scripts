import sys
import os
import csv
import argparse


def is_valid_file(parser, file_name):
    if not os.path.exists(file_name):
        parser.error("The file does not exist!")
        sys.exit(1)


def is_valid_csv(parser, file_name, row_limit):
    row_count = 0
    for row in csv.reader(open(file_name)):
        row_count += 1
    # Note: You could also use a generator expression
    # and the sum() function to count the rows:
    # row_count = sum(1 for row in csv.reader(open(file_name)))
    if row_limit > row_count:
        parser.error(
            "The row count does not match"
        )
        sys.exit(1)


def parse_file(arguments):
    input_file = arguments[0]
    output_file = arguments[1]
    row_limit = arguments[2]
    output_path = '.'  
    
    with open(input_file, 'r') as input_csv:
        datareader = csv.reader(input_csv)
        all_rows = []
        for row in datareader:
            all_rows.append(row)

        current_chunk = 1
        for i in range(0, len(all_rows), row_limit):  
            chunk = all_rows[i:i + row_limit]  

            current_output = os.path.join(  
                output_path,
                "{}-{}.csv".format(output_file, current_chunk)
            )

            chunk.insert(0, header)

            with open(current_output, 'w') as output_csv:
                writer = csv.writer(output_csv)
                writer = writer.writerows(chunk)

            print("Chunk # {}:".format(current_chunk))
            print("Filepath: {}".format(current_output))
            print("nimber of rows: {}".format(len(chunk)))

            # Create new chunk
            current_chunk += 1


if __name__ == "__main__":
    arguments = get_arguments()
    parse_file(arguments)
