import random

class HospitalAssistant:
    def __init__(self):
        self.greetings = ["Hello! How can I assist you today?",
                          "Welcome to our hospital. How can I help you?",
                          "Hi there! What brings you here today?"]
        self.goodbyes = ["Goodbye! Take care.",
                         "Hope you feel better soon. Goodbye!",
                         "See you later. Have a nice day!"]
        self.thanks = ["You're welcome!",
                       "Glad I could help!",
                       "No problem, happy to assist!"]
        self.options = ["1. Schedule an appointment",
                        "2. Inquire about medical services",
                        "3. Check visiting hours",
                        "4. Exit"]

    def greet(self):
        return random.choice(self.greetings)

    def say_goodbye(self):
        return random.choice(self.goodbyes)

    def respond_to_thanks(self):
        return random.choice(self.thanks)

    def display_options(self):
        return "\n".join(self.options)

    def handle_user_input(self, choice):
        if choice == '1':
            return "Please provide details for scheduling the appointment."
        elif choice == '2':
            return "What specific medical service are you inquiring about?"
        elif choice == '3':
            return "Our visiting hours are from 9 AM to 5 PM, Monday to Friday."
        elif choice == '4':
            return "exit"
        else:
            return "I'm sorry, I didn't understand your choice. Please try again."

def main():
    assistant = HospitalAssistant()
    print(assistant.greet())

    while True:
        print(assistant.display_options())
        choice = input("Please enter the number of your choice: ")
        response = assistant.handle_user_input(choice)
        
        if response == "exit":
            print(assistant.say_goodbye())
            break
        else:
            print(response)

if __name__ == "__main__":
    main()
