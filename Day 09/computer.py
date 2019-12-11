from typing import List

class intcodeComputer:
    def __init__(self, comp: List[int], input: List[int] = []) -> None:
        self.comp = { i : comp[i] for i in range(0, len(comp) ) }
        self.input = input
        self.i = 0
        self.output = list()
        self.paused = False
        self.base = 0

    def getModeVal(self, pos: int, mode: int):
        if mode == 1:
            return pos
        elif mode == 2:
            return self.comp[pos+self.base]
        else:
            return self.comp[pos]

    def compute(self):
        while  self.i < len(self.comp):
            opcode = self.comp[self.i] % 100
            # 0 = address mode; 1 = immediate mode; 2 = relative mode
            mode1  = self.comp[self.i]//100   % 10
            mode2  = self.comp[self.i]//1000  % 10
            mode3  = self.comp[self.i]//10000 % 10
            # what the parameters are based on the mode
            try: p1 = self.getModeVal(self.comp[self.i+1], mode1)
            except: p1 = 0
            try: p2 = self.getModeVal(self.comp[self.i+2], mode2)
            except: p2 = 0
            try: p3 = self.getModeVal(self.comp[self.i+3], mode3)
            except: p3 = 0
            # these are always address/relative mode parameters
            try: p1_s  = self.comp[self.i+1] + self.base if mode1 == 2 else \
                         self.comp[self.i+1]
            except: pass
            try: p2_s  = self.comp[self.i+2] + self.base if mode2 == 2 else \
                         self.comp[self.i+2]
            except: pass
            try: p3_s  = self.comp[self.i+3] + self.base if mode3 == 2 else \
                         self.comp[self.i+3]
            except: pass

            if opcode == 1: # Addition: *p3 <- p1 + p2
                self.comp[ p3_s ] = p1 + p2
                self.i += 4
            elif opcode == 2: # Multiplication: *p3 <- p1 * p2
                self.comp[ p3_s ] = p1 * p2
                self.i += 4
            elif opcode == 3: # Store: *p1 <- input
                if not self.input:
                    self.paused = True
                    return
                self.comp[ p1_s ] = self.input.pop(0)
                self.i += 2
            elif opcode == 4: # Output: output p1
                self.output.append( p1 )
                self.i += 2
            elif opcode == 5: # Jump to p2 if p1 != 0
                self.i = p2 if p1 != 0 else self.i+3
            elif opcode == 6: # Jump to p2 if p1 == 0
                self.i = p2 if p1 == 0 else self.i+3
            elif opcode == 7: # Less-than: *p3 <- p1 < p2
                self.comp[ p3_s ] = 1 if p1 < p2 else 0
                self.i += 4
            elif opcode == 8: # Equality: *p3 <- p1 == p2
                self.comp[ p3_s ] = 1 if p1 == p2 else 0
                self.i += 4
            elif opcode == 9: # Add to relative base
                self.base += p1
                self.i += 2
            elif opcode == 99:  # Halt Program
                self.paused = False
                return