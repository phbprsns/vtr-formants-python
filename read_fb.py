import numpy as np
import pandas as pd

'''

THE ORIGINAL MATLAB CODE

    fid=fopen(FMTFILE, 'r', 'b');
    n_frame=fread(fid, 1, 'int32');
    samPeriod=fread(fid, 1, 'int32');
    sampSize=fread(fid, 1, 'int16');
    numComps=sampSize/4; 			 
    fileType=fread(fid, 1, 'int16');  
    dataSet=zeros(n_frame,numComps);
    for n = 1:n_frame
       a=fread(fid, numComps, 'float');  
       dataSet(n,:)=a';
    end
    fclose(fid);

Useful documentation links for both MATLAB and Python

https://www.mathworks.com/help/matlab/ref/fopen.html
https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html
https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing

'''

def read_fb(FMTFILE: str, verbose=False) -> pd.DataFrame:

    with open(FMTFILE, 'rb') as fid:
        n_frame = np.fromfile(fid, dtype='>i4', count=1)[0] # datatype is big-endian 32-bit signed integer
        samPeriod=np.fromfile(fid, dtype='>i4', count=1)[0] # datatype is big-endian 32-bit signed integer
        sampSize= np.fromfile(fid, dtype='>i2', count=1)[0] # datatype is big-endian 16-bit signed integer
        fileType= np.fromfile(fid, dtype='>i2', count=1)[0] # datatype is big-endian 16-bit signed integer
        
        numComps=sampSize//4
        
        dataSet=np.zeros((n_frame,numComps))
        if verbose:
            print('n_frame', n_frame)
            print('sampSize', sampSize)
            print('numComps', numComps)
            print(dataSet.shape)
            
        for n in range(n_frame):
            try:
                a=np.fromfile(fid, dtype='>f', count=numComps) # datatype is big-endian float
                dataSet[n,:] = a
            except Exception as expt:
                print(n)
                print(expt)
                break
    fb = pd.DataFrame(dataSet, columns=['F1', 'F2', 'F3', 'F4', 'B1', 'B2', 'B3', 'B4'])
    fb['ms'] = [5 + i*10 for i in range(len(fb))]
    fb['sec'] = fb['ms'] / 1000
    return fb

if __name__ == '__main__':
    FMTFILE = '../VTRFormants/Train/dr1/fcjf0/si1027.fb'
    dataset = read_fb(FMTFILE)
    dataset.to_csv('../VTRFormants/csv/si1027.csv', index=False)
