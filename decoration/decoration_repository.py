class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        try:
            find_try = [deco for deco in self.decorations if deco.__class__.__name__ == decoration_type][0]
            return find_try
        except IndexError:
            return "None"