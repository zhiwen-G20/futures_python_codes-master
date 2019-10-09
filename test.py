import  pandas as np
import numpy as np
import  sys
from toolkit.datapreprocessing.dataloading import getrawdatafromcsvfile, computeTickPriceFromRawData
from toolkit.datashow.rawdatashow import plot5levelrawdata
from toolkit.datashow.rawdatashow import plotcontourTest

# filefullpath = "../maininsts/sn/sn0000/20190919Tgsn200120190919.csv"
filefullpath = "H:/UsefulInfo/Futures/DataCentre/FiveLevelTickData/maininsts/sn/sn0000/20190805Tgsn190920190805.csv"

rawdata = getrawdatafromcsvfile(filefullpath, 5)
tickPrice = computeTickPriceFromRawData(rawdata)
plot5levelrawdata(rawdata, '21:00:00', 200000)
# plotcontourTest()

print(rawdata.head(5))