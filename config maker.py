import os

def create_file(file_name, content):
    if not os.path.exists("config"):
        os.mkdir("config")

    if os.path.exists(file_name):
        os.remove(file_name)
        print("[ ! ] An Existing config found, Overwriting.. ")
    
    with open(file_name, 'w') as file:
        file.write(content)

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("[ ! ] Please enter a valid integer.")


print("""



                             ██╗░░░░░██╗████████╗██╗░░██╗██╗██╗░░░██╗███╗░░░███╗
                             ██║░░░░░██║╚══██╔══╝██║░░██║██║██║░░░██║████╗░████║
                             ██║░░░░░██║░░░██║░░░███████║██║██║░░░██║██╔████╔██║
                             ██║░░░░░██║░░░██║░░░██╔══██║██║██║░░░██║██║╚██╔╝██║
                             ███████╗██║░░░██║░░░██║░░██║██║╚██████╔╝██║░╚═╝░██║
                             ╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝   [ V 4 ]


                                   Config Maker - (made in py cuz i am lazy)


""")
webhook_message_content = input("[ ? ] Webhook Message: ")
webhook_amount_content = get_integer_input("[ ? ] Webhook Message Amount: ")
channel_names_content = input("[ ? ] Channel Names: ")
channel_amount_content = get_integer_input("[ ? ] Channel Amount: ")
role_names_content = input("[ ? ] Role Names: ")
role_amount_content = get_integer_input("[ ? ] Role Amount: ")

create_file("config/webhookmessage.txt", webhook_message_content)
create_file("config/webhookamount.txt", str(webhook_amount_content))
create_file("config/channelnames.txt", channel_names_content)
create_file("config/channelamount.txt", str(channel_amount_content))
create_file("config/rolenames.txt", role_names_content)
create_file("config/roleamount.txt", str(role_amount_content))

input("[ ! ] Config complete. Press enter to close..")