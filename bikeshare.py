import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =""
    city_names = ['chicago', 'new york city', 'washington']
    while city.lower() not in city_names:
        city=input("Please input city name (chicago, new york city, washington)")
        city=city.lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month =""
    months = ['all','january', 'february', 'march' , 'april','may','june']
    while month.lower() not in months:
        month=input("Please input for month (all, january, february, ... , june)")
        month=month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =""
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday' , 'friday','saturday','sunday']
    while day.lower() not in days:
        day=input("Please input for day of week (all, monday, tuesday, ... sunday)")    
        day=day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read data from csv file
    df= pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # convert the End Time column to datetime
    #df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name  #weekday_name in previous pandas
    
    #extract hour from start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    
    #combination of start station and end station trip to create new column
    df['start_end_station']=df['Start Station'] + '  ---  ' + df['End Station']
    

    
    #filter data 

    #filter by month
    if month!='all':
        #get index of selected month from months
        months = ['all','january', 'february', 'march' , 'april','may','june']
        month = months.index(month) # just because all at the index 0 and starts from inex 1
        #filter by month to create the new data frame
        df = df[df['month']==month]
    #filter by day    
    if day!='all':
        #get index of selected day from days
        days = ['all','monday', 'tuesday', 'wednesday', 'thursday' , 'friday','saturday','sunday']
        #filter by month to create the new data frame    
        df = df[df['day_of_week']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['all','january', 'february', 'march' , 'april','may','june']
    print ("\nThe most common month:" , months[df['month'].mode()[0]])

    # TO DO: display the most common day of week
    print ("\nThe most common day of the week:",df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour of the day
    print ("\nThe most common hour of the day:",df['hour'].mode()[0])
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ("\nThe most commonly used start station:",df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print ("\nThe most commonly used end station:",df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print ("\nThe most frequent combination of start station and end station trip:",df['start_end_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nTotal travel time %s seconds" % (df['Trip Duration'].sum()))
    

    # TO DO: display mean travel time
    print("\nMean travel time %s seconds" % (df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print( '\ncounts of user types: \n',df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print( '\ncounts of gender: \n',df['Gender'].value_counts())    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print ('\nYear of birth: Easliest {} , Recent {} , Most common {}'.format(int(df['Birth Year'].min()),int(df['Birth Year'].max()),int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
