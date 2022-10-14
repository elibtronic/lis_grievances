import pandas as pd
import datetime
#import matplotlib
import numpy as np
import csv
import matplotlib.pyplot as plt
from settings import *


'''
Spits out grief index by months, no time specified, is all time
'''
def grief_index(df, s_date="",e_date=""):
    if s_date == "":
        n = df.loc[df['status'] =='?']['status'].count()
        d = df.loc[df['status'] =='X']['status'].count() + df.loc[df['status'] =='?']['status'].count()

    else:

        s = s_date.split("/")
        e = e_date.split("/")

        start_date = pd.Timestamp(int(s[2]), int(s[0]), int(s[1]), 12)
        end_date = pd.Timestamp(int(e[2]), int(e[0]), int(e[1]), 12)

        t_window = df[(df['lisg'] >= start_date) & (df['lisg'] <= end_date)]

        n = t_window.loc[t_window["status"] == "?"]["status"].count()
        d = t_window.loc[t_window["status"] == "X"]["status"].count() + t_window.loc[t_window["status"] =="?"]["status"].count()

        #print(t_window)
        #print(n,d)

    #Actual Grief Index calculated below
    gi = round((n / (n+d)) * 100,4)

    return gi


def grief_to_file():
    gatfile = open("html/alltime.txt","w")
    gatfile.write(str(grief_index(df)))
    gatfile.close()


def grief_series(df):

    grief_s = {}

    this_month = datetime.datetime.now().month
    this_year = datetime.datetime.now().year

    last_day = {

        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    #partial 2016
    for y in range(2016,2017):
        for m in range(2,13):

            start_d = str(m)+"/1/"+str(y)
            end_d = str(m)+"/"+str(last_day[m])+"/"+str(y)
            #print(start_d,"-",end_d,"-",grief_index(df,start_d,end_d))
            grief_s[start_d] = grief_index(df,start_d,end_d)

    #full years
    for y in range(2017,datetime.datetime.now().year):
        for m in range(1,13):

            start_d = str(m)+"/1/"+str(y)
            end_d = str(m)+"/"+str(last_day[m])+"/"+str(y)
            #print(start_d,"-",end_d,"-",grief_index(df,start_d,end_d))
            grief_s[start_d] = grief_index(df,start_d,end_d)

    #current year
    for y in range(datetime.datetime.now().year,datetime.datetime.now().year+1):
        for m in range(1,13):
            if m < datetime.datetime.now().month:
                start_d = str(m)+"/1/"+str(y)
                end_d = str(m)+"/"+str(last_day[m])+"/"+str(y)
                #print(start_d,"-",end_d,"-",grief_index(df,start_d,end_d))
                grief_s[start_d] = grief_index(df,start_d,end_d)

    (pd.DataFrame.from_dict(data=grief_s, orient='index').to_csv('html/grief_series.csv', header=False))


    return

def gen_viz():

    #time series
    ts = []

    #list of monthly GI scores
    ds = []

    with open("html/grief_series.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            ts.append(row[0])
            ds.append(float(row[1]))

    total_gi = float(open("html/alltime.txt","r").readline())

    #overall GI score
    t_gi_s = [total_gi] * len(ts)


    #chart params
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(211)
    ax.plot(ts,ds)
    ax.plot(t_gi_s)
    ax.legend(["Monthly","Overall"])
    ax.set_title("THE GRIEF INDEX")
    ax.set_xlabel('month')
    ax.set_ylabel('grief index')
    ax.set_xticks(np.arange(0,len(ts)+1,3))
    plt.xticks(rotation = 45)
    plt.savefig('html/grief_index.png')
    #plt.show()


if __name__ == "__main__":
    df = pd.read_csv(CSV_DATA)
    df['lisg'] = pd.to_datetime(df['lisg'])
    grief_to_file()
    grief_series(df)
    gen_viz()


    