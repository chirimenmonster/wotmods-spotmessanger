
import math
import BigWorld
from items.vehicles import getVehicleClass
from gui.battle_control import avatar_getter, arena_info, minimap_utils
from gui.battle_control.minimap_utils import MINIMAP_SIZE
from messenger import MessengerEntry

from modconsts import VEHICLE_TYPE, BATTLE_TYPE
from logger import log

class Utils:

    @staticmethod
    def getTime():
        return BigWorld.time()

    @staticmethod
    def getPlayer():
        return BigWorld.player()

    @staticmethod
    def getPos(avatar = None):
        if not avatar:
            avatar = BigWorld.player()
        position = BigWorld.entities[avatar.playerVehicleID].position
        log.debug('position = {}'.format(position))
        return position

    @staticmethod
    def getTeamAmount(avatar = None):
        arena = avatar_getter.getArena(avatar)
        team = avatar_getter.getPlayerTeam(avatar)
        return len([ k for k, v in arena.vehicles.items() if v['team'] == team and v['isAlive'] ])

    @staticmethod
    def addClientMessage(message, isCurrentPlayer = False):
        MessengerEntry.g_instance.gui.addClientMessage(message, isCurrentPlayer)


class VehicleInfo(object):

    def __init__(self, avatar=None):
        self._typeDescriptor = avatar_getter.getVehicleTypeDescriptor(avatar)
    
    @property
    def name(self):
        return self._typeDescriptor.type.name
    
    @property
    def className(self):
        return getVehicleClass(self._typeDescriptor.type.compactDescr)

    @property
    def classAbbr(self):
        return VEHICLE_TYPE.LABELS[self.className]


class ArenaInfo(object):

    def __init__(self, avatar=None):
        self._arena = avatar_getter.getArena()

    @property
    def id(self):
        return self._arena.guiType

    @property
    def attrLabel(self):
        return BATTLE_TYPE.WOT_ATTR_NAME[self.id]
        
    @property
    def name(self):
        return BATTLE_TYPE.WOT_LABELS[self.id]

    @property
    def battleType(self):
        return BATTLE_TYPE.LABELS.get(self.id, 'others')


class MinimapInfo(object):

    @staticmethod
    def makeCellIndex(localX, localY):
        return int(minimap_utils.makeCellIndex(localX, localY))


    @staticmethod
    def getCellName(cellIndex):
        return minimap_utils.getCellName(cellIndex)

        
    @staticmethod
    def getLocalByPosition(position, bottomLeft, upperRight):
        spaceSize = upperRight - bottomLeft
        centerPos = (upperRight + bottomLeft) * 0.5
        localX = (position[0] - centerPos[0]) / spaceSize[0] * MINIMAP_SIZE[0] + MINIMAP_SIZE[0] * 0.5
        localY = -(position[2] - centerPos[1]) / spaceSize[1] * MINIMAP_SIZE[1] + MINIMAP_SIZE[1] * 0.5
        localX = max(min(localX, MINIMAP_SIZE[0] - 0.1), 0)
        localY = max(min(localY, MINIMAP_SIZE[1] - 0.1), 0)
        return (localX, localY)


    @classmethod
    def getCellIndexByPosition(cls, position):      
        arenaType = arena_info.getArenaType()
        bottomLeft, upperRight = arenaType.boundingBox
        localPos = cls.getLocalByPosition(position, bottomLeft, upperRight)
        cellIndex = cls.makeCellIndex(localPos[0], localPos[1])
        cellName = cls.getCellName(cellIndex)
        log.debug('bottomLeft = {}, upperRight = {}, spaceSize = {}'.format(bottomLeft, upperRight, upperRight - bottomLeft))
        log.debug('posion = {}, local = {}, cellIndex = {}, cellName = {}'.format(position, localPos, cellIndex, cellName))
        return cellIndex

