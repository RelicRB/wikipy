import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
query = input("Query/Topic: ")
topic_pg = wiki_wiki.page(query)

if topic_pg.exists():
    print(" \n What would you like?: \n 1. Summary only \n 2. Page Sections")
    print("\n Choose a number: ")
    choice = int(input())
    if choice == 1:
           print("\n" , topic_pg.summary)
    else:
       print("\n Sections: ")
       for section in topic_pg.sections:
                print("\n",section.title)
       print("\n Chose a section")
       sec_title = input("")
       section = topic_pg.section_by_title(sec_title)
       if section:
             print("\n", section.text)
       else:
             print("Invalid section name")

