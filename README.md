# csv-to-texgrapghs
Script for converting .csv data to .tex graph/figure templates. Script should be executed with optional paraments:

optional arguments:
  -h, --help            show this help message and exit
  -fp CSVFILES [CSVFILES ...], --filepath CSVFILES [CSVFILES ...]
                        [REQUIRED] relative path to .csv file(s) to be read
  -d, --directory       [DIRNAME/*] if specified, filepath will be read as directory and all elements will be read
  -s {axis,semilogyaxis,semilogxaxis,loglogaxis}, --xyscale {axis,semilogyaxis,semilogxaxis,loglogaxis}
                        sets the scale for xy-axis on generated graph
  -n, --newfile         creates new file, with header/outro

