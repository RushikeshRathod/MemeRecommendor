l = ['adfasfd','how','are','you']
import  csv

with open("out.csv","a") as f:
    wr = csv.writer(f,delimiter=",")
    wr.writerow(l)