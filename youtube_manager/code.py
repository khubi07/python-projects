import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    #used enumerate for indexing
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):#directly loop laga diye enum ke uper
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)


def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("enter new video name: ")
        time = input("enter new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to be deleted: "))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")
        

def main(): #industrial method to start prohram 
    videos = load_data() #brings data from file
    while True:
        print("\n Youtube Manager | choose an option")
        print("\n 1. list all youtube videos")
        print(" 2. Add a youtube video")
        print(" 3. Update a youtube video detail")
        print(" 4. Delete a youtube video")
        print(" 5. Exit the app")
       

        choice = input("enter your choice(1-5): ")
        # print(videos)
        #if choice == "1" instead of this we can write match


        match choice:
            case'1':
                list_all_videos(videos)
            case'2':
                add_video(videos)
            case'3':
                update_video(videos)
            case'4':
                delete_video(videos)
            case'5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()