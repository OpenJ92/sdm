from setup.db.raw.config import db 

from setup.db.raw.models.replay.info import INFO

class PLAYER(db.Model):
    __tablename__ = "PLAYER"
    __table_args__ = {"schema": "replay"}

    __id__ = db.Column(db.Integer, primary_key = True)

    sid = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    is_human = db.Column(db.Boolean)
    is_observer = db.Column(db.Boolean)
    is_referee = db.Column(db.Boolean)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)
    toon_id = db.Column(db.BigInteger)
    uid = db.Column(db.Integer)
    clan_tag = db.Column(db.Text)
    name = db.Column(db.Text)
    combined_race_levels = db.Column(db.BigInteger)
    highest_league = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    result = db.Column(db.Text)
    pick_race = db.Column(db.Text)
    play_race = db.Column(db.Text)
    
    id = db.Column(db.Integer)

    owned_objects = db.realtionship('OBJECT', back_populates='owner')
    killed_objects = 

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    replay = db.relationship('INFO', back_populates='players')

    @classmethod
    def process(cls, replay):
        objs = []
        parents = cls.process_dependancies(replay)
        condition = cls.process_conditions(replay)
        if condition:
            for obj in replay.players:
                data = cls.process_raw_data(obj)
                data_derived = cls.process_derived(obj)
                objs.append(cls(**data, **parents, **data_derived))
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        return True

    @classmethod
    def process_dependancies(cls, replay):
        UT = None if not replay else INFO.select_from_object(replay)
        return {
                    'replay' : UT,
                    '__INFO__' : None if UT else UT.__id__
               }

    @classmethod
    def process_raw_data(cls, obj):
        return {
                        key
                        :
                        value 
                        for key,value 
                        in vars(obj).items()
                        if key in cls.columns
                }
    
    @classmethod
    def process_derived(cls, obj):
        return {
                        'id' : obj.detail_data['bnet']['uid']
               }

    @classmethod
    def select_from_object(cls, obj):
        pass

    columns = {
                    "sid",
                    "team_id",
                    "is_human",
                    "is_observer",
                    "is_referee",
                    "region",
                    "subregion",
                    "toon_id",
                    "uid",
                    "clan_tag",
                    "name",
                    "combined_race_levels",
                    "highest_league",
                    "pid",
                    "result",
                    "pick_race",
                    "play_race"
            }
