import os


if not os.path.exists('.env'):
    env = open(".env", "w")

    print("------")    
    print('Welcome to your leveling system bot setup.')
    print("------")    

    # TOKEN
    print('Your bot\'s token can be obtained from https://discord.com/developers/applications.')
    token = input('Bot token: ')
    env.write(f"TOKEN={token}\n")
    print("------")


    # Close File
    env.close()

    print('All done, enjoy your bot.')

else:
    print("You already done this before")
