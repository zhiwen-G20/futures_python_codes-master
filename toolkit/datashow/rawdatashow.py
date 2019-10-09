import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from toolkit.datapreprocessing.dataloading import computeTickPriceFromRawData
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
    x = np.arange(-10, 10, step)
    y = np.arange(-5, 15, step)

    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2

    plt.figure(figsize=(10, 6))
    plt.contourf(X, Y, Z)
    plt.contour(X, Y, Z)
    plt.xlabel('X/m')
    plt.ylabel('Y/m')

    plt.show()


def timestr2seconds(timestr):
    '''
    将单个时间字符串转化为s为段位的整形
    :param timestr: 如：‘09:00:02’
    :return:  如：ret = 09*3600+ 00*60 + 02
    '''
    hh, mm, ss = int(timestr[:2]), int(timestr[3:5]), int(timestr[6:8])
    totsec = hh * 3600 + mm * 60 + ss
    return totsec


def plot5levelrawdata_contour(data, starttime='21:00:21', lastSeconds=10):
    '''
    根据行情文件，画出三维的5挡行情图
    :param data: dataframe, 每日行情数据
    :param model: 画图的一些选项
    :return:
    '''

    # 计算tickPrice
    tickPrice = computeTickPriceFromRawData(data)

    # 计算起止时间和索引值
    lastTime = data['m_lasttime']
    startSeconds = timestr2seconds(starttime)
    endSeconds = startSeconds + lastSeconds

    startIndex = (lastTime - startSeconds).abs().idxmin()
    endIndex = (lastTime - endSeconds).abs().idxmin()

    indices = np.arange(startIndex, endIndex)

    # 获取相应的价格和委托量
    bidPrices = np.array(data.loc[indices, ['BidPrice1', 'BidPrice2', 'BidPrice3', 'BidPrice4', 'BidPrice5']])
    askPrices = np.array(data.loc[indices, ['AskPrice1', 'AskPrice2', 'AskPrice3', 'AskPrice4', 'AskPrice5']])
    bidVolumes = np.array(data.loc[indices, ['BidVolume1', 'BidVolume2', 'BidVolume3', 'BidVolume4', 'BidVolume5']])
    askVolumes = np.array(data.loc[indices, ['AskVolume1', 'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5']])
    lastPrice = np.expand_dims(np.array(data.loc[indices, 'LastPrice']), axis=1)
    # lastVolume = np.expand_dims(np.array(data.loc[indices, 'Volume']), axis=1)

    # 先画出买价委托
    last_xpos = indices
    last_ypos = lastPrice.squeeze()

    fig = plt.figure()
    xx = indices.repeat(5).reshape(-1, 5)
    yy = askPrices.reshape(-1, 5)
    zz = askVolumes.reshape(-1, 5)
    bid_yy = bidPrices.reshape(-1, 5)
    bid_zz = bidVolumes.reshape(-1, 5)

    volumes_seq = np.log(np.concatenate([zz,   bid_zz]).reshape(-1,1).squeeze())

    plt.hist(volumes_seq, 10)
    plt.show()
    return


    linenumber = 8
    a1 = plt.contourf(xx, yy, zz, linenumber, alpha=0.5, cmap=plt.cm.jet)
    b1 = plt.contour(xx, yy, zz, linenumber, colors='black', linewidths=0.1)
    a2 = plt.contourf(xx, bid_yy, bid_zz, linenumber, alpha=0.5, cmap=plt.cm.jet)
    b2 = plt.contour(xx, bid_yy, bid_zz, linenumber, colors='black', linewidths=0.1)

    plt.plot(last_xpos, last_ypos, color='y', linewidth=2, alpha=0.99)

    plt.colorbar(a1, ticks=[0, 0.25, 0.5, 0.75, 1])

    plt.show()
    return


def plot5levelrawdata_surface(data, starttime='21:00:21', lastSeconds=10):
    '''
    根据行情文件，画出三维的5挡行情图
    :param data: dataframe, 每日行情数据
    :param model: 画图的一些选项
    :return:
    '''

    # 计算tickPrice
    tickPrice = computeTickPriceFromRawData(data)

    # 计算起止时间和索引值
    lastTime = data['m_lasttime']
    startSeconds = timestr2seconds(starttime)
    endSeconds = startSeconds + lastSeconds

    startIndex = (lastTime - startSeconds).abs().idxmin()
    endIndex = (lastTime - endSeconds).abs().idxmin()

    indices = np.arange(startIndex, endIndex)

    # 获取相应的价格和委托量
    bidPrices = np.array(data.loc[indices, ['BidPrice1', 'BidPrice2', 'BidPrice3', 'BidPrice4', 'BidPrice5']])
    askPrices = np.array(data.loc[indices, ['AskPrice1', 'AskPrice2', 'AskPrice3', 'AskPrice4', 'AskPrice5']])
    bidVolumes = np.array(data.loc[indices, ['BidVolume1', 'BidVolume2', 'BidVolume3', 'BidVolume4', 'BidVolume5']])
    askVolumes = np.array(data.loc[indices, ['AskVolume1', 'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5']])
    lastPrice = np.expand_dims(np.array(data.loc[indices, 'LastPrice']), axis=1)
    # lastVolume = np.expand_dims(np.array(data.loc[indices, 'Volume']), axis=1)

    # 先画出买价委托
    last_xpos = indices
    last_ypos = lastPrice.squeeze()
    last_zpos = np.zeros_like(last_ypos)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xx = indices.repeat(5).reshape(-1, 5)
    yy = askPrices.reshape(-1, 5)
    zz = askVolumes.reshape(-1,5)
    bid_yy = bidPrices.reshape(-1, 5)
    bid_zz = bidVolumes.reshape(-1, 5)

    ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, cmap=plt.cm.jet, alpha=0.6)
    ax.plot_surface(xx, bid_yy, bid_zz, rstride=1, cstride=1, cmap=plt.cm.jet, alpha=0.6)
    ax.plot(last_xpos, last_ypos, last_zpos, color='y', linewidth=2, alpha=0.99)

    ax.set_xlabel('epoeches')
    ax.set_ylabel('prices')
    ax.set_zlabel('volumes')
    plt.show()
    return


def plot5levelrawdata_wireframe(data, starttime='21:00:21', lastSeconds=10):
    '''
    根据行情文件，画出三维的5挡行情图
    :param data: dataframe, 每日行情数据
    :param model: 画图的一些选项
    :return:
    '''

    # 计算tickPrice
    tickPrice = computeTickPriceFromRawData(data)

    # 计算起止时间和索引值
    lastTime = data['m_lasttime']
    startSeconds = timestr2seconds(starttime)
    endSeconds = startSeconds + lastSeconds

    startIndex = (lastTime - startSeconds).abs().idxmin()
    endIndex = (lastTime - endSeconds).abs().idxmin()

    indices = np.arange(startIndex, endIndex)

    # 获取相应的价格和委托量
    bidPrices = np.array(data.loc[indices, ['BidPrice1', 'BidPrice2', 'BidPrice3', 'BidPrice4', 'BidPrice5']])
    askPrices = np.array(data.loc[indices, ['AskPrice1', 'AskPrice2', 'AskPrice3', 'AskPrice4', 'AskPrice5']])
    bidVolumes = np.array(data.loc[indices, ['BidVolume1', 'BidVolume2', 'BidVolume3', 'BidVolume4', 'BidVolume5']])
    askVolumes = np.array(data.loc[indices, ['AskVolume1', 'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5']])
    lastPrice = np.expand_dims(np.array(data.loc[indices, 'LastPrice']), axis=1)
    # lastVolume = np.expand_dims(np.array(data.loc[indices, 'Volume']), axis=1)

    # 先画出买价委托
    last_xpos = indices
    last_ypos = lastPrice.squeeze()
    last_zpos = np.zeros_like(last_ypos)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xx = indices.repeat(5).reshape(-1, 5)
    yy = askPrices.reshape(-1, 5)
    zz = askVolumes.reshape(-1,5)
    bid_yy = bidPrices.reshape(-1, 5)
    bid_zz = bidVolumes.reshape(-1, 5)

    ax.plot_wireframe(xx, yy, zz, rstride=1, cstride=1, color='r', alpha=0.6)
    ax.plot_wireframe(xx, bid_yy, bid_zz, rstride=1, cstride=1, color='b', alpha=0.6)
    ax.plot(last_xpos, last_ypos, last_zpos, color='y', linewidth=2, alpha=0.99)

    ax.set_xlabel('epoeches')
    ax.set_ylabel('prices')
    ax.set_zlabel('volumes')
    plt.show()
    return

def plot5levelrawdata_bar3d(data, starttime='21:00:21', lastSeconds=10):
    '''
    根据行情文件，画出三维的5挡行情图
    :param data: dataframe, 每日行情数据
    :param model: 画图的一些选项
    :return:
    '''

    # 计算tickPrice
    tickPrice = computeTickPriceFromRawData(data)

    # 计算起止时间和索引值
    lastTime = data['m_lasttime']
    startSeconds = timestr2seconds(starttime)
    endSeconds = startSeconds + lastSeconds

    startIndex = (lastTime - startSeconds).abs().idxmin()
    endIndex = (lastTime - endSeconds).abs().idxmin()

    indices = np.arange(startIndex, endIndex)

    # 获取相应的价格和委托量
    bidPrices = np.array(data.loc[indices, ['BidPrice1', 'BidPrice2', 'BidPrice3', 'BidPrice4', 'BidPrice5']])
    askPrices = np.array(data.loc[indices, ['AskPrice1', 'AskPrice2', 'AskPrice3', 'AskPrice4', 'AskPrice5']])
    bidVolumes = np.array(data.loc[indices, ['BidVolume1', 'BidVolume2', 'BidVolume3', 'BidVolume4', 'BidVolume5']])
    askVolumes = np.array(data.loc[indices, ['AskVolume1', 'AskVolume2', 'AskVolume3', 'AskVolume4', 'AskVolume5']])
    lastPrice = np.expand_dims(np.array(data.loc[indices, 'LastPrice']), axis=1)
    # lastVolume = np.expand_dims(np.array(data.loc[indices, 'Volume']), axis=1)

    # 先画出买价委托
    xpos = indices.repeat(5)
    ypos = askPrices.reshape(1, -1).squeeze()
    zpos = np.zeros_like(ypos)
    dx = 0.3
    dy = 0.3 * tickPrice
    dz = askVolumes.reshape(1, -1).squeeze()

    bid_ypos = bidPrices.reshape(1, -1).squeeze()
    bid_dz = bidVolumes.reshape(1, -1).squeeze()

    last_xpos = indices
    last_ypos = lastPrice.squeeze()
    last_zpos = np.zeros_like(last_ypos)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r', alpha=0.6, zsort='average')
    ax.bar3d(xpos, bid_ypos, zpos, dx, dy, bid_dz, color='b', alpha=0.6, zsort='average')
    ax.plot(last_xpos, last_ypos, last_zpos, color='y', alpha=0.99)

    ax.set_xlabel('epoeches')
    ax.set_ylabel('prices')
    ax.set_zlabel('volumes')
    plt.show()

    return


"""

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

"""
