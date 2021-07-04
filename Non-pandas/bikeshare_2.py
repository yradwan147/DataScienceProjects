import time
import pandas as pd
import numpy as np
import os

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

PATH = os.path.dirname(os.path.realpath(__file__))

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']
days = ['all', 'sunday', 'monday', 'tuesday',
        'wednesday', 'thursday', 'friday', 'saturday']


def raw_data_prompt(df):
    row_number = 0
    prompt = input(
        "Would you like to see the raw data? It will be displayed five rows at a time. (y/n)\n")
    if prompt == 'y':
        while True:
            row_number += 5
            print(df[row_number-5:row_number])
            prompt2 = input("Continue? (y/n)\n")
            if prompt2 == 'n':
                break


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input(
            "Enter the city you'd like to select: (chicago, new york city, washington)\n")).lower()
        if city not in CITY_DATA:
            print("Invalid Input\n")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input(
            "Enter the month you'd like to filter or type all if you want full inspection\n")).lower()
        if month not in months:
            print("Invalid Input\n")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input(
            "Enter the day you'd like to filter or type all if you want full inspection\n")).lower()
        if day not in days:
            print("Invalid Input\n")
        else:
            break

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

    # load data file into a dataframe
    df = pd.read_csv(PATH + '\\' + CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: ' + str(months[df['month'].mode()[0]]))

    # display the most common day of week
    print('Most common day: ' + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('Most common day: ' + str((df['Start Time'].dt.hour).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most common end station: ' + str(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ' + str(df['Trip Duration'].sum()))
    # display mean travel time
    print('Mean travel time: ' + str(df['Trip Duration'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, flag):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Counts: \n' + str(df['User Type'].value_counts())[
          :str(df['User Type'].value_counts()).find("Name:")])
    # Display counts of gender
    if flag:
        print('Gender Counts: \n' + str(df['Gender'].value_counts())
              [:str(df['Gender'].value_counts()).find("Name:")])

    # Display earliest, most recent, and most common year of birth
        print('Earliest year of birth: ' + str(df['Birth Year'].min()) +
              '\nMost recent year of birth: ' + str(df['Birth Year'].max()) +
              '\nMost common year of birth: ' + str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        if city == 'washington':
            flag = False
        else:
            flag = True
        df = load_data(city, month, day)

        raw_data_prompt(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, flag)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
