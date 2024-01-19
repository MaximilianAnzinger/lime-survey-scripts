import csv
from participant import Participant, ParticipantField

def generateCSV(fields: list[ParticipantField] ,participants: list[Participant], output: str = "data/output.csv"):
    with open(output, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[field.value[1] for field in fields])
        writer.writeheader()
        for participant in participants:
            writer.writerow({field.value[1]: participant.getField(field) for field in fields})