your_dog = input("What's your dog's name? Enter here: ").capitalize()
dog_gender = str(input("Is your dog a boy or a girl? Enter here: "))
dog_adjective = input("Describe your pooch with one adjective: ").lower()
dog_action = input("Something your pooch likes doing: ").lower()


if dog_gender == str("girl" or "Girl" or "GIRL" or "female" or "Female" or "FEMALE"):
        print("{} is a {} pooch. She also likes {}.".format(your_dog, dog_adjective, dog_action))
elif dog_gender == "boy" or "Boy" or "BOY" or "male" or "Male" or "MALE":
        print("{} is a {} pooch. He also likes {}.".format(your_dog, dog_adjective, dog_action))