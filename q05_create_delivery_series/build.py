# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_delivery_series():
    deliveries =(ipl_matches_array[:,11])
    deliveries_series = pd.Series(data=deliveries)
    return deliveries

print(create_delivery_series())


