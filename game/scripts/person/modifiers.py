class Modifiers(object):
    def __init__(self):
        self._names = []
        self._attributes = []
        self._times = []
    

    def tick_time(self):
        to_del = []
        for i in range(len(self._times)):
            try:
                self._times[i] -= 1
                if self._times[i] < 1:
                    to_del.append(self._names[i])
            except TypeError:
                pass
        for i in to_del:
            self.del_item(i)

   
    def del_item(self, index):
        if isinstance(index, str):
            for name in self._names:
                if name == index:
                    index = self._names.index(name)
        self._names.pop(index)
        self._attributes.pop(index)
        self._times.pop(index)


    def add_item(self, name, attributes, time=None):
        if any([value == 0 for value in attributes.values()]):
            raise Exception("Modifier %s has attribute with 0 value, a.k.a useless modifier"%(name))
        if not name in self._names:
            self._names.append(name)
            self._attributes.append(attributes)
            self._times.append(time)
        else:
            index = self._names.index(name)
            self._names[index] = name
            self._attributes[index] = attributes
            self._times[index] = time


    def get_modified_attribute(self, attribute):
        mod = 0
        for d in self._attributes:
            for k, v in d.items():
                if k == attribute:
                    mod += v
        return mod


    def get_all(self):
        last_name = self._names[-1]
        txt = ''
        for name in self._names:
            index = self._names.index(name)
            attr_txt = ''
            d = self._attributes[index]
            for k, v in d.items():
                attr_txt += "{0}({1})".format(k, v)
            time_txt = self._times[index]
            txt += "{0}: attributes: {1}, time: {2}".format(name, attr_txt, time_txt)
            if name != last_name:
                txt += '\n'
        return txt

    def get_modifier(self, name):
        index = None
        for n in self._names:
            if n == name:
                index = self._names.index(name)
        try:
            return name, self._attributes[index], self._times[index]
        except TypeError:
            return None


    def get_modifier_separate(self, attribute, names=False):
        if not names:
            l = []
            for d in self._attributes:
                for k, v in d.items():
                    if k == attribute:
                        l.append(v)
        else:
            l = []
            for i in range(len(self._attributes)):
                d = self._attributes[i]
                for k, v in d.items():
                    if k == attribute:
                        l.append((self._names[i], v))
        return l