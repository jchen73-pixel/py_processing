class SubwayStation:
	def __init__(self, name, borough, lines):
		self.name = name
		self.borough = borough
		self.lines = lines
		self.elevator = False
	def updateElevator(self, newElevator):
		self.elevator = newElevator
yankeeStadium = SubwayStation("161 St - Yankee Stadium", "Bronx", ["B", "D", 4])
for attr, value in vars(yankeeStadium).items():
	print(f"\t{attr}: {value}")
yankeeStadium.updateElevator(True)
print("New elevator value =",yankeeStadium.elevator)
