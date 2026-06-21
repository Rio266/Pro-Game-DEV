class Car():
    brand = "Jaguar"
    speed = 120

    def accelerate(self):
        self.speed += 10
        print(self.speed)
jaguar = Car()

jaguar.accelerate()
jaguar.accelerate()