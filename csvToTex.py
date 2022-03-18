import pandas as pd
import matplotlib.pyplot as plt
import glob
import argparse

plt.style.use('seaborn-white')
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = ['serif']

parser = argparse.ArgumentParser(description='Accepts .csv files and returns basic LaTex template with generated graphs.')
parser.add_argument(
  "-f",
  "--filepath",
  required = True, 
  type     = str,
  nargs    = '+',
  dest     = 'csvFiles',
  help     = '[REQUIRED] relative path to .csv file(s) to be read',
)
args = parser.parse_args()

def GenerateGraph(path):
  df = pd.read_csv(path, sep=';',header=None,index_col=0)
  df.index.name = "entrada"
  df.columns = ["op."]
  fig, ax = plt.subplots()
  ax.set_yscale("linear")
  ax.set_xscale("linear")
  ax.plot(df, linestyle='--', marker='+', color='red')
  ax.grid()
  ax.set(xlabel='Valor de entrada', ylabel='N° de operações',title=path[14:-4])

def GenerateTexFigure(path):
  df = pd.read_csv(path, sep=';',header=None)
  path = path.replace('_','-')
  tuples = [tuple(row) for row in df.values]
  coord = ''.join(str(tuples))[1:-1].replace("), ",")")
  file.write(latexFig.format(tikzpicture='tikzpicture',
                      axis='axis',
                      TITLE=path[14:-4],
                      COORDINATES=coord))

latexFig = open('resources/latexFig.txt', 'r')
latexFig = latexFig.read()
latexHeader = open('resources/latexHeader.txt')
latexHeader = latexHeader.read()
latexOutro = '\n\end{document}'

file = open("generatedTex.tex", "w")
file.write(latexHeader)

for path in args.csvFiles:
  #GenerateGraph(path)
  print("PATH: " + path)
  GenerateTexFigure(path)

file.write(latexOutro)
file.close()