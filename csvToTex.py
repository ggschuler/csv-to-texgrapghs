import pandas as pd
import matplotlib.pyplot as plt
import glob
import argparse

from soupsieve import match

plt.style.use('seaborn-white')
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = ['serif']

parser = argparse.ArgumentParser(description='Accepts .csv files and returns basic LaTex template with generated graphs.')

parser.add_argument(
  "-fp",
  "--filepath",
  required = True, 
  type     = str,
  nargs    = '+',
  dest     = "csvFiles",
  help     = "[REQUIRED] relative path to .csv file(s) to be read",
)

parser.add_argument(
  "-d",
  "--directory",
  action = "store_true",
  dest   = "readFromDir",
  help   = "[DIRNAME/*] if specified, filepath will be read as directory and all elements will be read"
)

parser.add_argument(
  "-s",
  "--xyscale",
  dest    = "xyscale",
  default = "axis",
  choices = ["axis", "semilogyaxis", "semilogxaxis", "loglogaxis"],
  help    = "sets the scale for xy-axis on generated graph"
)

parser.add_argument(
  "-n",
  "--newfile",
  action = "store_true",
  dest   = "newfile",
  help   = "creates new file, with header/outro"
)

args = parser.parse_args()

def GenerateGraph(path):
  df = pd.read_csv(path, sep=';',header=None,index_col=0)
  df.index.name = "entrada"
  df.columns = ["op."]
  fig, ax = plt.subplots()
  ax.set_yscale(args.yscale)
  ax.set_xscale(args.xscale)
  ax.plot(df, linestyle='--', marker='+', color='red')
  ax.grid()
  ax.set(xlabel='Valor de entrada', ylabel='N° de operações',title=path[14:-4])

def GenerateTexFigure(path):
  df = pd.read_csv(path, sep=';',header=None)
  path = path.replace('_','-')
  tuples = [tuple(row) for row in df.values]
  coord = ''.join(str(tuples))[1:-1].replace("), ",")")
  file.write(latexFig.format(tikzpicture='tikzpicture',
                      axis=args.xyscale,
                      TITLE=path,
                      COORDINATES=coord))

latexFig = open('resources/latexFig.txt', 'r')
latexFig = latexFig.read()

if(args.newfile): 
  latexHeader = open('resources/latexHeader.txt')
  latexHeader = latexHeader.read()
  latexOutro = '\n\end{document}'
else:
  latexHeader = ''
  latexOutro = ''

file = open("generatedTex.tex", "w")
file.write(latexHeader)

if (not args.readFromDir):
  for path in args.csvFiles:
    #GenerateGraph(path)
    print("PATH: " + path)
    GenerateTexFigure(path)
else:
  for path in sorted(glob.glob(args.csvFiles[0])):
    print("PATH: " + path)
    GenerateTexFigure(path)

file.write(latexOutro)
file.close()