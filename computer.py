class CPU:
    def __init__(self, cores):
        self.cores = cores
    
class RAM:
    def __init__(self, size):
        self.size = size

class hardDrive:
    def __init__(self, capacity):
        self.capacity = capacity


# computer has a CPU
# computer has a ram
# computer has a hard drive
class Computer:
    def __init__(self, cores, ram_size, hd_copacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = hardDrive(hd_copacity)


mac = Computer(8, 16, 512)
