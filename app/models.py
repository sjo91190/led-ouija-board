from app import db


class OuijaPhrase(db.Model):
    __tablename__ = "phrase"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Text)
    remote_ip = db.Column(db.Text)
    phrase = db.Column(db.Text)

    def __init__(self, timestamp, remote_ip, phrase):
        self.timestamp = timestamp
        self.remote_ip = remote_ip
        self.phrase = phrase
