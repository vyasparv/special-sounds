# import cleaned data 

pd.read_csv("clean_meteorite_landings.csv")

print(df)

# python date objects for all the columns 
def clean(x):
    # x looks like 8/10/2023
    year = int(x.split("/")[2])
    month = int(x.split("/")[1])
    day = datetime.datetime(year, month, day)
    return x 

# clean up string dates in the column 
df['year'] = df['year'].apply(clean)

# Replace NaN values in column 'mass' with 0 
df['mass'] = df['mass'].fillna(0)

# Sort date by ascending
df = df.sort_values(by='year', ascending = True)

# converting csv into a list 
my_data = df.to_dict('records')

print(my_data)

# starting time for each converted time integer 

my_data_timed = [
    {
        'beat': mymidi.beat(d[my_data])
        'year': d['year']
    } for d in my_data
]

# starting date of the original data set 
start_time = my_data[0]['beat']

def data_to_pitch_tuned('year'):
