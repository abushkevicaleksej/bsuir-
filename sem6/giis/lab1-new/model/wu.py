from model.main_manager import GraphicManager
from collections import defaultdict
import math
from model.cda import CDAManager

class WuManager(GraphicManager):
    def __init__(self, coords: dict):
        self.raw_coords = coords
        self.res_table = defaultdict(dict)
        self.by_cda = False
        self._calc_coords()

    def _can_be_CDA(self):
        x1, y1, x2, y2 = self.raw_coords
        if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
            return True
        return False

    def _round(self, x):
        return math.floor(x + 0.5)

    def _fpart(self, x):
        return x - math.floor(x)

    def _rfpart(self, x):
        return 1 - self._fpart(x)

    def _calc_coords(self):
        if self._can_be_CDA():
            self.by_cda = True
            cda_manager = CDAManager(self.raw_coords)
            self.res_table = cda_manager.res_table
            return

        x1, y1, x2, y2 = self.raw_coords
        steep = abs(y2 - y1) > abs(x2 - x1)

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx, dy = x2 - x1, y2 - y1

        if dx == 0.0:
            grad = 1.0
        else:
            grad = dy / dx

        # process start point
        xend = self._round(x1)
        yend = y1 + grad * (xend - x1)
        xgap = self._rfpart(x1 + 0.5)
        xpxl1 = xend  # will use in loop
        ypxl1 = math.floor(yend)

        if steep:
            c = round(self._rfpart(yend) * xgap, 2) or 1.0
            self.res_table[0] = {'x': ypxl1, 'y': xpxl1, 'c': c, 'plot': (ypxl1, xpxl1)}
            c = round(self._fpart(yend) * xgap, 2) or 1.0
            self.res_table[1] = {'x': ypxl1 + 1, 'y': xpxl1, 'c': c, 'plot': (ypxl1 + 1, xpxl1)}
        else:
            c = round(self._rfpart(yend) * xgap, 2) or 1.0
            self.res_table[0] = {'x': xpxl1, 'y': ypxl1, 'c': c, 'plot': (xpxl1, ypxl1)}
            c = round(self._fpart(yend) * xgap, 2) or 1.0
            self.res_table[1] = {'x': xpxl1, 'y': ypxl1 + 1, 'c': c, 'plot': (xpxl1, ypxl1 + 1)}

        intery = yend + grad  # first y-intersection for loop

        # process end point
        xend = self._round(x2)
        yend = y2 + grad * (xend - x2)
        xgap = self._fpart(x2 + 0.5)
        xpxl2 = xend  # will use in loop
        ypxl2 = math.floor(yend)

        i = 2
        if steep:
            for z in range(xpxl1 + 1, xpxl2):
                c = round(self._rfpart(intery), 2) or 1.0
                self.res_table[i] = {'x': math.floor(intery), 'y': z, 'c': c, 'plot': (math.floor(intery), z)}
                i += 1
                c = round(self._fpart(yend) * xgap, 2) or 1.0
                self.res_table[i] = {'x': math.floor(intery) + 1, 'y': z, 'c': c, 'plot': (math.floor(intery) + 1, z)}
                intery += grad
                i += 1
        else:
            for z in range(xpxl1 + 1, xpxl2):
                c = round(self._rfpart(intery), 2) or 1.0
                self.res_table[i] = {'x': z, 'y': math.floor(intery), 'c': c, 'plot': (z, math.floor(intery))}
                i += 1
                c = round(self._fpart(yend), 2) or 1.0
                self.res_table[i] = {'x': z, 'y': math.floor(intery) + 1, 'c': c, 'plot': (z, math.floor(intery) + 1)}
                intery += grad
                i += 1

        if steep:
            c = round(self._rfpart(yend) * xgap, 2) or 1.0
            self.res_table[i] = {'x': ypxl2, 'y': xpxl2, 'c': c, 'plot': (ypxl2, xpxl2)}
            c = round(self._fpart(yend) * xgap, 2) or 1.0
            self.res_table[i + 1] = {'x': ypxl2 + 1, 'y': xpxl2, 'c': c, 'plot': (ypxl2 + 1, xpxl2)}
        else:
            c = round(self._rfpart(yend) * xgap, 2) or 1.0
            self.res_table[i] = {'x': xpxl2, 'y': ypxl2, 'c': c, 'plot': (xpxl2, ypxl2)}
            c = round(self._fpart(yend) * xgap, 2) or 1.0
            self.res_table[i + 1] = {'x': xpxl2, 'y': ypxl2 + 1, 'c': c, 'plot': (xpxl2, ypxl2 + 1)}

    @property
    def _c(self):
        return [coords['c'] for coords in self.res_table.values()]

    def __str__(self):
        return 'Метод Ву'