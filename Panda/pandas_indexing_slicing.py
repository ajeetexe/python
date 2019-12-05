from pandas import read_csv

df = read_csv('document/data.txt', header=None)
df.columns = ['Id', 'Name', 'City', 'State', 'Country']
df.set_index('Id', inplace=True)
df1 = df.loc['1':'2', 'Name':'State']
print(df1)
df2 = df.iloc[1:3, 1:]
# To add index
df2['Continent'] = df2.shape[0] * ['Asia']
print(df2)

# for Deleting
# df1 = df.drop('1',0)
# df1 = df.drop(df.index[0:3],0) deleting index
# df1 = df.drop(df.columns[0:3],0) deleting columns
# df1_t =df.T   To transpose
