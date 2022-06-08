import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv', 'new york' :'new_york_city.csv' }
def row_data_display(df):
    """
    Keeps asking useres if they want to see 5 rows of individual trip data until they enter no.
    Args:
        (pandas data frame) df: the filtered data frame from the required database specified in get_filters fun
    """
    data_counter = 0
    try:
        while True:
            if data_counter == 0:
                row_data_display_input = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            else:
                row_data_display_input = input('\nWould you like to view the next 5 rows of individual trip data? Enter yes or no\n').lower()
            if row_data_display_input == 'yes':
                if data_counter < (len(df)-5):
                    print(df[data_counter:data_counter+5])
                    data_counter += 5
                elif len(df)-5 < data_counter < len(df):
                    print('df[data_counter:]')
                    print("That's the end of the file")
                    break
            else:
                break
    except KeyboardInterrupt:
        print('')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city file to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city_input = input('Which city do you want to analyze data for, Chicago, New York City or Washington?\n').lower()
        while True:
            if city_input in CITY_DATA:
                city = CITY_DATA[city_input]
                break
            else:
                city_input = input('We, don\'t have data for {} city, please choose from Chicago, New York City or Washington\nplease make sure you entered it right\n'.format(city_input)).lower()
    except KeyboardInterrupt:
        try:
            keyboard_interrupt_input = input("Enter r to restart the program or exit to exit\n").lower()
            if keyboard_interrupt_input == 'r':
                print('The program has been restarted\n')
                main()
            else:
                print('Thanks for using our program')
                exit()
        except KeyboardInterrupt:
            print('Thanks for using our program')
            exit()
    print('You choosed: {}\n'.format(city_input.title()))

    # get user input for month (all, january, february, ... , june)
    # accepting namess or integer inputs for months (jan: 1, feb:2,...)
    try:
        month_dict = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 'all': 'all'}
        month_input = input('Which month do you want to analyze data for:\n(all, january, february, ... , june)\n').lower()
        while True:
            if month_input == 'all':
                month = 'all'
                break
            # handling typos in month input
            elif 'jan' in month_input:
                month = 1
                break
            elif 'feb' in month_input:
                month = 2
                break
            elif 'mar' in month_input:
                month = 3
                break
            elif 'apr' in month_input:
                month = 4
                break
            elif 'may' in month_input:
                month = 5
                break
            elif 'jun' in month_input:
                month = 6
                break
            elif 'jul' in month_input or 'aug' in month_input or 'sep' in month_input or 'oct' in month_input or 'nov' in month_input or 'dec' in month_input:
                month_input = input("We don't have data for {}, please choose a month from January to June\n".format(month_input.title())).lower()
            # handling integer input for month name
            elif month_input.isdigit() and 0 < int(month_input) <13:
                if int(month_input) <= 6:
                    month = int(month_input)
                    break
                elif 6 < int(month_input) <= 12:
                    month_input = input("We don't have data for the {}th month, please choose from January to June\n".format(month_input)).lower()
            else:
                month_input = input('There is no {} in months, please choose a month from January to June\n'.format(month_input)).lower()
        print('The selected month is {}\n'.format(month_dict[month]))
    except KeyboardInterrupt:
        try:
            keyboard_interrupt_input = input("Enter r to restart the program or exit to exit\n").lower()
            if keyboard_interrupt_input == 'r':
                print('The program has been restarted\n')
                main()
            else:
                print('Thanks for using our program')
                exit()
        except KeyboardInterrupt:
            print('Thanks for using our program')
            exit()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day_input = input('Which day do you want to analyze data for:\n(all, monday, tuesday, ... sunday)\n').lower()
        while True:
            if day_input == 'all':
                day = 'all'
                break
            # handling typos in day input
            elif 'mon' in day_input:
                day = 'Monday'
                break
            elif 'tue' in day_input:
                day = 'Tuesday'
                break
            elif 'wed' in day_input:
                day = 'Wednesday'
                break
            elif 'thu' in day_input:
                day = 'Thursday'
                break
            elif 'fri' in day_input:
                day = 'Friday'
                break
            elif 'sat' in day_input:
                day = 'Saturday'
                break
            elif 'sun' in day_input:
                day = 'Sunday'
                break
            else:
                day_input = input('There is no {} in days, please choose a day from Monday to Sunday \n'.format(day_input)).lower()
        print('The selected day is {}\n'.format(day))
    except KeyboardInterrupt:
        try:
            keyboard_interrupt_input = input("Enter r to restart the program or exit to exit\n").lower()
            if keyboard_interrupt_input == 'r':
                print('The program has been restarted\n')
                main()
            else:
                print('Thanks for using our program')
                exit()
        except KeyboardInterrupt:
            print('Thanks for using our program')
            exit()
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
    df = pd.read_csv(city)
    df.fillna(method='ffill', axis=0, inplace=True)
    df.fillna(method='backfill', axis=0, inplace=True)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    df['Start Station [To] End Station'] = df['Start Station'] +' -[To]- ' + df['End Station']
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month == 'all' and day != 'all':
        df = df[df['Day'] == day]
        print('You filtered data by day')
    elif day == 'all' and month != 'all':
        df = df[df['Month'] == month]
        print('You filtered data by month ')
    elif day != 'all' and month != 'all':
        df = df[df['Month'] == month]
        df = df[df['Day'] == day]
        print('You filtered data by day and month')

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_dict = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    print('The most common month is: {} with count of {} which represents {}% of the selected data'.format(month_dict[df['Month'].value_counts().index[0]],
    df['Month'].value_counts().iloc[0], round(df['Month'].value_counts().iloc[0]*100/len(df), 2)))

    if month == 'all':
        print('The second most common month is: {} with count of {} which represents {}% of the selected data'.format(month_dict[df['Month'].value_counts().index[1]],
        df['Month'].value_counts().iloc[1], round(df['Month'].value_counts().iloc[1]*100/len(df), 2)))

        print('The least common month is: {} with count of {} which represents {}% of the selected data'.format(month_dict[df['Month'].value_counts().index[-1]],
        df['Month'].value_counts().iloc[-1], round(df['Month'].value_counts().iloc[-1]*100/len(df), 2)))

    # display the most common day of week
    print('\nThe most common day of the week is: {} with count of {} which represents {}% of the selected data'.format(df['Day'].value_counts().index[0],
    df['Day'].value_counts().iloc[0], round(df['Day'].value_counts().iloc[0]*100/len(df), 2)))

    if day == 'all':
        print('The second most common day of the week is: {} with count of {} which represents {}% of the selected data'.format(df['Day'].value_counts().index[1],
        df['Day'].value_counts().iloc[1], round(df['Day'].value_counts().iloc[1]*100/len(df), 2)))

        print('The least common day of the week is: {} with count of {} which represents {}% of the selected data'.format(df['Day'].value_counts().index[-1],
        df['Day'].value_counts().iloc[-1], round(df['Day'].value_counts().iloc[-1]*100/len(df), 2)))

    # display the most common start hthe selected
    print('\nThe most common start Hour is: {} o\'clock with count of {} which represents {}% of the selected data'.format(df['Hour'].value_counts().index[0],
    df['Hour'].value_counts().iloc[0], round(df['Hour'].value_counts().iloc[0]*100/len(df), 2)))

    print('The second most common start Hour is: {} o\'clock with count of {} which represents {}% of the selected data'.format(df['Hour'].value_counts().index[1],
    df['Hour'].value_counts().iloc[1], round(df['Hour'].value_counts().iloc[1]*100/len(df), 2)))

    print('The least common start Hour is: {} with count of {} which represents {}% of the selected data'.format(df['Hour'].value_counts().index[-1],
    df['Hour'].value_counts().iloc[-1], round(df['Hour'].value_counts().iloc[-1]*100/len(df), 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_series = df['Start Station'].value_counts()
    print('The most commonly used start station is {} with count of {} which represents {}% of the selected data'.format(start_station_series.index[0],
    start_station_series.iloc[0], round(start_station_series.iloc[0]*100/len(df), 2)))

    print('The second most commonly used start station is {} with count of {} which represents {}% of the selected data'.format(start_station_series.index[1],
    start_station_series.iloc[1], round(start_station_series.iloc[1]*100/len(df), 2)))

    print('The least commonly used start station is {} with count of {} which represents {}% of the selected data'.format(start_station_series.index[-1],
    start_station_series.iloc[-1], round(start_station_series.iloc[-1]*100/len(df), 4)))

    # display most commonly used end station
    end_station_series = df['End Station'].value_counts()
    print('\nThe most commonly used end station is {} with count of {} which represents {}% of the selected data'.format(end_station_series.index[0],
    end_station_series.iloc[0], round(end_station_series.iloc[0]*100/len(df), 2)))

    print('The second most commonly used end station is {} with count of {} which represents {}% of the selected data'.format(end_station_series.index[1],
    end_station_series.iloc[1], round(end_station_series.iloc[1]*100/len(df), 2)))

    print('The least commonly used end station is {} with count of {} which represents {}% of the selected data'.format(end_station_series.index[-1],
    end_station_series.iloc[-1], round(end_station_series.iloc[-1]*100/len(df), 4)))

    # display most frequent combination of start station and end station trip
    start_station_to_end_station_series = df['Start Station [To] End Station'].value_counts()
    print('\nThe most frequent combination of start station and end station trip is {} with count of {}\nwhich represents {}% of the selected data'.format(start_station_to_end_station_series.index[0],
    start_station_to_end_station_series.iloc[0], round(start_station_to_end_station_series.iloc[0]*100/len(df), 2)))

    print('The second most frequent combination of start station and end station trip is {} with count of {}\nwhich represents {}% of the selected data'.format(start_station_to_end_station_series.index[1],
    start_station_to_end_station_series.iloc[1], round(start_station_to_end_station_series.iloc[1]*100/len(df), 2)))

    print('The least frequent combination of start station and end station trip is {} with count of {}\nwhich represents {}% of the selected data'.format(start_station_to_end_station_series.index[-1],
    start_station_to_end_station_series.iloc[-1], round(start_station_to_end_station_series.iloc[-1]*100/len(df), 4)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_traveling_time = df['Trip Duration'].sum()
    print('Total traveling time is {}'.format(str(datetime.timedelta(seconds = int(total_traveling_time)))))

    # display mean travel time
    mean_traveling_time = df['Trip Duration'].mean()
    print('\nMean traveling time is {}'.format(str(datetime.timedelta(seconds = int(mean_traveling_time)))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type_series = df['User Type'].value_counts()
    # Display counts of user types
    for i in range(len(user_type_series)):
        print(user_type_series.index[i], user_type_series.iloc[i], sep=': ')

    # Display counts of gender
    if city == 'washington.csv':
        print("There are no data for gender in Washington database")

    else:
        gender_series = df['Gender'].value_counts()
        for i in range(len(gender_series)):
            print(gender_series.index[i], gender_series.iloc[i], sep=': ')

    # Display earliest, most recent, and most common year of birth
    if city == 'washington.csv':
        print("There are no data for birth year in Washington database")

    else:
        print('\nThe earliest year of birth is', int(df['Birth Year'].min()))
        print('The most recent year of birth is', int(df['Birth Year'].max()))

        #handling more than one mode
        birth_year_mode_series = df['Birth Year'].mode()
        print("The most common year of birth is ", end='')
        for i in range(len(birth_year_mode_series)):
            print(int(df['Birth Year'].mode().iloc[i]), end=' ')
        print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        row_data_display(df)

        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print('Thanks for using our program')
                exit()
            else:
                print('The program has been restarted\n')
        except KeyboardInterrupt:
            print("Thanks for using our program")
            exit()

if __name__ == "__main__":
	main()
