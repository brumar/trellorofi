import sys
import random
import webbrowser

from rofi import Rofi
from trello import Card, TrelloClient

from settings import ACTION_LIST, INBOX_LIST, PROCESS_LIST, NOTES_LIST, API_KEY, API_SECRET, TOKEN


# Monkey patching Trello Card so that __str__ is more practical
Card.__str__ = lambda instance: instance.name

# Monkey patching show > error
Rofi.show = Rofi.error


options = ("notes", "inbox", "work")

if "" in (API_KEY, API_SECRET, TOKEN):
    sys.exit("Incorrect Configuration, please go to https://trello.com/app-key and fill settings.py accordingly")


client = TrelloClient(
    api_key=API_KEY,
    api_secret=API_SECRET,
    token=TOKEN
)


def more_info(card):
    name = card.name
    labels = [label.name for label in card.labels]
    desc = card.description
    return "\n".join([name, "labels: " + ", ".join(labels), desc])

if __name__ == "__main__":
    r = Rofi()
    option = r.select(prompt="action: ", options=options).selection

    if option == "work":
        cards = client.get_list(ACTION_LIST).list_cards()
        random.shuffle(cards)
        selected_card = r.select(options=cards).selection
        if selected_card is not None:
            choice = r.select(options=('show', 'open', "select")).selection
            if choice is not None:
                if choice == "show":
                    info = more_info(selected_card)
                    r.show(info)
                    choice, key = r.select(options=('open', "select"))
                if choice == "open":
                    webbrowser.open(selected_card.url, new=1, autoraise=True)
                if choice == "select":
                    selected_card.change_list(PROCESS_LIST)
                    r.show("card has moved to PROCESS_LIST")

    if option == "inbox":
        text = r.text_entry(prompt="short description: ")
        client.get_list(INBOX_LIST).add_card(text)
        r.show("card added")

    if option == "notes":
        text = r.text_entry(prompt="text: ")
        client.get_list(NOTES_LIST).add_card(text)
        r.show("card added")
