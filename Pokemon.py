import pandas as pd

pd.set_option("display.width",320)
pd.set_option("display.max_columns",None)  # Shows all columns
#pd.set_option("display.max_rows",None) # Shows all rows
#df = pd.read_csv(r"C:\Users\oswpe\OneDrive\Desktop\Pokemon_Data\pokemon_data.csv")
#df_xlsx = pd.read_excel(r"C:\Users\oswpe\OneDrive\Desktop\Pokemon_Data\pokemon_data.xlsx")
#print(df_xlsx.head(3))
#print(df.head(5))
#print(df.tail(3))
df = pd.read_csv(r"C:\Users\oswpe\OneDrive\Desktop\Pokemon_Data\pokemon_data.txt", delimiter='\t')
print(df.head(5))
print(df.columns)
#print(df['Name'][0:5])
#print(df.Name)
print(df[['Name', 'Type 1', 'HP']])
print(df.iloc[0:4]) #Read each row
print(df.iloc[2,1])
#for index, row in df.iterrows():
    #print(index, row['Name'])
# print(df.loc[df['Type 1'] == "Fire",])
# print(df.loc[df['Type 1'] == "Grass",])
# print(df.describe())
# print(df.sort_values(['Name'],ascending=False))
# print(df.sort_values(['Type 1', 'HP'],ascending=[1,0])) # 1-ascending,0-descending
print(df.head(5))
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))
print(45+49+49+65+65+45)
df = df.drop(columns=['Total'])
print(df.head(5))
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5))
cols = list(df.columns.values)
print(cols)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))
#df.to_csv('modified.csv', index=False)
df.to_excel('modified.xlsx',index=False)
df.to_csv('modified.txt',index=False,sep='\t')
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(new_df)
new_df.to_csv('filtered.csv')
print(new_df)
new_df = new_df.reset_index(drop=True, inplace =True)
print(new_df)
#print(df.loc[df['Name'].str.contains('Mega')])
#print(df.loc[~df['Name'].str.contains('Mega')])
import re
#print([df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
df.loc[df['Type 1'] == 'Flamer', 'Type 1' ] = 'Fire'
print(df)
df.loc[df['Type 1'] == 'Fire', 'Legendary' ] = True
print(df)
df = pd.read_csv('modified.csv')
print(df)
df.loc[df['Total'] >500, ['Generation','Legendary']] = 'TEST VALUE'
print(df)
df.loc[df['Total'] >500, ['Generation','Legendary']] = ['Test1', 'Test 2']
print(df)
df = pd.read_csv('modified.csv')
print(df)
#df.groupby(['Type 1'].mean().sort_values('Attack', ascending=False))
print(df)

#print(df.groupby(['Type 1'].count()))
df['count'] =1
#df.groupby(['Type 1'].count()['count'])
# Working with large amounts of data
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])
    #print('CHUNK DF')
    #print(df)








