# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP NOT NULL, user_id BIGINT NOT NULL, level TEXT, song_id TEXT, artist_id TEXT, session_id TEXT, location TEXT, user_agent TEXT);

""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(user_id BIGINT PRIMARY KEY, first_name TEXT, last_name TEXT, gender TEXT, level TEXT);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(song_id VARCHAR PRIMARY KEY, title TEXT NOT NULL, artist_id VARCHAR, year INT, duration NUMERIC(8,5) NOT NULL);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(artist_id VARCHAR PRIMARY KEY, name TEXT NOT NULL, location VARCHAR, latitude DOUBLE PRECISION, longitude DOUBLE PRECISION);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(start_time TIMESTAMP PRIMARY KEY, hour INT, day TEXT, week INT, month TEXT, year INT, weekday TEXT);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
        SELECT songs.song_id,
               artists.artist_id
        FROM  songs
          INNER JOIN artists
            ON songs.artist_id = artists.artist_id
        WHERE songs.title = %s
              AND
              artists.name = %s
              AND
              songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]