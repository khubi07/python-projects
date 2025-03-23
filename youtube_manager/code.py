




while True:
    print("\n Youtube Manager | choose an option")
    print("\n 1. list all youtube videos")
    print("\n 2. Add a youtube video")
    print("\n 3. Update a youtube video detail")
    print("\n 4. Delete a youtube video")
    print("\n 5. Exit the app")
    
    choice = input("enter your choice(1-5): ")
    #if choice == "1" instead of this we can write match

    match choice:
        case'1':
            list_all_videos(video)