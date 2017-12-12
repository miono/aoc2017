#!/usr/bin/env python


class AOC17_12():
    def __init__(self):
        self.pipes = open('input').readlines()
        self.pipelist = []
        self.tmpgroup = []
        self.groups = []
        self.touched_pipes = []

        for pipe in self.pipes:
            pipe = pipe.strip().split()
            self.pipelist.append([int(pipe[0]), pipe[2:]])

    def check_connection(self, conns):
        for i in conns:
            i = int(i.strip(','))
            if i not in self.tmpgroup:
                self.tmpgroup.append(i)
                self.touched_pipes.append(i)
                self.check_connection(self.pipelist[i][1])

    def calculate(self):
        for i in xrange(len(self.pipelist)):
            if i not in self.touched_pipes:
                self.check_connection(self.pipelist[i][1])
                self.groups.append(self.tmpgroup)
                self.tmpgroup = []

    def solution(self):
        return len(self.groups)


problem = AOC17_12()
problem.calculate()
print problem.solution()
