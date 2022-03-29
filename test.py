import random
import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics

df=pd.read_csv("data.csv")
height_list=df["Height"].to_list()
weight_list=df["Weight"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)


print("_mean,heightMean,Median,Mode of height is {},{} and {} respectivly".format(height_median,height_mode))
print("Mean,Median,Mode of weight is {},{} and {} respectivly".format(weight_mean,weight_median,weight_mode))

height_std=statistics.stdev(height_list)
weight_std=statistics.stdev(weight_list)

print("Height Standard Deviation  and Weight Standard Deviation {} and {} repectivly".format(height_std,weight_std))

