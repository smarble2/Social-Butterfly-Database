Create user 'TTSUser' IDENTIFIED BY 'osboxes.org';

create database SBA;

grant all privileges on SBA.* TO 'TTSUser';

create table SBA.UserTable
(
   User_ID int PRIMARY KEY,
   Username varchar(50) UNIQUE,
   Email varchar(50),
   Pass_word varchar(50)
);


create table SBA.PostTable
(
   Post_ID int PRIMARY KEY,
   User_ID int,
   Content_Type varchar(10), 
   Post_Time varchar(7), 
   FOREIGN KEY(User_ID) REFERENCES UserTable(User_ID)
);


create table SBA.CommentTable
(
   Comment_Content varchar(50),
   User_ID int,
   Post_ID int,
   Comment_Time varchar(7), 
   FOREIGN KEY(User_ID) REFERENCES UserTable(User_ID),
   FOREIGN KEY(Post_ID) REFERENCES PostTable(Post_ID)
);


create table SBA.LikeTable
(
   Like_ID int PRIMARY KEY,
   User_ID int,
   Post_ID int,
   Like_Time varchar(7), 
   FOREIGN KEY(User_ID) REFERENCES UserTable(User_ID),
   FOREIGN KEY(Post_ID) REFERENCES PostTable(Post_ID)
);


create table SBA.FriendTable
(
   User_ID int,
   NumOfFriends int,
   FOREIGN KEY(User_ID) REFERENCES UserTable(User_ID)
);

create sequence SBA.uid_seq;
create sequence SBA.pid_seq;
create sequence SBA.com_seq;
create sequence SBA.like_seq;
create sequence SBA.friend_seq;
