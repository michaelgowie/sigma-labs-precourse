animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"},
    {"name": "Poppet", "type": "Cow"}
]


def say_hello_to_pets(pets):
    for pet in pets:
        hello_message = ""
        if pet["type"] == "dog":
            hello_message = "Woof"
        elif pet["type"] == "cat":
            hello_message = "meow"
        else:
            raise Exception('The type must either cat or dog.')
        pet_name = pet["name"]
        print(f"{hello_message}, {pet_name}!")


if __name__ == "__main__":
    say_hello_to_pets(animals)
