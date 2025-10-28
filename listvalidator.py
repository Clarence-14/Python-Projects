# A program that lets the user add items to a shopping list in a loop, validating inputs (e.g., no empty items) and allowing quit with "done".

items = [None]
while items[-1] != "done":
    item = input("Enter an item to add to your shopping list (or type 'done' to finish): ")
    if item == "done":
        break
    elif item.strip() == "":
        print("Item cannot be empty. Please enter a valid item.")
    else:
        items.append(item)
if len(items) > 1:
    print("Your shopping list:")
    for i in items[1:]:
        print(f"- {i}")
