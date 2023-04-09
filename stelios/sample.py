"""
Όταν γράφεις multiline comment μέσα σε τρία double quotes, δε θεωρείται σχόλιο αλλά docstring (documentation string),
δηλαδή περιγραφή λειτουργικότητας. Docstring μπορούμε να γράψουμε αμέσως μετά τη δήλωση μιας μεταβλητής, στην αρχή
μιας κλάσης, στην αρχή μιας συνάρτησης ή στο πάνω μέρος ενός module, όπως εδώ. Μπορεί να γραφτεί όσο μεγάλο χρειάζεται,
για να εξηγεί στους χρήστες τι δηλώνει η μεταβλητή, πως πρέπει να χρησιμοποιούν την κλάση / συνάρτηση ή ποια είναι
τα περιεχόμενα του module.
Στο PyCharm, κάνοντας hover το ποντίκι πάνω από το όνομα μιας κλάσης βλέπεις ένα preview του docstring, αν υπάρχει.

ΣΗΜΕΙΩΣΗ: Το typing είναι builtin module με εργαλεία για να εξηγούμε τι είδους είναι η κάθε μεταβλητή, τι επιστρέφει
η κάθε συνάρτηση κλπ. Είναι μόνο για τη δική μας διευκόλυνση, ΔΕΝ επηρεάζει την εκτέλεση του προγράμματος.
"""

import tkinter as tk
from typing import NoReturn, Callable
import winsound

from assets import Constants, Character, Characters

class ApplicationScreen:

    # Αυτή η κλάση θα αντιπροσωπεύει την κάθε οθόνη της εφαρμογής. Το κουμπί της εξόδου, το φόντο και άλλα
    # χαρακτηριστικά που θα είναι κοινά σε πολλές οθόνες, μπορούν να μπουν εδώ.

    def __init__(self) -> NoReturn: ...


class Application(tk.Tk):

    """
    This is the basic class of the application, inheriting tkinter.Tk.
    """

    CONSTANTS: Constants = Constants()

    def __init__(self) -> NoReturn:
        super().__init__()  # ---------------------------------------------------------------------- call to superclass
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.attributes('-fullscreen', True)
        self.characters: Characters = Characters()  # -------- container of Character objects, accessed by dot notation
        # self.bind('<Control-x>', self.quit)  # --------------------------------- first try to have keyboard shortcuts
        self.start_screen()
        self.mainloop()
        return

    def clear_screen(self) -> NoReturn:
        for widget in self.winfo_children(): widget.destroy()

    def home_button(self) -> NoReturn:
        tk.Button(self, text="Home", command=self.start_screen).place(x=1880, y=25)

    def quit_button(self) -> NoReturn:
        tk.Button(self, text="Quit", command=self.quit).place(x=1880, y=5)

    def loading_screen(self) -> NoReturn: ...

    def start_screen(self) -> NoReturn:

        def button(text: str, command: Callable) -> tk.Button:
            # ------------------------------------- this nested function produces reusable code (DON'T REPEAT YOURSELF)
            return tk.Button(bg_label, text=text, font=self.CONSTANTS.BUTTON_FONT, bg='white', command=command)

        # Load the background image
        bg_label = tk.Label(self, image=tk.PhotoImage(file="background.png"))
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a label with larger font size
        label = tk.Label(bg_label, text="Welcome to LoisRealm", font=("Roman", 56), fg='white')
        label.pack()

        # Add three buttons to the interface

        button("Start game", self.character_selection_screen).place(x=550, y=500)
        button("Settings", self.settings_screen).place(x=550, y=600)
        button("Exit", self.quit).place(x=550, y=700)  # -- Γιατί έχεις κουμπιά QUIT και EXIT? Να βγάλεις το ένα

        self.quit_button()  # ---------------------------------------------------------------------------- quit program
        return

    @staticmethod
    def settings_screen() -> NoReturn:
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        return

    def character_selection_screen(self) -> NoReturn:

        def character_button(character_object: Character) -> tk.Button:  # ---------------- also produces reusable code
            return tk.Button(self, text=character_object.name, font=("Arial", 56), bg='white',
                             command=lambda: self.character_screen(character_object))

        self.clear_screen()  # ------------------------------------------------------------------ clear the main screen

        # Create the character creation screen
        character_label = tk.Label(self, text="Create your character", font=("Roman", 56), fg='yellow')
        character_label.place(x=200, y=1000)

        # background for character creation
        bg_image = tk.PhotoImage(file="background.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # bg_color = bg_image.get(0, 0)  # ---------------------------------------------- δεν το χρησιμοποιείς πουθενά!

        self.quit_button()  # ---------------------------------------------------------------------------- quit program

        coordinate_x: int = 50
        for character in self.characters:
            character_button(character).place(x=coordinate_x, y=100)
            coordinate_x += 600  # Από εδώ ρυθμίζεις πόσο θα απέχουν τα κουμπιά
        return

    def character_screen(self, character: Character) -> NoReturn:
        # Η συγκεκριμένη οθόνη της εφαρμογής εξαρτάται μόνο από το κάθε Character.
        # Φροντίζουμε τα απαραίτητα δεδομένα να περιλαμβάνονται στα αντικείμενα Character.

        self.clear_screen()  # ------------------------------------------------------------------ clear the main screen

        self.configure(background='red')
        image = tk.PhotoImage(file=character.file_path)
        label = tk.Label(self, image=image)
        label.place(x=50, y=50)
        winsound.PlaySound(character.sound_path, winsound.SND_ASYNC)
        text = tk.Label(self, text=character.text, font=self.CONSTANTS.STANDARD_FONT,
                        fg='black', background='red')
        text.place(x=450, y=200)
        stats = tk.Label(self, text=character.stats, font=self.CONSTANTS.STANDARD_FONT,
                         fg='black', background='red')
        stats.place(x=450, y=500)
        extra = tk.Label(self, text="SPECIAL SKILL:\n" + character.extra, font=self.CONSTANTS.STANDARD_FONT,
                         fg='black', background='orange')
        extra.place(x=850, y=500)

        back_button = tk.Button(text="Back", font=self.CONSTANTS.BUTTON_FONT, bg='white',
                                command=self.character_selection_screen)
        back_button.place(x=1650, y=1000)

        continue_button = tk.Button(text="Continue", font=self.CONSTANTS.BUTTON_FONT, bg='white')
        continue_button.place(x=1750, y=1000)

        self.quit_button()  # ---------------------------------------------------------------------------- quit program
        return


if __name__ == '__main__': Application()
