from pandas import read_csv

# If csv file have no header then we set header as None

df = read_csv('document/data.txt', header=None)

# To Add Columns in dataframe we use this.
df.columns = ['Id', 'Name', 'City', 'State', 'Country']

# To set index we have to use another variable
# df1 = df.set_index('Id')
# We can use inplace

df.set_index('Id', inplace=True)
print(df)
