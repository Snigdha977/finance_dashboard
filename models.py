class User:
    def __init__(self, id, name, role, status):
        self.id = id
        self.name = name
        self.role = role
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'status': self.status
        }


class Record:
    def __init__(self, id, amount, type, category, date, notes):
        self.id = id
        self.amount = amount
        self.type = type
        self.category = category
        self.date = date
        self.notes = notes

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'type': self.type,
            'category': self.category,
            'date': self.date,
            'notes': self.notes
        }
