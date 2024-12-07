# Grid dimensions: 130x130
# 5213 fail

class Map:
    data = []
    guard_position = (0, 0)
    guard_facing = (0, -1)
    visited = set()

    def __init__(self, input_file):
        with open(input_file, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                self.data.append([])
                for j in range(len(line.strip())):
                    char = line.strip()[j]

                    if char == "^":
                        self.data[i].append(".")
                        self.guard_position = (j, i)
                        self.visited.add((j, i))
                    else:
                        self.data[i].append(char)

    def rotate_90(self):
        if self.guard_facing == (0, 1):
            self.guard_facing = (-1, 0)
        elif self.guard_facing == (-1, 0):
            self.guard_facing = (0, -1)
        elif self.guard_facing == (0, -1):
            self.guard_facing = (1, 0)
        else:
            self.guard_facing = (0, 1)

    def get_facing_tile_pos(self):
        return (self.guard_position[0] + self.guard_facing[0], self.guard_position[1] + self.guard_facing[1])

    def is_in_bounds(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        try:
            self.data[pos[1]][pos[0]]
            return True
        except:
            return False
    
    def move_forward(self):
        facing = self.get_facing_tile_pos()
        if not self.is_in_bounds(facing):
            self.guard_position = facing
            return

        tile_data = self.data[facing[1]][facing[0]]
        if tile_data == "#":
            self.rotate_90()
        else:
            self.guard_position = facing
            self.visited.add(self.guard_position)


    def get_num_visited(self):
        return len(self.visited)


m = Map("input.txt")
while m.is_in_bounds(m.guard_position):
    print(m.get_num_visited())
    print(m.guard_position)
    m.move_forward()

print(m.get_num_visited())