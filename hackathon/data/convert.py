
import numpy
import pandas
import glob, os
import tifffile

CALCIUMDATA = "/Users/Anthony/Desktop/CalciumData"

def main():

    files = glob.glob(os.path.join("annotations", "*.csv"))
    for file in files:
        basename = os.path.basename(file)
        streamname = basename.replace(".csv", ".tif").replace("manual_", "")
        streamname = os.path.join(CALCIUMDATA, streamname)
        
        if os.path.isfile(streamname):
            df = pandas.read_csv(file)
            stream = tifffile.imread(streamname)
            traces = []
            for idx, row, in df.iterrows():
                trace = stream[:, int(row["Y"]), int(row["X"])]
                traces.append(trace)
            traces = numpy.array(traces)
            
            numpy.save(os.path.join("traces", os.path.basename(streamname).replace(".tif", ".npy")), traces)

if __name__ == "__main__":

    main()
