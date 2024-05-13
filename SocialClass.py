from Entitys.Connect_Database import Connect_Database

class UserTable:
    def __init__(self,dbconn):
        self.dbconn = dbconn
    #setters and getters
    def setUser_ID(self,uid):
        self.User_ID = uid
    def getUser_ID(self):
        return self.User_ID

    def setUsername(self,Username):
        self.Username = Username
    def getUsername(self):
        return self.Username

    def setEmail(self,Email):
        self.Email = Email
    def getEmail(self):
        return self.Email

    def setPass_word(self,Pass_word):
        self.Pass_word = Pass_word
    def getPass_word(self):
        return self.Pass_word

    #real functions
    def insert(self):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object
        cur.execute('select NEXTVAL(SBA.uid_seq) from dual') #next val
        entry = cur.fetchone() #get vals
        self.User_ID = int(entry[0])

        #insert stmt
        sql = 'insert into UserTable(User_ID,Username,Email,Pass_word) values (%s,%s,%s,%s)'
        val = (self.User_ID,self.Username,self.Email,self.Pass_word)

        #run sql cmd
        cur.execute(sql,val)

        #commit
        temp.commit()


    def updateUser(self):
        # will update values for users

        temp = self.dbconn.getConnection() #connect
        cur = temp.cursor()

        stmt = 'update UserTable set Username = %s, Email = %s, Pass_word = %s where User_ID = %s'
        val = (self.Username,self.Email,self.Pass_word, self.User_ID)

        cur.execute(stmt,val) #execute stmt cmd

        temp.commit()

    def findByUsername(self,name):

        temp = self.dbconn.getConnection()
        cur = temp.cursor()
        # select to show vals associated w username
        stmt = "select User_ID, Email, Pass_word from UserTable where Username = %s"

        val = [name]

        cur.execute(stmt,val)

        result = cur.fetchone()

        #show vals
        self.Username = name
        self.User_ID = result[0]
        self.Email = result[1]
        self.Pass_word = result[2]

    def DisplayAll(self):
        # this method will return a list of water_systems objects
        UserList = list()  # create empty list

        # get database connection
        temp = self.dbconn.getConnection()
        mysqlcursor = temp.cursor()

        # create the sql
        sql = "select User_ID,Username,Email,Pass_word from UserTable order by User_ID"
        mysqlcursor.execute(sql)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        for rows in myresults:
            # create social butterfly
            tempsb = UserTable(self.dbconn)
            # load the values into the attributes of the object using the setter methods
            tempsb.setUser_ID(int(rows[0]))
            tempsb.setUsername(rows[1])
            tempsb.setEmail(rows[2])
            tempsb.setPass_word(rows[3])
            # add to list
            UserList.append(tempsb)
        # return the list of objects
        return UserList


#PostTable class
class PostTable:
        #coonectt
    def __init__(self,dbconn):
        self.dbconn = dbconn

    #setters and getters
    def setUser_ID(self,uid):
        self.User_ID = uid
    def getUser_ID(self):
        return self.User_ID

    def setPost_ID(self,pid):
        self.Post_ID = pid
    def getPost_ID(self):
        return self.Post_ID

    def setContent_Type(self,typo):
        self.Content_Type = typo
    def getContent_Type(self):
        return self.Content_Type

    def setPost_Time(self,pt):
        self.Post_Time = pt
    def getPost_Time(self):
        return self.Post_Time

    def PostContent(self):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object
        cur.execute('select NEXTVAL(SBA.pid_seq) from dual') #next val
        entry = cur.fetchone() #get vals
        self.Post_ID = int(entry[0])

        #insert stmt
        sql = 'insert into PostTable(Post_ID,User_ID,Content_Type,Post_Time) values (%s,%s,%s,%s)'
        val = (self.Post_ID,self.User_ID,self.Content_Type,self.Post_Time)

        #run sql cmd
        cur.execute(sql,val)

        #commit
        temp.commit()

    def DisplayTimeline(self):
        # this method will return a list of water_systems objects
        PostList = list()  # create empty list

        # get database connection
        temp = self.dbconn.getConnection()
        mysqlcursor = temp.cursor()

        # create the sql
        sql = "select Post_ID,User_ID,Content_Type,Post_Time from PostTable order by Post_ID"
        mysqlcursor.execute(sql)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        for rows in myresults:
            # create social butterfly
            temps = PostTable(self.dbconn)
            # load the values into the attributes of the object using the setter methods
            temps.setPost_ID(int(rows[0]))
            temps.setUser_ID(rows[1])
            temps.setContent_Type(rows[2])
            temps.setPost_Time(rows[3])
            # add to list
            PostList.append(temps)
        # return the list of objects
        return PostList


#CommetTable class

class CommentTable:
    #coonectt
    def __init__(self,dbconn):
        self.dbconn = dbconn

    #setters and getters
    def setUser_ID(self,uid):
        self.User_ID = uid
    def getUser_ID(self):
        return self.User_ID

    def setPost_ID(self,pid):
        self.Post_ID = pid
    def getPost_ID(self):
        return self.Post_ID

    def setComment_Content(self,typo):
        self.Comment_Content = typo
    def getComment_Content(self):
        return self.Comment_Content

    def setComment_Time(self,pt):
        self.Comment_Time = pt
    def getComment_Time(self):
        return self.Comment_Time

    #insert a new comment
    def Comment(self):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object

        #insert stmt
        sql = 'insert into PostTable(Comment_Content,User_ID,Post_ID,Comment_Time) values (%s,%s,%s,%s)'
        val = (self.Post_ID,self.User_ID,self.Comment_Content,self.Comment_Time)

        #run sql cmd
        cur.execute(sql,val)

        #commit
        temp.commit()

    def SearchComments(self,ID):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object

        sql = "select User_ID,Comment_Content,Comment_Time from CommentTable where Post_ID = %s"

        val = [ID]
        cur.execute(sql, val)
        myresults = cur.fetchall()
        Comments = list()

        for i in myresults:
            temps = CommentTable(self.dbconn)

            temps.setUser_ID(int(i[0]))
            temps.setComment_Content(i[1])
            temps.setComment_Time(i[2])
            # add to list
            Comments.append(temps)
        # return the list of objects
        return Comments

class LikeTable:
    #coonectt
    def __init__(self,dbconn):
        self.dbconn = dbconn

    #setters and getters
    def setUser_ID(self,uid):
        self.User_ID = uid
    def getUser_ID(self):
        return self.User_ID

    def setPost_ID(self,pid):
        self.Post_ID = pid
    def getPost_ID(self):
        return self.Post_ID

    def setLike_ID(self,lid):
        self.Like_ID = lid
    def getLike_ID(self):
        return self.Like_ID

    def setLike_Time(self,lt):
        self.Like_Time = lt
    def getLike_Time(self):
        return self.Like_Time

    #insert a new comment
    def Like(self):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object
        cur.execute('select NEXTVAL(SBA.like_seq) from dual') #next val
        entry = cur.fetchone() #get vals
        self.Like_ID = int(entry[0])

        #insert stmt
        sql = 'insert into LikeTable(Like_ID,User_ID,Post_ID,Like_Time) values (%s,%s,%s,%s)'
        val = (self.Like_ID,self.User_ID,self.Post_ID,self.Like_Time)

        #run sql cmd
        cur.execute(sql,val)

        #commit
        temp.commit()

    def SearchLikes(self,ID):
        temp = self.dbconn.getConnection() #connect to DB
        cur = temp.cursor() #cursor object

        sql = "select Like_ID,User_ID from LikeTable where Post_ID = %s"

        val = [ID]
        cur.execute(sql, val)
        myresults = cur.fetchall()
        likes = list()
        for i in myresults:
            temps = LikeTable(self.dbconn)
            temps.setLike_ID(int(i[0]))
            temps.setUser_ID(int(i[1]))
            # add to list
            likes.append(temps)
        # return the list of objects
        if(not likes):
            print("There are No Likes Under This Post")
            return
        else:
            return likes


class FriendTable:
    #coonectt
    def __init__(self,dbconn):
        self.dbconn = dbconn

    #setters and getters
    def setUser_ID(self,uid):
        self.User_ID = uid
    def getUser_ID(self):
        return self.User_ID

    def setNumOfFriends(self,n):
        self.NumOfFriends = n
    def getNumOfFriends(self):
        return self.NumOfFriends

    def SeeFriends(self):
        Friends = list()  # create empty list

        # get database connection
        temp = self.dbconn.getConnection()
        cur = temp.cursor()

        # create the sql
        sql = "select User_ID,NumOfFriends from FriendTable order by User_ID"
        cur.execute(sql)
        # get all of the results

        myresults = cur.fetchall()
        # loop through each result
        for rows in myresults:
            #create social butterfly
            tempsb = FriendTable(self.dbconn)

            tempsb.setUser_ID(int(rows[0]))
            tempsb.setNumOfFriends(int(rows[1]))

            # add to list
            Friends.append(tempsb)
        # return the list of objects
        return Friends


