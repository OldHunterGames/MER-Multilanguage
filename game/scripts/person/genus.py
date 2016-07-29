# -*- coding: UTF-8 -*-
def init_genus(caller, genus):
    for sub in Genus.__subclasses__():
        if sub.name == genus:
            try:
                if caller.genus != sub:
                    caller.genus.remove(caller)
            except AttributeError:
                pass
            sub.invoke(caller)
            return sub
    raise Exception("No genus named %s"%(genus))


class Genus(object):
    pass


class Human(Genus):
    name = 'human'
    spirit = 0
    _features_ = ['human', 'human_head']
    @classmethod
    def remove(cls, caller):
        for feature in cls._features_:
            caller.remove_feature(feature)
    @classmethod
    def invoke(cls, caller):
        for feature in cls._features_:
            caller.add_feature(feature)
        return cls


