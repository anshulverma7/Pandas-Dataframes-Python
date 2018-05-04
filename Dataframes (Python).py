# Author: Anshul Verma

# Dataframes

# EM624 - Exercise 06

import pandas as pd

# to load the 3 datasets (movies.dat, users.dat, ratings.dat) into pandas dataframes
df0 = pd.read_table('movies.dat', sep='::', engine='python', header=None)
df0.columns=['Movie ID','Title','Genre']

df1 = pd.read_table('users.dat', sep='::', engine='python', header=None)
df1.columns=['User ID','Gender','Age', 'Occupation', 'Zipcode']

df2 = pd.read_table('ratings.dat', sep='::', engine='python', header=None)
df2.columns=['User ID','Movie ID','Rating', 'Timestamp']

# to print the first 5 rows of the three dataframes
print "\nThe first 5 rows of movies dataframe are:"
print df0[:5]
print "\nThe first 5 rows of users dataframe are:"
print df1[:5]
print "\nThe first 5 rows of ratings dataframe are:"
print df2[:5]

# to merge the 3 dataframes into a single dataframe
data = pd.merge(pd.merge(df2, df1), df0)

# to print the number of records in each of the 4 dataframes
print "\nThe number of records in movies dataframe are:", len(df0.index)
print "The number of records in users dataframe are:", len(df1.index)
print "The number of records in ratings dataframe are:", len(df2.index)
print "The number of records in merged dataframe are:", len(data.index)

# to assign occupation name to the numerical values in Occupation column 
data.Occupation.replace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [ 'Other / Not Specified', 'Academic / Educator', 'Artist', 'Clerical / Admin', 'College / Grad Student', 'Customer Service', 'Doctor / Healthcare', 'Executive / Managerial', 'Farmer', 'Homemaker', 'K-12 Student', 'Lawyer', 'Programmer', 'Retired', 'Sales / Marketing', 'Scientist', 'Self-Employed', 'Technician / Engineer', 'Tradesman / Craftsman', 'Unemployed', 'Writer'], inplace=True)

# to print last 5 rows of merged dataframe
print "\nThe last 5 rows of merged dataframe are:"
print data[-5:]

# to print the 5 occupations that give higher ratings for movies
df3 = data.groupby('Occupation').sum().sort_values(by='Rating', ascending=False)
print "\nThe 5 occupations that give higher ratings for movies are:"
print df3[:5]