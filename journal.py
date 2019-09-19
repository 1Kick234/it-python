from banner import banner
banner("Deep Thoughts", "Gavin Orcutt")

def main():
    run_event_loop()

def run_event_loop():
    print("What do you want to do with your journal?")
    command = "J"
    journal_data = []

    while command.upper() != "E":
        command = input("[L]ist entries, [A]dd an entry, [E]xit: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() != "E":
            print("Input not recognized.")

def list_entries(data):
    print("Your journal entries:")
    for number, entry in enumerate(data):
        print(f"{number+1}. {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exist: ")
    data.append(entry)

main()