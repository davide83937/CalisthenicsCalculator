class setLine:
    def __init__(self, skill, malus):
        self.skill = skill
        self.malus = malus

    def __repr__(self):
        return f"setLine(skill={self.skill!r}, malus={self.malus!r})"
