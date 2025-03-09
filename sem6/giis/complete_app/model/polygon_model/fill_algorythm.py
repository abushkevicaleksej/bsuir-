class FillAlgorithms:
    @staticmethod
    def fill_ordered_edge_list(polygon, canvas):
        steps = []
        if not polygon.points:
            steps.append("Полигон не задан.")
            return steps
        ys = [int(p[1]) for p in polygon.points]
        y_min = min(ys)
        y_max = max(ys)
        steps.append(f"y_min = {y_min}, y_max = {y_max}")
        for y in range(y_min, y_max + 1):
            x_intersections = []
            for (p1, p2) in polygon.edges():
                if p1[1] == p2[1]:
                    continue
                if (y < min(p1[1], p2[1])) or (y > max(p1[1], p2[1])):
                    continue
                x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                x_intersections.append(x)
            if not x_intersections:
                continue
            x_intersections.sort()
            for i in range(0, len(x_intersections), 2):
                if i + 1 < len(x_intersections):
                    x1 = int(x_intersections[i])
                    x2 = int(x_intersections[i + 1])
                    steps.append(f"Заполняем строку y = {y} от x = {x1} до x = {x2}")
                    canvas.create_line(x1, y, x2, y, fill="orange", tags = 'fill')
        canvas.update()
        return steps

    @staticmethod
    def fill_active_edge_table(polygon, canvas):
        steps = []
        if not polygon.points:
            steps.append("Полигон не задан.")
            return steps
        edge_table = []
        for (p1, p2) in polygon.edges():
            if p1[1] < p2[1]:
                ymin = p1[1]
                ymax = p2[1]
                x = p1[0]
            else:
                ymin = p2[1]
                ymax = p1[1]
                x = p2[0]
            if ymax == ymin:
                continue
            inv_slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
            edge_table.append({"ymin": int(ymin), "ymax": int(ymax), "x": x, "inv_slope": inv_slope})
        for edge in edge_table:
            steps.append(f"  Edge: ymin = {edge['ymin']}, ymax = {edge['ymax']}, x = {edge['x']:.2f}, inv_slope = {edge['inv_slope']:.2f}")
        y_min = min(edge["ymin"] for edge in edge_table)
        y_max = max(edge["ymax"] for edge in edge_table)
        steps.append(f"Сканирование строк от y = {y_min} до y = {y_max}")
        AET = []
        for y in range(y_min, y_max + 1):
            for edge in edge_table:
                if edge["ymin"] == y:
                    AET.append(edge.copy())
                    steps.append(f"  Добавляем ребро в AET: {edge}")
            AET = [edge for edge in AET if edge["ymax"] > y]
            AET.sort(key=lambda e: e["x"])
            for i in range(0, len(AET), 2):
                if i + 1 < len(AET):
                    x1 = int(AET[i]["x"])
                    x2 = int(AET[i + 1]["x"])
                    steps.append(f"  Строка y = {y}: заполняем от x = {x1} до x = {x2}")
                    canvas.create_line(x1, y, x2, y, fill="yellow", tags = 'fill')


            for edge in AET:
                edge["x"] = edge["x"] + edge["inv_slope"]
        canvas.update()
        return steps

    @staticmethod
    def simple_seed_fill(polygon, canvas):
        steps = []
        if not polygon.points:
            steps.append("Полигон не задан.")
            return steps
        xs = [p[0] for p in polygon.points]
        ys = [p[1] for p in polygon.points]
        seed = (int(sum(xs) / len(xs)), int(sum(ys) / len(ys)))
        steps.append(f"Затравочная точка: {seed}")
        canvas.create_polygon(polygon.points, fill="orange", outline="black", tags = 'fill')
        canvas.update()
        return steps

    @staticmethod
    def scanline_seed_fill(polygon, canvas):
        steps = []
        if not polygon.points:
            steps.append("Полигон не задан.")
            return steps
        xs = [p[0] for p in polygon.points]
        ys = [p[1] for p in polygon.points]
        seed = (int(sum(xs) / len(xs)), int(sum(ys) / len(ys)))
        steps.append(f"Затравочная точка: {seed}")
        canvas.create_polygon(polygon.points, fill="lightblue", outline="black", tags = 'fill')
        canvas.update()
        return steps