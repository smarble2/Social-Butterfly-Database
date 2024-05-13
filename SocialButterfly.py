from Entitys.SocialClass import UserTable
from Entitys.SocialClass import PostTable
from Entitys.SocialClass import CommentTable
from Entitys.SocialClass import LikeTable
from Entitys.SocialClass import FriendTable

from Entitys.Connect_Database import Connect_Database

def mainmenu():
    print("\nWelcome Butterfly. What Would You Like To Do ?")
    print("\nUser Actions: ")
    print("1. Enter a new social butterfly user")
    print("2. Display all users in social butterfly")
    print("3. Update a current user")
    print ("4. Display social butterfly user by username")

    print ("\n\nPost Actions: ")
    print ("5. Create A Post for the Timeline")
    print("6. View All Posts")

    print("\n\nComment Actions: ")
    print ("7. Comment On A Post")
    print("8. View Comments On Post by ID")

    print("\n\nLike Actions: ")
    print("9. Like a Post")
    print("10. View Likes by Post ID")

    print("\n\nFriend Actions: ")
    print("11.View Number of Friends of All Social Butterflies")

    print("12. Quit")

def SBapp():
    choice = 0; #init user input
    conn = Connect_Database() #est a connection to db

    sb = UserTable(conn) #current usertable in the social butterfly db

    while(choice < 10):
        mainmenu() #call menu options
        choice = int(input("Enter choice: "))

        if(choice == 1):
            print("Insert a new User into the Social Butterfly App")
            name = input('Enter a cool username: ')
            email = input('Enter your email address: ')
            pw = input('Enter a password: ')
            sb = UserTable(conn)
            sb.setUsername(name)
            sb.setEmail(email)
            sb.setPass_word(pw)
            sb.insert()
            print("New User Alert! Welcome to Social Butterfly.")
        elif(choice == 2):
            print("Showing all Social Butterflies: \n")
            allsb = sb.DisplayAll()
            for i in allsb:
                print('User ID:', i.getUser_ID(), 'Username:', i.getUsername(), 'Email:',
                i.getEmail(), 'Password:', i.getPass_word())
        elif(choice == 3):
            print("Let's Change Some Info...")
            i = input("Enter the User_ID you want to update: ")
            u = input('Enter new Username: ')
            e = input('Enter new Email ')
            p = input('Enter new Password: ')
            sb.setUser_ID(i)
            sb.setUsername(u)
            sb.setEmail(e)
            sb.setPass_word(p)
            sb.updateUser()
            print('Update complete')
        elif(choice == 4):
            print("Search for another butterfly")
            Username= input("Enter Username: ")
            sb.findByUsername(Username)
            print(' User_ID: ', sb.getUser_ID())
            print(' Email: ', sb.getEmail())
            print(' Password: ', sb.getPass_word())

        elif (choice == 5 ):
            print("Post Something fun: ")
            u  = input('ID of who is posting: ')
            c = input('What are you posting (video or photo): ')
            t = input('What time is it: ')
            ps = PostTable(conn)
            ps.setUser_ID(u)
            ps.setContent_Type(c)
            ps.setPost_Time(t)
            ps.PostContent()
            print("You Just Posted a ", c, " at ", t," ! ")
        elif(choice == 6):
            print("Showing all Timeline Posts: \n")
            ps = PostTable(conn) #post table obj
            alls = ps.DisplayTimeline()

            for i in alls:
                print('Post ID:', i.getPost_ID(), 'User_ID:', i.getUser_ID(), 'Content:',
                i.getContent_Type(), 'Post Time:', i.getPost_Time())

        elif (choice == 7):
            # to create comments
            print("Comment Something Nice: ")
            u  = input('ID of who is commenting: ')
            p = input('ID of the Post that you are commenting on: ')
            c = input ('Type your comment: ')
            t = input('What time is it: ')

            cs = CommentTable(conn)
            cs.setUser_ID(u)
            cs.setPost_ID(p)
            cs.setComment_Content(c)
            cs.setComment_Time(t)

            cs.Comment()
            print("You Just Commented", c, " on ", p,"'s Post ! ")

        elif(choice == 8):
            ct = CommentTable(conn) #conntect

            print("Search for Comments under a Post")
            i= input("Enter ID of the Post: ")

            coms = ct.SearchComments(i)
            print("Showing Comments Under Post ID",i, ": \n")
            for c in coms:
                print('User_ID:', c.getUser_ID(), 'Comment:',
                c.getComment_Content(), 'Comment Time:', c.getComment_Time())

        elif (choice == 9):
            # to create comments
            print("Like A Post: ")
            u  = input('ID of who is Liking : ')
            p = input('ID of the Post that you are Liking: ')
            t = input('What time is it: ')

            ls = LikeTable(conn)
            ls.setUser_ID(u)
            ls.setPost_ID(p)
            ls.setLike_Time(t)

            ls.Like()
            print("You Just Liked",p,"'s Post ! ")

        elif(choice == 10):
            ls = LikeTable(conn) #conntect

            print("Search for Likes under a Post")
            i= input("Enter ID of the Post: ")

            likes = ls.SearchLikes(i)
            if(not likes):
                print("...")
            else:
                print("Showing Likes Under Post ID",i, ": \n")
                for l in likes:
                    print('User_ID:', l.getUser_ID(), 'Like ID:',
                    l.getLike_ID())
            SBapp()
        elif(choice == 11):
            fb = FriendTable(conn)
            print("Showing all Butterflies and Number of Friends: \n")
            allfb = fb.SeeFriends()
            for i in allfb:
                print('User ID:', i.getUser_ID(), 'has ', i.getNumOfFriends())
            SBapp()
        else:
            print("Leaving? Bye Bye Butterfly!")
            conn.close()

SBapp() #call app