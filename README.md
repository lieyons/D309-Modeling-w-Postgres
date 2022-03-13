# Data Modeling with Postgres

## Introduction

Startup company Sparkify requested a solution for analyzing their user and song data from their new streaming app. The goal for this solution was to make it easier to understand what songs users are listening to. 

The provided solution utilizes the previously existing JSON directory logs of user activity, as well as JSON metadata available on device songs. This was used to create an ETL pipeline using Python. The data sets are organized into a star schema, with one fact table, and four dimension tables. 

## Star Schema

### Fact Table
1. songplays - records in log data associated with song plays i.e. records with page NextSong
  - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
2. users - users in the app
  - user_id, first_name, last_name, gender, level

3. songs - songs in music database
  - song_id, title, artist_id, year, duration

4. artists - artists in music database
  - artist_id, name, location, latitude, longitude

5. time - timestamps of records in songplays broken down into specific units
  - start_time, hour, day, week, month, year, weekday
  
### User Activity Logs

The log files in the user activity dataset are partitioned by year and month. 

*Example:*
>log_data/2018/11/2018-11-12-events.json
>log_data/2018/11/2018-11-13-events.json

The user activity logs contain information about the user of the app *(ie: name, gender, user_id, location etc)*, as well as data regarding music listened to *(ie: title, artist_name)*. This provides data for our fact table, **songplays**, as well as the dimension tables **users** and **time**. 

### Song Metadata

The song data set includes metadata about the song and artist. The song data is partitioned by the first three letters of each song's track ID. 

Example:
>song_data/A/B/C/TRABCEI128F424C983.json
>song_data/A/A/B/TRAABJL12903CDCF1A.json

Here is a sample song record:
>{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

The metadata includes information on the song *(ie: song_id, title etc)*, as well as the artist information *(ie: artist_id, artist_location etc)*. This is used to populate the dimension tables for **songs** and **artists** 


Graphical representation of STAR schema: 
