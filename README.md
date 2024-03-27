# CSV to TeX graphs.
Script for converting .csv data to .tex graph/figure templates. Script should be executed with optional paraments:

Optional arguments:
```
  -h,                                             --help      Show this help message and exit  
  -fp CSVFILES [CSVFILES ...],                    --filepath  CSVFILES [CSVFILES ...]  
                                                  [REQUIRED] relative path to .csv file(s) to be read  
  -d,                                             --directory, Filepath will be read as directory and all elements will be read
                                                  [DIRNAME/*] if specified
  -s,                                             --xyscale    Sets the scale for xy-axis on generated graph
{axis,semilogyaxis,semilogxaxis,loglogaxis}       {axis,semilogyaxis,semilogxaxis,loglogaxis}
                        
  -n,                                             --newfile    Creates new file, with header/outro
```
