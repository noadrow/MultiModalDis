import pandas as pd
from statsmodels.stats.diagnostic import lilliefors
from time import time
import os

def lilliefors_test_fast(df,name):
    results,cgs,satistics,stds = [], [], [],[]
    for cg in df.index:
        data = df.loc[cg].dropna()
        std = data.std()
        data = data.to_list()

        if bool(data):
            result = lilliefors(data)
            pass_val = False if ((result[0] < 0.1) or (std < 0.1)) else True

        else:
            pass_val = False

        # True for normal distribution

        if pass_val:
            results.append(cg)
            stds.append(std)
            satistics.append(result[0])
            cgs.append(cg)

    new_pd = pd.DataFrame({'cg': cgs, 'std': stds, 'satistics': satistics})

    return results
def loading_file_path():
    import sys
    if(len(sys.argv) > 1):
        INPUT_control = str(sys.argv[1])
    else:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        INPUT_control = askopenfilename(title='pick a pickle')

        return INPUT_control

def load_file_to_df(INPUT_control=""):
    if(INPUT_control == ''):
        print('no pickle has been chosen :(')

    df = pd.read_pickle(INPUT_control)
    # df.set_index(df.columns[0],inplace=True)
    # df.index = df['index']
    # df = df.drop(columns=['Unnamed: 0'])

    return df

# load data
INPUT_FILE=loading_file_path()
file_name = os.path.basename(INPUT_FILE).split(".")[0]

OUTPUT_FILE = os.path.join(os.path.dirname(INPUT_FILE),f"lilifores_{file_name}.txt")


print ("path loaded !!!")

df = load_file_to_df(INPUT_FILE)
print ("file data exported !!!")

all_probes_file = pd.DataFrame(df.index)
print ("cgs extracted !!!")

time_0 = time()
multimodals = lilliefors_test_fast(df,file_name)
TotalTime_1 = time()-time_0

time_0 = time()
f = open(OUTPUT_FILE,"x")
f.write("\n".join(multimodals))
f.close()
TotalTime_2 = time()-time_0

print(f"noam's csv re-formatting finished in: {TotalTime_2} sec")
print(f"saved to {OUTPUT_FILE}")
