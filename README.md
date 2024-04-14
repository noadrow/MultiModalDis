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


# Output:
The primary output is a table with two columns: 'CpG' containing the identifier for each multi-modal CpG site, and 'Distributions' indicating the number of modal distributions detected (e.g., 2 for bi-modal, 3 for tri-modal). This table allows researchers to quickly identify and focus on the subset of CpGs exhibiting complex methylation patterns across the samples.
