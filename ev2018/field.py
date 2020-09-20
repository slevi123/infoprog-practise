from pathlib import Path

from ev2018.decoder import Decoder


class Field:
    FIELD_FILE = Path("./given/fields.in").resolve()
    FIELD_PIC_DIR = Path('./field_pictures')
    fields = {}

    def __init__(self, kep, nev, kategoria, koltseg, veszelyes, eszkozok=None):
        self.kep, self.nev, self.kategoria, self.koltseg, self.veszelyes, self.eszkozok = \
            kep, nev, kategoria, koltseg, veszelyes, eszkozok

    def __repr__(self):
        return f"Field: {self.nev}, {self.kategoria}, {self.koltseg}, {self.veszelyes}, {self.eszkozok}"

    @classmethod
    def filder(cls):
        fields = {}
        for field in Field.FIELD_FILE.read_text().split('\n')[1:-1]:
            x = field.split(';')
            nev = x[0]
            fields[nev] = Field(None, *x)

        # return fields
        cls.fields = fields

    @classmethod
    def __sor_process(cls, sor):
        return [cls.fields[field_name] for field_name in sor]

    @classmethod
    def get_map(cls):
        sima_terkep = Decoder().decode()
        terkep = [cls.__sor_process(sor) for sor in sima_terkep]
        return terkep


if __name__ == "__main__":
    Field.filder()
    print(Field.get_map())
