drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

SELECT username, password FROM users;
insert into users values  (1,"shashi","shashi1234");
