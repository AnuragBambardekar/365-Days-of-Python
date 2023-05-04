import schedule
import time
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook():
    filename = '131_Schedule_Jupyter_notebook/test.ipynb'
    with open(filename) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
    
    ep = ExecutePreprocessor(timeout=None, kernel_name='python3')

    nb_out = ep.preprocess(nb_in)
    
    print("Done Execution")

schedule.every(24).hours.do(run_notebook)

while True:
    schedule.run_pending()
    time.sleep(1)
