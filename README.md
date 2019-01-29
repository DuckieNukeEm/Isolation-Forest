# Isolation-Forest
Implemntation and Presentation on Isolation Forest

### Paper

The paper is titled 'Isolation Forest', written by:    
* Fei Tony Liu of the Gippsland School of Infomration Technology  
* Kai Ming Ting of the Giipsland School of Infomration Technology  
* Zhi-Hua Zhou  of the National Key Laboratoy for Novel Software Technology

Published in the Proceedings of the 8th IEEE International Conference on on Data Mining, pages 412-422, Pisa, Italy, 2008

You can find the paper here as *Isolation Forest.pdf*

### Presentation
The Presentation was presented on 2019-01-24 to the NWA data science meetup at 6pm.
The ending is super weak (I know) 

### iForest.ipynb

Ia Jupyter notebook where I test some of the properties of Isolation Forest. Works pretty well, but there are clear areas of improvement.
One being to take into account factor/categorical variables.
Another one being a Anomoly scores for Variables, which would indicate how lickly a variable is to generate an anomoly.


### iForest.py

A python implemention of the Isolation Forest. It works off pandas DataFrames.
