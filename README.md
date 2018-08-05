# Latex Table Creator
Simple program that given a csv/ssv file returns the content ready to copy/paste in latex table format.

## Input
* --file: The csv/ssv file.
* --separator: The separator used in the file, by default the separator is ','.
* --format: The desired format for the cells, by default the format is all 'c'. 
* --columns: The desired columns in the file, by default takes all the columns.

## Output
The given input:
```  
  python latex_table_creator.py --file test_set.csv --format "|cccc|" > out.txt --columns 3,4,5,6
```
test_set.csv:
```
3,4,5,6
11,13,63,14
14,9,62,19
8,8,63,9
7,8,54,20
7,12,61,15
12,5,63,10
13,10,61,14
5,8,60,17
5,16,63,14 
5,7,66,12
13,11,94,23
12,10,52,17
10,12,69,16
8,11,53,17
11,10,59,18
7,8,66,12
```
Gives the following output:
```
\begin{table}[POSITION]
\begin{tabular}{|cccc|}
\hline
3&4&5&6 \\ \hline 
11&13&63&14 \\ \hline 
14&9&62&19 \\ \hline 
8&8&63&9 \\ \hline 
7&8&54&20 \\ \hline 
7&12&61&15 \\ \hline 
12&5&63&10 \\ \hline 
13&10&61&14 \\ \hline 
5&8&60&17 \\ \hline 
5&16&63&14 \\ \hline 
5&7&66&12 \\ \hline 
13&11&94&23 \\ \hline 
12&10&52&17 \\ \hline 
10&12&69&16 \\ \hline 
8&11&53&17 \\ \hline 
11&10&59&18 \\ \hline 
7&8&66&12 \\ \hline

\\
\end{tabular}
\caption{A CAPTION} \label{tab:A LABEL}
\end{table}
```
## Built With
[Python](https://www.python.org/) - Primary Language.

## Authors
* **Jordi Ricard Onrubia Palacios** - *Programming* - [JordiROP](https://github.com/JordiROP)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
