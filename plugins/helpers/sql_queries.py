class SqlQueries:
    songplay_table_insert = ("""
        SELECT e.ts as start_time,
            e.userId as user_id,
            e.level as level,
            s.song_id as song_id,
            s.artist_id as artist_id,
            e.sessionId as session_id,
            e.location as location,
            e.userAgent as user_agent
        FROM staging_events e
        JOIN staging_songs s ON (e.song = s.title AND e.artist = s.artist_name)
    """)

    user_table_insert = ("""
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page='NextSong'
    """)

    song_table_insert = ("""
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)