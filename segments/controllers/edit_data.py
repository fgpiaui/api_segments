class EditData:
    def __init__(self, field,value, object):
        self._data = {
            field:value
        }
        self._field = field
        self._value = value
        self._object = object

    def update(self):
        setattr(self._object, self._field, self._value)
        self._object.save()
        return self._object