import argparse
import pandas as pd
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--format', default=None, type=str, 
                    help='cell format')
parser.add_argument('--file', type=str, help='csv/ssv file', 
                    required=True)
parser.add_argument('--separator', default=',', type=str, 
                    help='csv separator"')
parser.add_argument('--columns', default=None, type=str,
                    help='list of wanted columns')
parser.add_argument('--position', default='h', type=str,
                    help='position of the table')
parser.add_argument('')

def printer(format, columns, file_reader):
    print "\\begin{table}[POSITION]"
    print "\\begin{tabular}{" + format + "}"
    print file_reader.to_csv(sep='&', index=False, 
                            line_terminator=" \\\\ \\hline \n")
    print "\\\\"
    print "\\end{tabular}"
    print "\\caption{A CAPTION} \\label{tab:A LABEL}"
    print "\\end{table}"


def main(argv):
    args = parser.parse_args(argv[1:])
    delim = args.separator != ','
    columns = args.columns.split(',') if args.columns is not None else None
    file_reader = pd.read_csv(args.file, delim_whitespace=delim,
                              usecols=columns)
    format = args.format if args.format is not None else \
        "".join(['c'] * len(file_reader.columns))
    printer(format, args.columns, file_reader)


if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
