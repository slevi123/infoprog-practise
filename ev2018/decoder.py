from pathlib import Path


class Decoder:
    BASE = Path("./given").resolve()

    def __init__(self):
        braille_table_path = Decoder.BASE / "code.in"
        braille_table_lines = braille_table_path.read_text().split("\n")[1:-1] # betük száma és az utolsó újsor kilőve
        self.braille_table = dict(map(lambda x: x.split(';'), braille_table_lines))

        self.decode()

    def decode(self, raw_terkep=None):
        if not raw_terkep:
            raw_terkep = self.__class__.BASE / 'map_1.html'
        terkep = [self.sor_decode(sor) for sor in raw_terkep.read_text().split()[1:]]

        return terkep

    def sor_decode(self, sor):
        betuk = sor.split(';&#')
        betuk[0] = betuk[0][2:]
        betuk[-1] = betuk[-1][:-1]
        return ''.join([self.braille_table[betu] for betu in betuk]).split(" ")


a = Decoder()
