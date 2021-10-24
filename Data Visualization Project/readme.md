# # Bike Trips Dataset Analysis
## by Yousef Ahmed Radwan


## Dataset

> The used dataset includes information about Ford GoBike trips. It includes information like the start and end time of the trip, the start and end station of the trip, in addition to multiple other fields.

>There seems to be a number of missing fields in about 8000 rows. Since this number is relatively small in comparison to the total number of observations (183 thousand), these rows were removed.

We end up with 174952 rows in total. Now it's time to adjust some field data types.
1. start_time and end_time should have a dtype of datetime
2. start_station_id and end_station_id should be int types since the float type is of no value here.
3. user_type and member_gender can become a categorical dtype
4. member_birth_year should be an integer type

All of these changes were completed.

## Summary of Findings

* Most common trip duration is around 6 minutes and quickly drops off
* Most common starting and ending weekday is Thursday and least common are Saturday and Sunday
* Most common starting and ending hours seem to be either around 8-9am or 4-6pm
* Certain bikes are used alot more than others and these bikes are usually linked to higher ids from around 5000+
* Users are mostly subscribers and are mostly men
* start_hour and end_hour are almost exactly similar
* Average trip duration for every hour of the day seems similar with the exception of 2 and 3 am which have abnormal spikes, and a decrease at 6am
* Longer trip durations are mostly on Saturday and Sunday
* The previous bike_id observation is due to the fact that the most popular stations (top 20) all have bike ids around 5000 and it was not due to subscription.
* Doesn't seem to be any correlation between subscription type and age or gender
* Longer trips are mostly done by younger users
* Most short trips occur on later days of the week mostly regardless of start hour except the time interval between about 3 and 5 which seems to host less trips and on earlier weekdays. Most long trips also seem to be near the beginning of the week or the middle. 
* Male subscribers show a bimodal age distribution in comparison to unimodal male customers and subscribers feature more older users in the "Other" gender category
* In the top 15 stations, earlier hours of the day feature relatively low traffic with a few exceptions for one or 2 stations.
* In the top 15 stations, after 5am, activity becomes mostly uniform except for one super high spot at 11 pm at 2nd St.

However, it should be noted that the last heatmap (2 observations) can be subject to heavy biased since some hours of the day have more data points surrounding them than others and also some of these stations might have most of their trips during a certain time interval of the day and have very few trips otherwise.

## Key Insights for Presentation

> Select one or two main threads from your exploration to polish up for your presentation. Note any changes in design from your exploration step here.

* Certain bikes are used alot more than others and these bikes are usually linked to higher ids from around 5000+ and this is due to the fact that the most popular stations (top 20) all have bike ids around 5000

* Most common trip duration is around 6 minutes and quickly drops off
* Average trip duration for every hour of the day seems similar with the exception of 2 and 3 am which have abnormal spikes, and a decrease at 6am
* Most short trips occur on later days of the week mostly regardless of start hour except the time interval between about 3 and 5 which seems to host less trips and on earlier weekdays. Most long trips also seem to be near the beginning of the week or the middle.
* start_hour and end_hour are almost exactly similar

* Users are mostly subscribers and are mostly men
* Male subscribers show a bimodal age distribution in comparison to unimodal male customers and subscribers feature more older users in the "Other" gender category

* Top 15 stations heatmap