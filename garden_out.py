import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.signal import find_peaks
import pandas as pd
import matplotlib.pyplot as plt
import os


folder_path = 'C:/Users/noadr/Documents/blood_methylation/indi_jump/RA_beta_diff'

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

path = loading_file_path("pick a pickle")
df = pd.read_pickle(path)
path = loading_file_path("pick a tp table")
df_tp = pd.read_csv(path)
df.set_index(df.columns[0], inplace=True)
cgs = []
res_peak = []
res = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    df_cgs = pd.read_csv(file_path)
    cg_list = df_cgs.columns[1:]

    for cg in cg_list:
        series = df.loc[cg]
        tps1 = df_tp.iloc[:,0].values.tolist()
        data = series[tps1]
        #indices_ending_with_dot1 = series.index[series.index.str.endswith('.1')]
        #filtered_series = series[indices_ending_with_dot1]
        #data = np.array(filtered_series.sort_values())
        tp2 = df_cgs[cg].iloc[1]
        tp2 = np.array(tp2,dtype="float64")
        if tp2 > max(data) or tp2 < min(data):
            res.append(0)
            cgs.append(cg)
        else:
            res.append(1)
            cgs.append(cg)


result_df = pd.DataFrame.from_dict({"cg":cgs,"res":res})
result_df.to_csv(f'on_which_peak_res.csv')
