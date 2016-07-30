# -*- coding: UTF-8 -*-
def init_genus(caller, genus):
    for sub in Genus.__subclasses__():
        if sub.name == genus:
            try:
                if caller.genus.name != sub.name:
                    caller.genus.remove()
            except AttributeError:
                pass
            genus = sub(caller)
            genus.invoke()
            return genus
    raise Exception("No genus named %s"%(genus))


class Genus(object):
    def __init__(self, owner):
        self.owner = owner


class Human(Genus):
    name = 'human'
    spirit = 0
    _features_ = ['human', 'human_head']
    def remove(self):
        for feature in self._features_:
            self.owner.remove_feature(feature)
    def invoke(self):
        for feature in self._features_:
            self.owner.add_feature(feature)
        return self


