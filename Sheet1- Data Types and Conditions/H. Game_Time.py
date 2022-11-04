GameStartTime = eval (input("Enter the start time of the game:"))
GameEndTime = eval (input("Enter the end time of the game:"))
if GameEndTime > GameStartTime:
    print("THE GAME LASTED" , (GameEndTime - GameStartTime) , "HOUR(S)")
else:
    print("THE GAME LASTED", 24 - (GameStartTime - GameEndTime), "HOUR(S)")
