from setup.db.raw.models.datapack.ability import ABILITY 
from setup.db.raw.models.datapack.unit_type import UNIT_TYPE
from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.info import INFO

class INJECT():
    def __init__(self, replay):
        self._replay = replay

    def __construct__(self):
        UNIT_TYPE.process(self._replay)
