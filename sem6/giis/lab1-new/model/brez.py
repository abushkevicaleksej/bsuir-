from model.main_manager import GraphicManager

class BrazenhemManager(GraphicManager):
    def _calc_coords(self):
        x1, y1, x2, y2 = self.raw_coords
        dx = x2 - x1
        dy = y2 - y1
        sign_x = self._sign(dx)
        sign_y = self._sign(dy)

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1
        error, t = el / 2, 0
        self.res_table[0] = {'x': x, 'y': y, 'e': error, 'plot': (int(x), int(y))}

        i = 1
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            self.res_table[i] = {'x': x, 'y': y, 'e': error, 'plot': (int(x), int(y))}
            t += 1
            i += 1

    def __str__(self):
        return 'Метод Брезенхема'