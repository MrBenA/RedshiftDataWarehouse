import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# FILL IN THE REDSHIFT ENPOINT HERE 
DWH_ENDPOINT="" 
    
#FILL IN THE IAM ROLE ARN
DWH_ARN=""

# CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS sparkify;
SET search_path TO sparkify;

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
""")

staging_songs_table_create = ("""
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id IDENTITY(0,1) PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL,
        level VARCHAR() NOT NULL,
        song_id VARCHAR(),
        artist_id VARCHAR()
        session_id INTEGER NOT NULL,
        location VARCHAR(),
        user_agent VARCHAR()
);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR() NOT NULL,
        last_name VARCHAR() NOT NULL,
        gender VARCHAR(),
        level VARCHAR()
);
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR(),
        artist_id VARCHAR(),
        year INTEGER,
        duration FLOAT
);
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id VARCHAR() PRIMARY KEY,
        name VARCHAR NOT NULL,
        location VARCHAR(),
        latitude VARCHAR(),
        longitude VARCHAR()
);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INTEGER NOT NULL,
        day INTEGER NOT NULL,
        week INTEGER NOT NULL,
        month INTEGER NOT NULL,
        year INTEGER NOT NULL,
        weekday INTEGER NOT NULL
);
""")

# STAGING TABLES

staging_events_copy = ("""
copy staging_events_copy from 's3://udacity-dend/log_json_path.json' 
    credentials 'aws_iam_role={}' 
    region 'us-west-2';
""").format(DWH_ROLE_ARN)

staging_songs_copy = ("""
copy staging_events_copy from 's3://udacity-dend/song_data/{}' 
    credentials 'aws_iam_role={}'
    region 'us-west-2';
""").format(!!!!!, DWH_ROLE_ARN)

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]