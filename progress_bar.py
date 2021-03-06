# progress bar
from tqdm import tqdm
import time

for i in tqdm(range (101), desc="Downloading...", ascii=False, ncols=75):
    time.sleep(0.01)
print("Downloading Complete")