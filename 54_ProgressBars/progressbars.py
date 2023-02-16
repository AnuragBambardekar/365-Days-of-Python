from joblib import Parallel, delayed
import math
import time
from tqdm import tqdm

results = []

results = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in tqdm(range(25000)))