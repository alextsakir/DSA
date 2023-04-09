from typing import NoReturn, Union, Iterable, Final

_FONT = tuple[str, int]  # ---------------------- here we define a special data type, like this tuple describing a font

class Constants:

    """
    Here you put any constants you will use in the application, so you don't have to write them each time.
    """

    STANDARD_FONT: Final[_FONT] = ("Arial", 24)  # --------- Final will ensure no one will change values by mistake :-)
    BUTTON_FONT: Final[_FONT] = ("Arial", 20)

class Character:

    """
    Class that represents each character of the game and stores all relative information.
    """

    def __init__(self, name: str, strength: int, intelligence: int,
                 luck: int, stamina: int, speed: int,
                 social_skills: int, knowledge: int) -> NoReturn:
        self.name: str = name
        self.strength: int = strength
        self.intelligence: int = intelligence
        self.luck: int = luck
        self.stamina: int = stamina
        self.speed: int = speed
        self.social_skills: int = social_skills
        self.knowledge: int = knowledge
        self.text: str = "I don't have a description yet!"
        self.extra: str = "I don't have any extra features!"
        self.file_path: str = str()  # ---------------------------------- we should have a default character image here
        self.sound_path: str = str()  # -------------------------------------------- we should have a sample sound here
        self.bg_color: str = str()
        return

    def __str__(self) -> str:
        out: str = "Character " + self.name + "\n"
        for key, value in self.dict.items():
            if isinstance(value, int): out += key + ": " + str(value) + "\t\t"

        return out

    @property
    def dict(self) -> dict[str, Union[str, int]]: return self.__dict__  # ------------ Union[str, int] means str OR int

    @property
    def stats(self) -> str: return "Not Implemented"  # FIXME


class Characters:

    """
    Container class that holds all the Character objects.

    You can get each player by dot notation: <characters_object>.<character_name>

    You can also iterate through all characters in a for loop: for character in <characters_object>: print(character)
    """

    def __iter__(self) -> Iterable[Character]:  # ----------------- dunder method that makes Characters object iterable
        for value in self.__dict__.values():  # NOTABLE: dunder means double-underscore, method that starts with __...
            if isinstance(value, Character): yield value

    def __init__(self) -> NoReturn:
        self.george = Character("george", 6, 9, 2, 2, 8, 8, 10)
        self.george.text = "This is Gkotsopoulos!\n Gkotsopoulos is an angry beast. He hates many things but most of"\
                           " all he hates Patra.\nHe usually wants to die and he sleep at random times during the day."
        self.george.extra = "With this champion you have the ability to win even if you lose.\n But be careful " \
                            "because if you are unlucky you might always lose"
        self.george.file_path = "gkotso.png"
        self.george.sound_path = "Recording (32).wav"
        self.george.bg_color = "red"  # ------------------- να μου πεις τι χρώματα χρειάζεται να έχει ο κάθε χαρακτήρας

        self.spyros = Character("spyros", 10, 9, 8, 4, 2, 2, 8)
        self.spyros.text = "Spyros is a strong warrior when he is not sleeping.\n He usually sleeps but when he is"\
                           " awake he is quite strong.\n Give him pizzas and crepes and he will be happy, don't" \
                           "forget to wake him up"
        self.spyros.extra = "With this champion you have the ability to say <<i will come back later>>\n"\
                            " and there come back with full hp"
        self.spyros.file_path = "spyros.png"
        self.spyros.sound_path = "Recording.wav"
        self.spyros.bg_color = "purple"

        self.nikos = Character("nikos", 0, 0, 0, 0, 0, 0, 0)  # TODO ---------------------------------- TO BE COMPLETED
        self.nikos.text = "add a description"
        self.nikos.extra = "add an extra feature"
        self.nikos.file_path = "image name"
        self.nikos.sound_path = "sound name"
        self.nikos.bg_color = "add a color"
        return


if __name__ == "__main__":
    # Το σημείο αυτό εκτελείται μόνο όταν τρέχεις το αρχείο μόνο του.
    # Όταν γίνεται import αλλού, οι γραμμές από εδώ και κάτω αγνοούνται.

    for char in Characters(): print(char)
