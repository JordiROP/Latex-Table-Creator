import argparse
import pandas as pd
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--format', default=None, type=str, help='cell format')
parser.add_argument('--file', type=str, help='csv/ssv file')
parser.add_argument('--separator', default=',', type=str, help='separator ","\
                    or " "')
parser.add_argument('--columns', default=None, type=str,
                    help='wanted columns')


def printer(format, columns, file_reader):
    print "\\begin{table}[POSITION]"
    print "\\begin{tabular}{" + format + "}"
    print file_reader.to_csv(sep='&', index=False,
                             line_terminator=" \\\ \hline \n")
    print "\\\\"
    print "\\end{tabular}"
    print "\\caption{A CAPTION} \label{tab:A LABEL}"
    print "\\end{table}"


def main(argv):
    args = parser.parse_args(argv[1:])
    delim = args.separator != ','
    columns = args.columns.split(',') if args.columns is not None else None
    print args.columns
    file_reader = pd.read_csv(args.file, delim_whitespace=delim,
                              usecols=columns)

    format = args.format if args.format is not None else \
        "".join(['c'] * 23)
    printer(format, args.columns, file_reader)


if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
