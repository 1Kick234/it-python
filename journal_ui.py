import journal
from banner import banner
banner("Deep Thoughts", "Gavin Orcutt")

def main():
    run_event_loop()

def run_event_loop():
    filename = input("What should we call your journal file? ")
    print("What do you want to do with your journal?")
    command = "J" # J is Placeholder.
    journal_data = journal.load(filename)

    while command.upper() != "E":
        command = input("[L]ist entries, [A]dd an entry, [E]xit: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() != "E":
            print("Input not recognized.")

    journal.save(filename, journal_data)

def list_entries(data):
    print("Your journal entries:")
    for number, entry in enumerate(data):
        print(f"{number+1}. {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: ")
    journal.add_entry(entry, data)
    # data.append(entry)

main()