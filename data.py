import pandas as pd
import statistics as st
import plotly_express as pe
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random


data = pd.read_csv("data.csv")

fig = pe.scatter(data, y ="quant_saved" , color = "rem_any")

fig.show()

with open("data.csv") as f:
    reader = csv.reader(f)
    savingsData = list(reader)

savingsData.pop(0)


total_entries= len(savingsData)

reminded = 0

for i in savingsData:
    if int(i[3]) == 1:
        reminded += 1


not_reminded = total_entries - reminded

fig = go.Figure(go.Bar(x=["reminded" , "not reminded"] , y = [reminded , not_reminded]))
# fig.show()

# ---------------------- mean/median/mode/stdev of the quanty saved by everyonr -------------------------------------

allSavings = []

for i in savingsData:
    allSavings.append(float(i[0]))

mean = st.mean(allSavings)
median = st.median(allSavings)
mode = st.mode(allSavings)
stdev = st.stdev(allSavings)

print("-------------------------")
print("Mean : " , mean)
print("Mode : " , mode)
print("Median : " , median)
print("Std dev : " , stdev)


# ---------------------- mean/median/mode/stdev of the quanty saved by those who were reminded -------------------------------------

reminded_savings = []

not_reminded_savings = []

for i in savingsData:
    if int(i[3]) == 1:
        reminded_savings.append(float(i[0]))
    else:
        not_reminded_savings.append(float(i[0]))


print("-------------------------------------------------------------------")
print("Mean of the quanty saved by those who were reminded : " , st.mean(reminded_savings))
print("Mode of the quanty saved by those who were reminded : " , st.mode(reminded_savings))
print("Median of the quanty saved by those who were reminded : " , st.median(reminded_savings))
print("Std dev of the quanty saved by those who were reminded : " , st.stdev(reminded_savings))


print("-------------------------------------------------------------------")
print("Mean of the quanty saved by those who were not reminded : " , st.mean(not_reminded_savings))
print("Mode of the quanty saved by those who were not reminded : " , st.mode(not_reminded_savings))
print("Median of the quanty saved by those who were not reminded : " , st.median(not_reminded_savings))
print("Std dev of the quanty saved by those who were not reminded : " , st.stdev(not_reminded_savings))


# --------------------------------- Data Story 2 =---------------------------------------------------

graph = ff.create_distplot([data["quant_saved"].tolist()] , ["Savings"] , show_hist = False)
# graph.show()


# -------------------- Interquartile Range ----------------------

q1 = data["quant_saved"].quantile(0.25)
q3 = data["quant_saved"].quantile(0.75)

iqr = q3-q1

print("Q1 : " , q1)
print("Q2 : " , q3 )

print("IQR : " , iqr)

lowerWhisker = q1 - (1.5*iqr)
upperWhisker = q3 + (1.5*iqr)

print("lower whisker: " , lowerWhisker)

print("Upper whisker: " , upperWhisker)

newData = data[data["quant_saved"] < upperWhisker]

newAllSavings = newData["quant_saved"].tolist()

print("-------------------------------------------------------------------")
print("Mean of the quanty saved by everyone in NEW DATA : " , st.mean(newAllSavings))
print("Mode of the quanty saved by everyone in NEW DATA : " , st.mode(newAllSavings))
print("Median of the quanty saved by everyone in NEW DATA : " , st.median(newAllSavings))
print("Std dev of the quanty saved by everyone in NEW DATA : " , st.stdev(newAllSavings))


graph = ff.create_distplot([newData["quant_saved"].tolist()] , ["Savings"] , show_hist = False)
graph.show()


sample_meanlist = []

for i in range(1000):
    sample = []
    
    for i in range(100):
        sample.append(random.choice(newAllSavings))
    
    sample_meanlist.append(st.mean(sample))

meanOfSample = st.mean(sample_meanlist)
stdevOfSample = st.stdev(sample_meanlist)

print("------------------------------------------")
print("Mean of the sample : " , meanOfSample)
print("Stdev of the sample : " , stdevOfSample)

graph = ff.create_distplot([sample_meanlist] ,["sample of saving data"], show_hist = False)

graph.show()