import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_LIST = ['all','january','february','march','april','may','june']
DAYS_LIST   = ['all','monday','tuesday','wednesday','thursday','friday','sunday']

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
    while True:
        city = input("Please enter the city name: chicago, new york city or washington!").lower()             
        if city not in CITY_DATA:
            print('Invalid city, please choose between : chicago, new york city or washington')
            continue
        else:
            break
    while True:
     # TO DO: get user input for month (all, january, february, ... , june)
        month = input("please enter the month as : january,february..june or all ").lower()
        if month not in MONTHS_LIST:
            print('Invalid Month, please choose between january,february..june or all ')
            continue
        else:
            break
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        day = input("please enter the day as : monday,tuesday.. or all ").lower()
                
        if day not in DAYS_LIST:
            print('Invalid day')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    # extract day from start time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        montdict = {"january": 1,"february": 2,"march": 3,"avril":4,"may":5,"june":6 }
        month = montdict[month]
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)


    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.isocalendar().week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    combinations = df['combination'].mode()[0]
    print(combinations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby(['User Type'])['User Type'].count()
    print(user_type,'\n')

    # TO DO: Display counts of gender
    if city == 'washington':
        print('there is no gender info in washington')
    else:
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print("counts of gender in {} ".format(city))
        print(gender_count,'\n')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    df = df.sort_values(['Birth Year'])
    #print(df.head(1)['Birth Year'].to_string(index=False))
    print("The earliest year of birth:",df.head(1)['Birth Year'].to_string(index=False))
    df = df.sort_values(['Birth Year'],ascending=False)
    print("The most recent of birth is {}".format(df.head(1)['Birth Year'].to_string(index=False)))
    com_year = df['Birth Year'].mode()[0]
    print("The common year of birth is ",com_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    #if (view_data == 'no'):
      #  return
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?:Enter yes or no ").lower()
        if view_display != 'yes':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
