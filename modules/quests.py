import lxml.etree
import lxml.objectify

tree = lxml.objectify.parse(open('quest.xml'))

quests = {quest.id.pyval: quest for quest in tree.getroot().quest}

def get_quest_by_id(id):
	global quests
	
	return quests[id]

