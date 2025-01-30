# Python version of Hanoi Tower Algorithm with visualization

# The Tower of Hanoi is a classic problem in computer science and mathematics. It involves moving a set of disks from one peg to another, following specific rules.

## Problem Statement

# You have three pegs and `n` disks of different sizes. The goal is to move all the disks from the source peg to the destination peg using the auxiliary peg, following these rules:
# 1. Only one disk can be moved at a time.
# 2. A disk can only be placed on top of a larger disk or an empty peg.

from typing import List

class Block:
    def __init__(self, color: int):
        self.color = color
        self.moving = False
        self.target = False

class HanoiTower:
    def __init__(self, colls: int):
        self.blocks: List[List[Block]] = [[] for _ in range(colls)]       
        self.colls = colls
        self.moving_to = -1

    def fill(self, index: int, count: int):
        sub_array = self.blocks[index]
        for i in range(count):
            b = Block(i)
            sub_array.append(b)

    def print_tower(self):
        # mock block to visualize
        if self.moving_to >= 0:
            b = Block(0)
            b.target = True
            self.blocks[self.moving_to].append(b)
            pass

        max_height = max(len(sub_array) for sub_array in self.blocks)
        for level in range(max_height - 1, -1, -1):
            for sub_array in self.blocks:
                if level < len(sub_array):
                    block = sub_array[level]
                    if block.target == True:                        
                        print(f">*<", end=" ")
                    elif block.moving == True:
                        print(f">{block.color}<", end=" ")
                    else:
                        print(f"[{block.color}]", end=" ")
                else:
                    print("   ", end=" ")
            print()        
        for i in range(len(self.blocks)):
            print("~~~~", end="")            
        print()

        for i in range(len(self.blocks)):
            print(f"|{i}|", end=" ")
        print()

        #remove mock block
        if self.moving_to >= 0:
            self.blocks[self.moving_to].pop()
            pass         

def pm(start: int, end: int, t: HanoiTower):
    print(" ")
    print(" ")    
    print(" ")    
    block = t.blocks[start][len(t.blocks[start]) - 1];
    block.moving = True
    t.moving_to = end
    print("start move:")
    t.print_tower()
    print()
    print("end move:")
    # move block
    block.moving = False
    t.moving_to = -1
    t.blocks[start].pop();
    t.blocks[end].append(block);        
    t.print_tower()

def hanoi(n: int, start: int, end: int, t: HanoiTower):   
    if n == 1:
        pm(start, end, t)
        return

    other = 3 - (start + end)
    hanoi(n - 1, start, other, t)
    pm(start, end, t)    
    hanoi(n - 1, other, end, t)    

tower = HanoiTower(3)
tower.fill(0, 3)
tower.print_tower()
hanoi(3, 0, 2, tower)



