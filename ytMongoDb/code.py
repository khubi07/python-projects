# # import pymongo
# # client = pymongo.MongoClient("mongodb+srv://youtubePy:youtubePy@cluster0.1nva8dt.mongodb.net/ytmanager")
# #whatever we write after / is the name of db "ytmanager"

# from pymongo import MongoClient
# #when we write ths way we dont have to write pymongo in client
# client = MongoClient("mongodb+srv://youtubePy:youtubePy@cluster0.1nva8dt.mongodb.net/", tls = True)
# #not a good way handle ssl
# #but this is not a good practice to include id pass in url itself
# print(client)
# #also a good practice to stor edb name in db variable then use it anywhere
# db = client["ytmanager"]


# #creating collections
# #collection will be reflected in mongodb only when you add data 
# video_collection = db["videos"]
# print(video_collection)

# def list_video():
#     #'find' returns iterable obj
#     for video in video_collection.find():
#         print(f"ID: {video['_id']}, Name:{video['name'], Time: {video['time']}}")
    
# def Add_video(name, time):
#     video_collection.insert_one({"name": name, "time": time})
# def Update_video(video_id, new_name, new_time):
#     video_collection.update_one({'_id': video_id},{"$set": {"name": new_name, "time": new_time}})
# def Delete_video(video_id):
#     video_collection.delete_one({"_id": video_id})

# def main():
#     while True:
#         print("\n Youtube manager App")
#         print("1. list all videos ")
#         print("2. Add a new video")
#         print("3. Update a video")
#         print("4. Delete a video")
#         print("5. Exit the app")
#         choice = input("enter your choice: ")

#         if choice == '1':
#             list_video()
#         elif choice == '2':
#             name = input("enter video name: ")
#             time = input("enter video time: ")
#             Add_video(name, time)
#         elif choice == '3':
#             id = input("enter video id: ")
#             name = input("enter updated video name: ")
#             time = input("enter updated video time: ")
#             Update_video(id, name, time)
#         elif choice == '4':
#             id = input("enter video id: ")
#             Delete_video(id)
#         elif choice == '5':
#             break
#         else:
#             print("invlid choice:")

# if __name__ == "__main__":
#     main()