insert into SBA.UserTable (User_ID, Username, Email, Pass_word) values (NEXTVAL(SBA.uid_seq),'smarble2','sm@gmail.com','12345');
insert into SBA.UserTable (User_ID, Username, Email, Pass_word) values (NEXTVAL(SBA.uid_seq),'dqhendricks','dqhendricks@gmail.com','54321');
insert into SBA.UserTable (User_ID, Username, Email, Pass_word) values (NEXTVAL(SBA.uid_seq),'jqvaughan','jqvaughan@gmail.com','maxwel1');
insert into SBA.UserTable (User_ID, Username, Email, Pass_word) values (NEXTVAL(SBA.uid_seq),'sSosa','sosa@gmail.com','sosaSheloves');
insert into SBA.UserTable (User_ID, Username, Email, Pass_word) values (NEXTVAL(SBA.uid_seq),'RayOfSunshine','Rayal@gmail.com','Raymond3');

insert into SBA.PostTable(Post_ID,User_ID,Content_Type,Post_Time) values(NEXTVAL(SBA.pid_seq),1,'picture','11:18am');
insert into SBA.PostTable(Post_ID,User_ID,Content_Type,Post_Time) values(NEXTVAL(SBA.pid_seq),2,'video','11:30am');
insert into SBA.PostTable(Post_ID,User_ID,Content_Type,Post_Time) values(NEXTVAL(SBA.pid_seq),3,'picture','1:00pm');
insert into SBA.PostTable(Post_ID,User_ID,Content_Type,Post_Time) values(NEXTVAL(SBA.pid_seq),4,'video','7:00pm');
insert into SBA.PostTable(Post_ID,User_ID,Content_Type,Post_Time) values(NEXTVAL(SBA.pid_seq),5,'picture','10:00am');


insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('Beautiful',1,1,'9:45pm');
insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('So Cool!',1,2,'10:00pm');
insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('Amazing',2,3,'11:20am');
insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('Thats Awesome',4,6,'11:20am');
insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('Wow !',6,4,'11:20am');
insert into SBA.CommentTable(Comment_Content,User_ID,Post_ID,Comment_Time)values('Cool Work',3,5,'11:20am');


insert into SBA.LikeTable(Like_ID,User_ID,Post_ID,Like_Time)values(NEXTVAL(SBA.like_seq),2,3,'8:30pm');
insert into SBA.LikeTable(Like_ID, User_ID, Post_ID, Like_Time)values(NEXTVAL(SBA.like_seq), 1, 2, '9:00pm');
insert into SBA.LikeTable(Like_ID, User_ID, Post_ID, Like_Time)values(NEXTVAL(SBA.like_seq), 2, 1, '9:30pm');
insert into SBA.LikeTable(Like_ID, User_ID, Post_ID, Like_Time)values(NEXTVAL(SBA.like_seq), 6, 7, '11:54am');
insert into SBA.LikeTable(Like_ID, User_ID, Post_ID, Like_Time)values(NEXTVAL(SBA.like_seq), 6, 7, '10:11pm');

insert into SBA.FriendTable(User_ID , NumOfFriends)
values(1,100);
insert into SBA.FriendTable(User_ID , NumOfFriends)
values(2,150);
insert into SBA.FriendTable(User_ID , NumOfFriends)
values(3,200);
insert into SBA.FriendTable(User_ID , NumOfFriends)
values(4,250);
insert into SBA.FriendTable(User_ID , NumOfFriends)
values(5,300);
insert into SBA.FriendTable(User_ID , NumOfFriends)
values(6,450);
