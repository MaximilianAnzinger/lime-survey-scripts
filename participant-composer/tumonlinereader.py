import csv
from participant import Participant

def readFile(path: str, delimiter: str = ',', quotechar: str = '"'):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter, quotechar)
        return list(reader)
    
def rowsToParticipants(rows: list):
    participants = []
    for row in rows:
        participants.append(Participant(row['firstname'], row['lastname'], row['email'], row['emailstatus'], row['token'], row['language'], row['validfrom'], row['usesleft']))
    return participants