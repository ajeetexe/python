from pandas import read_excel, read_csv

df = read_excel("document/supermarkets.xlsx")
df1 = read_csv("document/supermarkets.csv")
print(f'{df} \n {df1}')
