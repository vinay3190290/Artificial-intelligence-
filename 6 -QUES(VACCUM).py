class VacuumCleaner:
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = 0
        self.clean_rooms = 0

    def suck(self):
        if self.rooms[self.current_room] == 'dirty':
            self.rooms[self.current_room] = 'clean'
            self.clean_rooms += 1
            print(f"Room {self.current_room} is now clean!")

    def move(self, direction):
        if direction == 'right':
            self.current_room = (self.current_room + 1) % len(self.rooms)
        elif direction == 'left':
            self.current_room = (self.current_room - 1) % len(self.rooms)
        print(f"Moved to room {self.current_room}")

    def run(self):
        while True:
            self.suck()
            if all(room == 'clean' for room in self.rooms):
                print("All rooms are clean!")
                break
            self.move('right')

# Initialize the vacuum cleaner with 5 rooms
vacuum = VacuumCleaner(['dirty', 'dirty', 'clean', 'dirty', 'dirty'])

# Run the vacuum cleaner
vacuum.run()