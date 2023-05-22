from dino_runner.utils.constants import FILE_1, FILE_2
class ScoresManager:

    def __init__(self):
        self.point = 0
    def add_point(self, point):
        self.point = point
        file1 = open(FILE_1,"r")
        file2 = open(FILE_2,"w")
        for line in file1:
            file2.write(line+"\n")
        file2.write(str(self.point))
        file1.close()
        file2.close()
        file1 = open(FILE_1,"w")
        file2 = open(FILE_2,"r")
        for line in file2:
            file1.write(line+"\n")
        file1.close()
        file2.close()

    def best_points(self):
        points = []
        file1 = open(FILE_1,"r")
        file2 = open(FILE_2,"w")
        for line in file1:
            if len(line)>0 and line!="\n":
                points.append(int(line))
                file2.write(line+"\n")
        file1.close()
        file2.close()
        file1 = open(FILE_1,"w")
        file2 = open(FILE_2,"r")
        for line in file2:
            file1.write(line+"\n")
        file1.close()
        file2.close()
        points.sort(reverse=True)
        return points
