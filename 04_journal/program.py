import journal

def main():
    print_header()
    run_event_loop()

def print_header():
    print("------------------------------------")
    print("       JOURNAL APP                  ")
    print("------------------------------------")
    print()

def run_event_loop():

    print("What do you want to do? ")
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:  #means "AND the command is NOT empty"
        cmd = input ("[L]ist entries, [A]dd an entry, E[x]it:  ")
        cmd = cmd.lower().strip()
        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'".format(cmd))
    print("Done. Goodbye.")
    journal.save(journal_name,journal_data)

def list_entries(data):
    print("Your journal entries:")
    entries = enumerate(reversed(data))
    for idx, entry in entries:
        print('* [{}] {} '.format(idx+1,entry))

def add_entry(data):
    text = input("Type your entry, <enter> to exit:  ")
    journal.add_entry(text, data)

print("__file__ = " + __file__)
print("__name__ = " + __name__)
# main()

if __name__ == '__main__':
    main()

