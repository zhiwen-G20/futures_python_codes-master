import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import random
import matplotlib.dates as mdates

'''
尝试多种图，比如contour, hist2d. 

'''




def plotcontourTest():
    step = 1
    x = np.arange(-10,10,step)
    y = np.arange(-5,15,step)

    X,Y = np.meshgrid(x,y)
    Z = X**2 + Y**2

    plt.figure(figsize=(10,6))
    plt.contourf(X,Y,Z)
    plt.contour(X,Y,Z)
    plt.xlabel('X/m')
    plt.ylabel('Y/m')

    plt.show()




def plot5levelrawdata(data,model=0):
    '''
    根据行情文件，画出三维的5挡行情图
    :param data: dataframe, 每日行情数据
    :param model: 画图的一些选项
    :return:
    '''
    nRows = data.shape[0]
    nCols = data.shape[1]
    bidPrices = np.array(data.loc[:,['BidPrice1','BidPrice2','BidPrice3','BidPrice4','BidPrice5']])
    askPrices = np.array(data.loc[:,['AskPrice1','AskPrice2','AskPrice3','AskPrice4','AskPrice5']])
    bidVolumes = np.array(data.loc[:,['BidVolume1','BidVolume2','BidVolume3','BidVolume4','BidVolume5']])
    askVolumes = np.array(data.loc[:,['AskVolume1', 'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5']])
    lastPrice = np.expand_dims(np.array(data.loc[:,'LastPrice']),axis=1)
    lastVolume = np.expand_dims(np.array(data.loc[:,'Volume']),axis=1)
    time = np.arange(0,nRows)
    # MinVol, MaxVol =
    X = time.repeat(11).reshape(nRows,11).T
    Y = np.concatenate((bidPrices,lastPrice,askPrices),axis=1).T
    Z = np.concatenate((bidVolumes,lastVolume*0,askVolumes),axis=1).T





    fig = plt.figure()
    plt.contourf(X, Y, Z)
    plt.contour(X,Y,Z)
    cb = plt.colorbar()
    cb.set_label('volume')
    plt.show()

    return
    # generate random numbers
    Query_times1 = range(0, 50)
    Query_times2 = range(0, 30)
    list_random1 = random.sample(Query_times1, 25)
    list_random2 = random.sample(Query_times2, 25)
    mpl.rcParams['font.size'] = 8

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    xs = np.arange(1, 26)
    ys = list_random1
    ys2 = list_random2
    ys3 = list_random1
    ys4 = list_random2
    ys5 = list_random1
    ys6 = list_random2
    ys7 = list_random1
    ys8 = list_random2
    z1 = 3
    total_width, n = 0.8, 2
    width = total_width / n
    color = plt.cm.Set2((np.arange(plt.cm.Set2.N)))
    p1 = ax.bar(xs, ys, z1, zdir='y', color='#FF0080', alpha=0.8, width=width, label='h=3,DA')
    p2 = ax.bar(xs + width, ys2, z1, zdir='y', color='CYAN', alpha=0.8, width=width, label='h=3,DGA')

    z2 = 4
    total_width, n = 0.8, 2
    width = total_width / n
    color = plt.cm.Set2((np.arange(plt.cm.Set2.N)))
    p3 = ax.bar(xs, ys3, z2, zdir='y', color='b', alpha=0.8, width=width, label='h=4,DA')
    p4 = ax.bar(xs + width, ys4, z2, zdir='y', color='#9AFF02', alpha=0.8, width=width, label='h=4,DGA')

    z3 = 5
    total_width, n = 0.8, 2
    width = total_width / n
    color = plt.cm.Set2((np.arange(plt.cm.Set2.N)))
    p5 = ax.bar(xs, ys5, z3, zdir='y', color='#FF8000', alpha=0.8, width=width, label='h=5,DA')
    p6 = ax.bar(xs + width, ys6, z3, zdir='y', color='violet', alpha=0.8, width=width, label='h=5,DGA')

    z4 = 6
    total_width, n = 0.8, 2
    width = total_width / n
    color = plt.cm.Set2((np.arange(plt.cm.Set2.N)))
    p7 = ax.bar(xs, ys7, z4, zdir='y', color='r', alpha=0.8, width=width, label='h=6,DA')
    p8 = ax.bar(xs + width, ys8, z4, zdir='y', color='#0072E3', alpha=0.8, width=width, label='h=6,DGA')

    # ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
    # ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))

    ax.set_xlabel('k-')
    ax.set_ylabel('Spatial hierarchy (h)')
    ax.set_zlabel('Count')
    # plt.legend(loc='upper left')
    # plt.legend(loc='upper left', bbox_to_anchor=(0.0,0.6),ncol=1,fancybox=True,shadow=False)#Control the position of the legend
    plt.show()



