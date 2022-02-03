class RegularPolygon:
    def __init__(self, bufferManager, pos, radius, sides, rotation=0, unit="degrees"):
        self.center_x = pos[0]
        self.center_y = pos[1]
        self.radius = radius
        self.sides = sides
        self.angle = rotation
        if unit == "degrees":
            self.angle *= (math.pi/180)
        self.angle_increment = (2 * math.pi)/self.sides
        self.vertices = [ self.center_x,self.center_y,0 ]
        self.indices = []

        #adding vertices
        for i in range(self.sides):
            x = self.radius * math.cos(self.angle)
            y = self.radius * math.sin(self.angle)
            new_x = self.center_x + x
            self.vertices.append(new_x)
            new_y = self.center_y + y
            self.vertices.append(new_y)
            self.vertices.append(0)
            self.angle += self.angle_increment

        #adding indices
        self.a = 2
        self.b = 1
        for i in range(self.sides - 1):
            self.indices.append(0)
            self.indices.append(self.a)
            self.indices.append(self.b)
            self.a += 1
            self.b += 1
        self.indices.append(0)
        self.indices.append(1)
        self.indices.append(self.sides)

        self.delta, self.indexStart = bufferManager.addIndexedData(self.vertices, self.indices)
    def draw(self):
        glDrawElementsBaseVertex( GL_TRIANGLES, self.sides * 3, GL_UNSIGNED_INT, self.indexStart, self.delta )
