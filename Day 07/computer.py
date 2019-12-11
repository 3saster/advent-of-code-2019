import math

class intcodeComputer:
    def __init__(self, comp, input = {}):
        self.comp = comp
        self.input = input
        self.i = 0
        self.output = list()
        self.paused = False

    def getModeVal(self, pos, mode):
        if mode == 1:
            return pos
        else:
            return self.comp[pos] if pos < len(self.comp) else 0

    def compute(self):
        while  self.i < len(self.comp):
            opcode = self.comp[self.i] % 100
            # 0 = address mode; 1 = immediate mode
            mode1  = math.floor(self.comp[self.i]/100)   % 10
            mode2  = math.floor(self.comp[self.i]/1000)  % 10
            mode3  = math.floor(self.comp[self.i]/10000) % 10
            # what the parameters are based on the mode
            p1 = self.getModeVal(self.comp[self.i+1], mode1) if self.i+1 < len(self.comp) else 0
            p2 = self.getModeVal(self.comp[self.i+2], mode2) if self.i+2 < len(self.comp) else 0
            p3 = self.getModeVal(self.comp[self.i+3], mode3) if self.i+3 < len(self.comp) else 0
            # these are always address mode parameters
            p1_s  = self.comp[self.i+1] if self.i+1 < len(self.comp) else 0
            p2_s  = self.comp[self.i+2] if self.i+2 < len(self.comp) else 0
            p3_s  = self.comp[self.i+3] if self.i+3 < len(self.comp) else 0

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
            elif opcode == 99:  # Halt Program
                self.paused = False
                return