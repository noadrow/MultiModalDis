# Description
A computational tool was developed to detect and characterize multi-modal distribution patterns in DNA methylation sites across the genome. The tool is designed to process Illumina methylation array data and identify CpG sites exhibiting bi-modal or tri-modal distributions of methylation values. The output provides a concise summary of these multi-modal sites for further analysis.

## Required 
1. python3
2. python packages: pandas, statsmodels, sklearn, scipy, matplotlib, numpy.

# Input
convert_to_pickle_with_gui - illumina beta table in a csv format.
lilifores - illumina beta table in a pickle format.
KDE - illumina beta table in a pickle format  and a list of CpGs id (output of lilifores).

# Example:
run script from command line 
``` bash
python convert_to_pickle_with_gui.py
```
choose csv table 
![image](https://github.com/noadrow/MultiModalDis/assets/105928017/9835007c-df85-4cff-bbd8-c342433c6399)
choose directory to save the result
![image](https://github.com/noadrow/MultiModalDis/assets/105928017/643839ad-5251-4691-a2de-004dd7895fc5)

``` bash
python lilifores.py
```
choose a pickle
![image](https://github.com/noadrow/MultiModalDis/assets/105928017/3219c6c2-4300-48f9-ba13-bcf12a4cadb3)
the result would be saved at the same location as the input file. 

``` bash
python KDE.py
```
choose a pickle
![image](https://github.com/noadrow/MultiModalDis/assets/105928017/3219c6c2-4300-48f9-ba13-bcf12a4cadb3)
choose a CpG list (lilifores.py output)
![image](https://github.com/noadrow/MultiModalDis/assets/105928017/f61ca4be-9c4e-4fab-989b-816c000ae51d)
results would be saved to the same lication as the input file.
the output contains a CpG list(.txt) and a table with number of peaks (.csv).

# Output:
The primary output is a table with two columns: 'CpG' containing the identifier for each multi-modal CpG site, and 'Distributions' indicating the number of modal distributions detected (e.g., 2 for bi-modal, 3 for tri-modal). This table allows researchers to quickly identify and focus on the subset of CpGs exhibiting complex methylation patterns across the samples.
