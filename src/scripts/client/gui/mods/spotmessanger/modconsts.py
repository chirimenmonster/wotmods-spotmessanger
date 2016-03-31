
from constants import ARENA_GUI_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME

class BATTLE_TYPE:
    LABELS = {
        ARENA_GUI_TYPE.UNKNOWN: 'GlobalMap',	
        ARENA_GUI_TYPE.RANDOM: 'Random',
        ARENA_GUI_TYPE.TRAINING: 'Training',
        ARENA_GUI_TYPE.COMPANY: 'Company',
        ARENA_GUI_TYPE.TUTORIAL: 'Tutorial',
        ARENA_GUI_TYPE.CYBERSPORT: 'TeamBattle',
        ARENA_GUI_TYPE.FALLOUT: 'Fallout',
        ARENA_GUI_TYPE.EVENT_BATTLES: 'EventBattles',
        ARENA_GUI_TYPE.SORTIE: 'Fortifications',
        ARENA_GUI_TYPE.FORT_BATTLE: 'Fortifications',
        ARENA_GUI_TYPE.RATED_CYBERSPORT: 'TeamBattle',
        ARENA_GUI_TYPE.RATED_SANDBOX: 'others',
        ARENA_GUI_TYPE.SANDBOX: 'ProvingGround',
        ARENA_GUI_TYPE.FALLOUT_CLASSIC: 'Fallout',
        ARENA_GUI_TYPE.FALLOUT_MULTITEAM: 'Fallout'
	}
    LIST = list(set(LABELS.values())) + ['default']

class VEHICLE_TYPE:
    LABELS = {
        VEHICLE_CLASS_NAME.LIGHT_TANK: 'LT',
        VEHICLE_CLASS_NAME.MEDIUM_TANK: 'MT',
        VEHICLE_CLASS_NAME.HEAVY_TANK: 'HT',
        VEHICLE_CLASS_NAME.AT_SPG: 'TD',
        VEHICLE_CLASS_NAME.SPG: 'SPG'
	}
    LIST = list(set(LABELS.values()))

class COMMAND_TYPE:
    LIST = [ 'ping', 'help', 'teammsg', 'squadmsg' ]
