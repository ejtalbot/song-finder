create table artists (
    id text primary key,
    name text not null
);

create table songs (
    id integer primary key,
    title text not null
);

create table tracks (
    id text primary key,
    artist_id not null,
    song_id not null,
    foreign key (artist_id) references artists (id),
    foreign key (song_id) references songs (id)
);