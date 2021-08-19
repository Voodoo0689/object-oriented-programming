class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, m_sm, sm):
        m = self._length * self._width * m_sm * sm / 1000
        return (f'{int(m)} т') # int не обязательно


r = Road(20, 5000)
print(r.mass(25, 5))