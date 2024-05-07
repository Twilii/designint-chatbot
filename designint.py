def greeting():
    name = input("Thanks for contacting DesignINT! May I have your name? ").capitalize()
    print(f"Thanks, {name}!")
    return

def select_category():
    category = input("""Please select from one of the categories below using the numbers 1-5.
[1] Store hours & locations\n[2] Status of order\n[3] Issue with order\n[4] Design services\n[5] Other\n""")

    if category == "1":
        store_location_hours()
        return

    if category == "2":
        order_status()
        return

    if category == "3":
        order_issue()
        return

    if category == "4":
        design_services()
        return

    if category == "5":
        other()
        return

    if category not in ["1", "2", "3", "4", "5"]:
        print("Please respond with the proper number for your inquiry.")
        select_category()

def store_location_hours():
    location = "5600 Waterfall Drive, Toronto, ON M5V 3L9"
    hours = "Monday - Saturday from 8AM to 6PM"
    print(f"DesignINT is located at {location}. The store is open {hours}.")
    additional_question = input("May I help you with anything else? [Y/N] ").capitalize()
    if additional_question == "Y":
            select_category()
    elif additional_question == "N":
            print("Thanks for contacting DesignINT!")
    else:
            print("""Please respond with either "Y" or "N".""")

def order_status():
    print("Sure, I can help you with that.")
    full_name = input("May I have the full name on the order? ")
    order_number = input("May I have the order number? ")
    transfer_ordersTeam()
    return

def order_issue():
    print("I'm sorry that you're experiencing issues with your order.")
    full_name = input("May I have the full name on the order? ")
    order_number = input("May I have the order number? ")
    issue = input("Could you please describe the issue with your order? ")
    transfer_issuesTeam()
    return

def design_services():
    print("I can definitely help you out with your design questions!")
    transfer_designTeam()
    return

def other():
    transfer_other()
    return

def transfer_ordersTeam():
    print("Awesome! I'm checking the status of the order now.")
    return

def transfer_issuesTeam():
    print("Thanks for providing that information. I'm looking into this now.")
    return

def transfer_designTeam():
    design_question = input("Tell me how I may be of assistance. ")
    return

def transfer_other():
    other_inquiry = input("No problem, please describe how I may be of assistance. ")
    return

greeting()
select_category()
