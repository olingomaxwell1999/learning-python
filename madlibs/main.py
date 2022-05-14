verb = input("Please input an action (verb): ")
noun = input("Please input an  noun: ")
possessive_noun = input("Please state a possessive noun (example : Father's): ")
event = input("What is an event that you have been to?: ")

paragraph = "I have never seen this uncle but i am supposed to {}\
    like him with special reference to the rather hard boiled\
        {} that things in {} office. I graduated from Nairobits\
            in 2021, just a quater century after my father\
                and a little later I participated in that delayed Toutonic migration known as the {}".format(verb, noun, possessive_noun, event)

print("Here is your madlibs...")

print(paragraph)