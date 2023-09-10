

import itertools
import threading
import time
import pandas as pd
import sys

def extract_data(source):
	return pd.read_csv(source,encoding='windows-1252')

def transform_data(data):
	df = data.copy()
	df[["Day","Month","Year"]] = df.Date.str.split("-", expand =True)
	df.dropna(inplace = True) 
	df.drop_duplicates(inplace = True)
	df.drop(columns = ["Target Status"], inplace =True)
	return df

def load_data(df_2, output):
	df_2.to_csv(output)



def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone! ')
    sys.stdout.flush()



if __name__ == "__main__":

	ll = sys.argv
	done = False
	t = threading.Thread(target=animate)
	t.start()
	#print(ll)

	data = extract_data(ll[1])
	new_data = transform_data(data)
	load_data(new_data,ll[2])

	time.sleep(1)
	done = True


