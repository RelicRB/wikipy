import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

while True:
    query = input("\nPlease enter a topic: ")

    topic_pg = wiki_wiki.page(query)

    if not topic_pg.exists():
        print("Sorry, that topic could not be found. Please try again.")
        continue

    print("\nWhat would you like to see?")
    print("1. Summary only")
    print("2. Page sections")

    while True:
        try:
            choice = int(input("\nPlease enter a number: "))
            if choice not in [1, 2]:
                print("Invalid input. Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        print("\n" + topic_pg.summary)
    else:
        print("\nSections:")
        for i, section in enumerate(topic_pg.sections, start=1):
            print(f"{i}. {section.title}")
        while True:
            try:
                choice = int(input("\nPlease choose a section (enter a number): "))
                if choice not in range(1, len(topic_pg.sections)+1):
                    print("Invalid input. Please enter a valid section number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        chosen_section = topic_pg.sections[choice-1]
        print("\n" + chosen_section.text)
