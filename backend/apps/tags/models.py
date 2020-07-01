from rest.app import db

candidate_tag = db.Table('candidate_tag',
                         db.Column('candidate_uid', db.Integer, db.ForeignKey('candidate.uid')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                         )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(200), nullable=False)
    value = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(32), nullable=False)
    candidate = db.relationship("Candidate", secondary=candidate_tag, backref=db.backref('addTags', lazy='dynamic'))
