import pandas as pd
import re

def loading_file_path(file_type):
    import sys
    if(len(sys.argv) > 1):
        INPUT_control = str(sys.argv[1])
    else:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        INPUT_control = askopenfilename(title=file_type)

        return INPUT_control

def read_cgs(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file]
    return lines

def contains_cg(index_value, cgs):
    """
    Check if the index value starts with any string from the cgs list,
    followed by an underscore.
    """
    parts = index_value.split('_')
    if len(parts) > 0 and parts[0] in cgs:
        return True
    return False


INPUT_FILE = loading_file_path("pick a csv")
df = pd.read_csv(INPUT_FILE)
path = loading_file_path("Choose a cpg list")
cgs = read_cgs(path)
INPUT_FILE = loading_file_path("pick an illumina table")
illumina = pd.read_csv(INPUT_FILE)
illumina.set_index(illumina.columns[0],inplace=True)

INPUT_FILE = loading_file_path("pick a tp table")
df_tp = pd.read_csv(INPUT_FILE)

df.set_index(df.columns[0],inplace=True)
df_filt = df[df.index.isin(cgs)]



# Assuming 'df' and 'cgs' are already defined
df_filt = df[df.index.map(lambda x: contains_cg(x, cgs))]

#for sample in df_filt.T.index:
for sample in df_tp.index:
    #temp = df_filt.T[df_filt.T.index.str.contains(sample.split(".")[0], na=False)]
    tp1 = df_tp.loc[sample][0]
    tp2 = df_tp.loc[sample][1]
    temp = df_filt[[tp1,tp2]].T


    #pattren = sample.split("W")[0]
    #temp10 = df_filt.T[df_filt.T.index.isin([f"{pattren}W10"])]
    #temp0 = df_filt.T[df_filt.T.index.isin([f"{pattren}W0"])]
    #temp = pd.concat([temp0, temp10])

    df_diff = temp.diff()
    columns_with_large_diff = []

    for index, row in df_diff.iterrows():
        # Identify columns with a difference greater than 0.25
        # temp0 = df_filt.T[df_filt.T.index.isin([f"{pattren}W0"])]
        significant_columns = row[abs(row) > 0.25].index.tolist()
        if(not significant_columns == []):
            significant_df = pd.DataFrame(df_diff.iloc[1]).T
            significant_df.index = [f'{index}_diff']
            significant_df = significant_df[significant_columns]
            before_diff_df = temp[significant_columns]
            processed_columns = [id.split('_')[0] for id in significant_columns]
            illumina_series = illumina.loc[illumina.index.map(lambda x: contains_cg(x, processed_columns))]['UCSC_RefGene_Name']

            result_df = pd.concat([before_diff_df, significant_df])
            result_df.loc['genes'] = illumina_series
            result_df.to_csv(f'{index}.csv')



