#connecting with db
import sqlite3
con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

#creating table videos(use ''' triple quotes as it sends the value as it is)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit() #to commit values

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id =?",(video_id,)) #while giving one parameter put ,
    con.commit()

def main():#created a main() function
    while True:
        print("\n Youttube manager App with db")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. exit")
        choice = input("enter your choice: ")

        #using if else to check cases
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("enter video id to update: ")
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("enter video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("invalid choice")

    con.close()   




if __name__ == "__main__":#if name is main then call main()
    main()