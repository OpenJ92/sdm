import sc2reader
from sc2reader.engine.plugins import SelectionTracker, APMTracker,\
        ContextLoader, GameHeartNormalizer
sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(ContextLoader())
sc2reader.engine.register_plugin(GameHeartNormalizer())

from src.db.raw.config import db
from src.db.raw.models.datapack.unit_type import UNIT_TYPE
from src.db.raw.models.datapack.ability import ABILITY
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.map import MAP
from src.db.raw.models.replay.objects import OBJECT
from src.db.raw.models.replay.player import PLAYER
from src.db.raw.inject import INJECT

## from src.app.index import *

if __name__ == "__main__":
    replay = sc2reader.load_replay("TvP.SC2Replay",load_level=5,load_map=True)
    inject = INJECT(replay)

    events = {}
    for event in replay.events:
        if event.name not in events.keys():
            events[event.name] = [event]
        else:
            events[event.name].append(event)

    def event_details(event_name, predicate = lambda e: True):
        for event in events[event_name]:
            if predicate(event):
                print(vars(event))


