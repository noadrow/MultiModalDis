import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.signal import find_peaks
import pandas as pd
import matplotlib.pyplot as plt
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

def KDE(data):

  kde = KernelDensity(bandwidth=0.05)
  kde.fit(data.reshape(-1, 1))
  densities = np.exp(kde.score_samples(data.reshape(-1, 1)))
  plt.plot(data, densities)
  return densities

def call_peaks(densities):

  # After generating densities...
  peaks, _ = find_peaks(densities, prominence=0.1)  # Adjust prominence as needed
  return len(peaks)

INPUT_FILE = loading_file_path("pick a pickle")
df = pd.read_pickle(INPUT_FILE)
# df.set_index(df.columns[0],inplace=True)
# df = df.drop(columns=['Unnamed: 0'])
path = loading_file_path("choose a cg list")
cg_list = pd.read_csv(path).values
results = []
cgs = []
for cg in cg_list:
    data = np.array(df.loc[cg[0]].sort_values())
    res = call_peaks(KDE(data))
    if(res>1):
        cgs.append(cg[0])
        results.append(res)

import os
result_df = pd.DataFrame({"cg":cgs,'peaks':results})

file_name = os.path.basename(INPUT_FILE).split(".")[0]

OUTPUT_FILE = os.path.join(os.path.dirname(INPUT_FILE),f"KDE_{file_name}.csv")

result_df.to_csv(OUTPUT_FILE)

OUTPUT_FILE = os.path.join(os.path.dirname(INPUT_FILE),f"KDE_{file_name}.txt")

f = open(OUTPUT_FILE,"x")
f.write("\n".join(cgs))
f.close()