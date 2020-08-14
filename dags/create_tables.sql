DROP TABLE IF EXISTS public.artists;
DROP TABLE IF EXISTS public.songplays;
DROP TABLE IF EXISTS public.songs;
DROP TABLE IF EXISTS public.staging_events;
DROP TABLE IF EXISTS public.staging_songs;
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.time;

CREATE TABLE public.artists (
	artistid varchar(256) NOT NULL,
	name varchar(256),
	location varchar(256),
	latitude numeric(18,0),
	longitude numeric(18,0)
);

CREATE TABLE public.songplays (
	songplay_id int IDENTITY(0,1) PRIMARY KEY, 
    start_time bigint NOT NULL, 
    user_id int NOT NULL, 
    level varchar NOT NULL, 
    song_id varchar, 
    artist_id varchar, 
    session_id int NOT NULL, 
    location varchar NOT NULL, 
    user_agent varchar NOT NULL
);

CREATE TABLE public.songs (
	songid varchar(256) NOT NULL,
	title varchar(256),
	artistid varchar(256),
	"year" int4,
	duration numeric(18,0),
	CONSTRAINT songs_pkey PRIMARY KEY (songid)
);

CREATE TABLE public.staging_events (
	artist varchar(256),
	auth varchar(256),
	firstname varchar(256),
	gender varchar(256),
	iteminsession int4,
	lastname varchar(256),
	length numeric(18,0),
	"level" varchar(256),
	location varchar(256),
	"method" varchar(256),
	page varchar(256),
	registration numeric(18,0),
	sessionid int4,
	song varchar(256),
	status int4,
	ts int8,
	useragent varchar(256),
	userid int4
);

CREATE TABLE public.staging_songs (
	num_songs int4,
	artist_id varchar(256),
	artist_name varchar(256),
	artist_latitude numeric(18,0),
	artist_longitude numeric(18,0),
	artist_location varchar(256),
	song_id varchar(256),
	title varchar(256),
	duration numeric(18,0),
	"year" int4
);

CREATE TABLE public.users (
	userid int4 NOT NULL,
	first_name varchar(256),
	last_name varchar(256),
	gender varchar(256),
	"level" varchar(256),
	CONSTRAINT users_pkey PRIMARY KEY (userid)
);

CREATE TABLE public.time (
    start_time varchar PRIMARY KEY, 
    hour int NOT NULL, 
    day int NOT NULL, 
    week int NOT NULL, 
    month int NOT NULL, 
    year int NOT NULL, 
    weekday int NOT NULL
);
