from collections import defaultdict
import math


class GraphicManager:
    def __init__(self, coords: tuple):
        self.raw_coords = coords
        self.res_table = {}
        self._calc_coords()
    
    def _calc_coords(self):
        pass
    
    @staticmethod
    def _sign(x: int|float):
        return 1 if x > 0 else (-1 if x < 0 else 0)
    
    @property
    def coords(self):
        return [coords['plot'] for coords in self.res_table.values()]
    
    @property
    def _c(self):
        return False
