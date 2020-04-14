from setup.db.raw.models.datapack.ability import ABILITY 
from setup.db.raw.models.datapack.unit_type import UNIT_TYPE

from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.objects import OBJECT
from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.map import MAP

from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent
from setup.db.raw.models.events.CameraEvent import CameraEvent
from setup.db.raw.models.events.ControlGroupEvent import ControlGroupEvent
from setup.db.raw.models.events.GetControlGroupEvent import GetControlGroupEvent
from setup.db.raw.models.events.SetControlGroupEvent import SetControlGroupEvent
from setup.db.raw.models.events.PlayerStatsEvent import PlayerStatsEvent
from setup.db.raw.models.events.PlayerLeaveEvent import PlayerLeaveEvent
from setup.db.raw.models.events.PlayerSetupEvent import PlayerSetupEvent
from setup.db.raw.models.events.TargetPointCommandEvent import TargetPointCommandEvent
from setup.db.raw.models.events.TargetUnitCommandEvent import TargetUnitCommandEvent
from setup.db.raw.models.events.UpgradeCompleteEvent import UpgradeCompleteEvent 
from setup.db.raw.models.events.UnitBornEvent import UnitBornEvent
from setup.db.raw.models.events.UnitDoneEvent import UnitDoneEvent

from setup.db.raw.config import db 

db.create_all()
