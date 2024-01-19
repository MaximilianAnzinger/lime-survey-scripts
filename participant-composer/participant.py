from dataclasses import dataclass
from enum import Enum

class ParticipantField(Enum):
    FIRST_NAME = ("first_name", "firstname")
    LAST_NAME = ("last_name", "lastname")
    EMAIL = ("email", "email")
    EMAIL_STATUS = ("email_status", "emailstatus")
    TOKEN = ("token", "token")
    LANGUAGE = ("language", "language")
    VALID_FORM = ("valid_from", "validfrom")
    USES_LEFT = ("uses_left", "usesleft")

@dataclass
class Participant:
    """A participant in a survey."""

    #Limesurvey
    first_name: str
    last_name: str
    email: str
    email_status: str = None
    token: str = None
    language: str = None
    valid_from: bool = None
    uses_left: int = None

    def getField(self, field : ParticipantField):
        return getattr(self, field.value[0])