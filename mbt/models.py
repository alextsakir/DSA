"""                                           Sunday 19 Mar 2023

Εφαρμογή που τρέχει από browser (web application) και οι χρήστες συνδέονται για να τη χρησιμοποιήσουν.
Λειτουργίες: Δημιουργία νέου χρήστη (sign up), λειτουργία σύνδεσης υπάρχοντος χρήστη (sign in).

        ΚΑΤΗΓΟΡΙΕΣ ΧΡΗΣΤΩΝ:              SUPERUSER                              USER

                                    Ο διαχειριστής της                  Οι υπόλοιποι χρήστες
                                  φαρμακευτικής εταιρείας

        ΕΡΩΤΗΜΑΤΟΛΟΓΙΑ                 Τα δημιουργεί                         Τα απαντούν

    ===============================================================================================

Ο διαχειριστής έχει τη δυνατότητα να αναρτά ανακοινώσεις, όπως όταν υπάρχει ένα νέο ερωτηματολόγιο διαθέσιμο.
Το κάθε ερωτηματολόγιο είναι σύνολο ερωτήσεων που συντάσσονται μόνο από τον διαχειριστή και συμπληρώνονται από τους
υπόλοιπους χρήστες. Η κάθε ερώτηση μπορεί να είναι πολλαπλής επιλογής ή ανάπτυξης.

Θα είναι ανώνυμο για τους χρήστες; (ο διαχειριστής θα μπορεί να βλέπει τις απαντήσεις του καθενός;).

Η εφαρμογή υπολογίζει στατιστικά πάνω στα αποτελέσματα, τα οποία μπορούν να βλέπουν όλοι.
"""

from dataclasses import dataclass
from datetime import date, timedelta
from random import choice, randint, randrange
from typing import NoReturn, Optional, List, Tuple, TypeVar, Type

from enumerations import *

_ADT = TypeVar("_ADT", str, int)  # NOTABLE
"""
Custom Type Variable indicating data types of answers: str or int.
"""

class MetaUser:

    """Class MetaUser
    Subclassed by: Administrator, SimpleUser, Doctor
    Represents a single User object.
    You are not supposed to create MetaUser objects. You should use subclasses instead.
    TODO COMPLETE
    """

    @dataclass
    class Name:  # ADDED ON 22 Mar 2023

        first: str
        last: str
        father: str

    __slots__: Tuple[str] = ("name", "email", "username", "__password", "sex",
                             "birth_date", "created_at", "type", "__phone")

    @classmethod
    def __new__(cls, *args, **kwargs) -> NoReturn: return None  # NOTABLE -> TO PREVENT FROM CREATING META-USER OBJECTS

    def __init__(self, first_name: Optional[str] = None,
                 last_name: Optional[str] = None, father_name: Optional[str] = None,
                 sex: Optional[Sexes] = Sexes.OTHER, username: Optional[str] = None,
                 password: Optional[int] = None, user_type: UserTypes = UserTypes.OTHER,
                 birth_date: Optional[date] = None, telephone: Optional[int] = None) -> NoReturn:
        self.name: MetaUser.Name = MetaUser.Name(first=first_name, last=last_name, father=father_name)
        self.email: Optional[str] = None
        self.username: str = username
        self.__password: int = password
        self.birth_date: Optional[date] = birth_date
        self.created_at: date = date.today()
        self.type: UserTypes = user_type
        self.sex: Sexes = sex
        self.__phone: Optional[int] = telephone
        # assert self.email_checker() and self.telephone_checker()  # PROBLEM ------------------------ IS IT NECESSARY?
        return

    def __str__(self) -> str:
        out: str = self.type.value
        if self.name.first is not None: out += " " * (10 - len(out)) + "|" + " " * 5 + self.name.first
        if self.name.last is not None: out += " " * (30 - len(out)) + self.name.last
        if self.name.father is not None: out += " " * (45 - len(out)) + self.name.father
        if self.username is not None: out += " " * (60 - len(out)) + self.username
        if self.__password is not None: out += " " * (80 - len(out)) + str(self.__password)
        if self.birth_date is not None: out += " " * (95 - len(out)) + str(self.birth_date)
        return out

    @classmethod
    def get_type(cls, user_type: UserTypes) -> Optional[Type["MetaUser"]]:
        for subclass in cls.__subclasses__():
            if subclass().type == user_type: return subclass
        return None

    @staticmethod
    def tabs() -> str:
        out: str = "GROUP" + " " * 5 + "|" + " " * 5 + "FIRST_NAME" + " " * 4 + "LAST_NAME" + " " * 6 + "FATHER_NAME"
        return out + " " * 4 + "USERNAME" + " " * 12 + "PASSWORD" + " " * 7 + "BIRTH_NAME" + "\n" + "=" * 105

    @property
    def age(self) -> int:
        age: int = date.today().year - self.birth_date.year
        if self.birth_date.month < date.today().month and self.birth_date.day < date.today().day: age -= 1
        return age

    @property
    def telephone(self) -> str:
        return "+30_" + str("_").join([str(self.__phone)[0: 3], str(self.__phone)[3: 6], str(self.__phone)[6:]])

    def credentials(self, username: Optional[str] = None, password: Optional[int] = None) -> NoReturn:
        self.username, self.__password = username, password
        return

    def email_checker(self, email: Optional[str] = None) -> bool:
        if not email and not self.email: return False
        if not self.email: self.email = email
        email: str = email.lower().replace(" ", "")
        if email.count("@") != 1 or not email.endswith((".gr", ".com")): return False
        for char in email:
            if ord(char) < 45 or ord(char) > 122: return False
        return True

    def telephone_checker(self, telephone: Optional[int] = None) -> bool:
        if not telephone and not self.__phone: return False
        if not self.__phone: self.__phone = telephone
        if len(str(telephone)) > 10: telephone = telephone[-10:]
        if len(str(telephone)) != 10 or not str(telephone)[0:2] == "69": return False
        return True

class Administrator(MetaUser):

    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None,
                 father_name: Optional[str] = None,
                 username: Optional[str] = None, password: Optional[str] = None) -> NoReturn:
        super().__init__(first_name, last_name, father_name, username, password)
        self.type = UserTypes.ADMIN
        return

    def create_questionnaire(self) -> NoReturn: ...

    def create_question(self) -> NoReturn: ...

    def create_multiple_choice(self) -> NoReturn: ...

    def create_open_ended(self) -> NoReturn: ...

class SimpleUser(MetaUser):

    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None,
                 father_name: Optional[str] = None,
                 username: Optional[str] = None, password: Optional[str] = None) -> NoReturn:
        super().__init__(first_name, last_name, father_name, username, password)
        self.type = UserTypes.USER
        return

class Doctor(MetaUser):

    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None,
                 father_name: Optional[str] = None,
                 username: Optional[str] = None, password: Optional[str] = None) -> NoReturn:
        super().__init__(first_name, last_name, father_name, username, password)
        self.type = UserTypes.DOCTOR
        return

class Generator:

    __slots__: Tuple[str] = ("__names", "__words")

    @classmethod
    def __new__(cls, *args, **kwargs) -> "Generator": return super().__new__(cls)  # NOTABLE ------------ TO BE REMOVED

    def __init__(self) -> NoReturn:
        self.__names: List[str] = self.names()  # PROBLEM --------------------------------- CHECK IMPORT OF typing.List
        self.__words: List[str] = self.common_words()
        return

    @staticmethod
    def common_words() -> List[str]:
        words: List[str] = list()
        with open("D:/text/common_english_words.txt", 'r', encoding="utf-8") as file:
            for line in file.readlines():
                word: str = str()
                for character in line:
                    if character.isalpha(): word += character
                words.append(word)
        return words

    def username(self) -> str: return choice(self.__words) + choice(self.__words).capitalize() + str(randint(5, 95))

    @staticmethod
    def date() -> date:
        delta: timedelta = date(2005, 12, 31) - date(date.today().year - 100, 1, 1)
        random_second = randrange((delta.days * 24 * 60 * 60) + delta.seconds)
        return date(1960, 1, 1) + timedelta(seconds=random_second)

    @staticmethod
    def names() -> list[str]:
        names: List[str] = list()
        with open("D:/text/greek_names.txt", 'r', encoding="utf-8") as file:
            for line in file.readlines():
                name: str = str()
                for character in line:
                    if character.isalpha(): name += character
                names.append(name)
        return names

    def user(self, user_type: Optional[UserTypes] = None) -> MetaUser:
        user: MetaUser = MetaUser(birth_date=self.date())
        user.name.first = choice(self.__names)
        user.name.last = choice(self.__names)
        user.name.father = choice(self.__names)
        user.type = user_type if user_type is not None else choice(UserTypes.members())
        user.credentials(username=self.username(), password=randint(1000, 9999))
        return user

    def users(self, amount: int, user_type: Optional[UserTypes] = None) -> list[MetaUser]:
        return [self.user(user_type=user_type) for _ in range(amount)]

class Question:

    __slots__: Tuple[str] = ("questionnaire", "presentation", "type", "answers")

    def __init__(self) -> NoReturn:
        self.questionnaire: Optional[Questionnaire] = None
        self.presentation: Optional[str] = None
        self.type: Optional[QuestionTypes] = None
        self.answers: List[str] = list()  # TODO -------------------------------------------------------- TO BE CHECKED
        return

    def __repr__(self) -> str: ...  # TODO ------------------------------------------------------------------ IMPLEMENT

    def __str__(self) -> str: ...  # TODO ------------------------------------------------------------------- IMPLEMENT

class MultipleChoice(Question):

    def __init__(self) -> NoReturn:
        super().__init__()
        self.type = QuestionTypes.MULTIPLE_CHOICE
        return

class OpenEndedQuestion(Question):

    def __init__(self) -> NoReturn:
        super().__init__()
        self.type = QuestionTypes.OPEN_ENDED
        return

class Answer:

    __slots__: Tuple[str] = ("user", "question", "data")

    def __init__(self, user: MetaUser, question: Question, data: _ADT) -> NoReturn:
        self.user: MetaUser = user
        self.question: Question = question
        self.data: _ADT = data
        return

    def __str__(self) -> str: return "ANSWER OF USER " + repr(self.user) + " FOR QUESTION " + repr(self.question)

    @property
    def type(self) -> QuestionTypes: return self.question.type

    @property
    def questionnaire(self) -> "Questionnaire": return self.question.questionnaire

class Questionnaire:

    __slots__: Tuple[str] = ("name", "description", "questions")

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None) -> NoReturn:
        self.name: Optional[str] = name
        self.description: Optional[str] = description
        self.questions: List[Question] = list()
        return

    def get(self, question_type: Optional[QuestionTypes] = None) -> Optional[List[Question]]:
        if question_type == QuestionTypes.MULTIPLE_CHOICE: return self.multiple_choice()
        if question_type == QuestionTypes.OPEN_ENDED: return self.open_ended()
        return None

    def multiple_choice(self) -> Optional[List[Question]]:
        questions: List[Question] = list()
        for question in self.questions:
            if question.type == QuestionTypes.MULTIPLE_CHOICE: questions.append(question)
        if not len(questions): return None
        return questions

    def open_ended(self) -> Optional[List[Question]]:
        questions: List[Question] = list()
        for question in self.questions:
            if question.type == QuestionTypes.OPEN_ENDED: questions.append(question)
        if not len(questions): return None
        return questions


__all__ = ["Administrator", "SimpleUser", "Doctor", "Generator", "MultipleChoice", "OpenEndedQuestion", "Questionnaire"]

if __name__ == "__main__": print(__all__)
