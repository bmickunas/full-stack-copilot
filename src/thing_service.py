class ThingService:
    def __init__(self, thing_dao):
        self.thing_dao = thing_dao

    def get_thing(self, thing_id):
        return self.thing_dao.get_thing(thing_id)