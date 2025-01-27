from model.main_manager import GraphicManager

class CDAManager(GraphicManager):
    def _calc_coords(self):
        x1, y1, x2, y2 = self.raw_coords
        length = max([abs(x2 - x1), abs(y2 - y1)])
        dx, dy = (x2 - x1) / length, (y2 - y1) / length
        x = round(x1 + 0.5 * self._sign(dx), 2)
        y = round(y1 + 0.5 * self._sign(dy), 2)
        self.res_table[0] = {'x': x, 'y': y, 'plot': (int(x), int(y))}
        for i in range(1, length + 1):
            x = round(x + dx, 2)
            y = round(y + dy, 2)
            self.res_table[i] = {'x': x, 'y': y, 'plot': (int(x), int(y))}

    def __str__(self):
        return 'ЦДА'