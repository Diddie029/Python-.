responses = {
    "hi" , "hey": "Hello there! How's ur day ?",
    "How are you": "I'm just a bunch of python code, but I'm doing great ",
    "bye": "Goodbe ! keep coding .",
}
while True:
    user_input = input("You:").lower()
    if user_input in responses:
        print("Bot:", responses[user_input])
    elif user_input == "exit":
        print("Bot: Shuttind down....")
        break 
    else:
        print("Bot: I don't know that yet...I'll let my developer Diddie know that.")