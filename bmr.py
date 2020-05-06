import sys

class Person:
	def __init__(self, mass, height, age, sex, fat):
		self.mass = mass
		self.height = height
		self.age = age
		self.sex = sex
		self.fat = fat
		
	def estimate(self):
		return int((self.mass / 0.45) * 10)
		
	def harrisBenedict(self): # published in 1919
		P = None
		if self.sex == 1:
			P = (13.7516 * self.mass + 5.0033 * self.height - 6.7550 * self.age + 66.4730)
		else:
			P = (9.5634 * self.mass + 1.8496 * self.height - 4.6756 * self.age + 655.0955)
		return int(P)
		
	def revisedHarrisBenedict(self): # revised in 1984
		P = None
		if self.sex == 1:
			P = (13.397 * self.mass + 4.799 * self.height - 5.677 * self.age + 88.362)
		else:
			P = (9.247 * self.mass + 3.098 * self.height - 4.330 * self.age + 447.593)
		return int(P)
	
	def mifflinStJeor(self): # 5% accurate than above
		P = None
		if self.sex == 1:
			P = (10 * self.mass + 6.25 * self.height - 5 * self.age + 5)
		else:
			P = (10 * self.mass + 6.25 * self.height - 5 * self.age - 161)
		return int(P)

	def katchMcArdle(self): # this formula calculate for RMR, above three is for BMR
		leanBodyMass = self.mass * (1 - self.fat / 100.0)
		P = 370 + (21.6 * leanBodyMass)
		return int(P)
	
if __name__ == '__main__':
	argv = sys.argv
	argv = ['bmr.py', 80, 178, 35, 1, 20]
	if len(argv) < 6:
		print('输入格式应为:\npython3 bmr.py <mass/kg> <height/cm> <age/year> <sex/1or0> <body fat rate/21.5>\n例如:\npython3 bmr.py 80 178 35 1 20')
		sys.exit(0)
	
	try:
		s = Person(argv[1], argv[2], argv[3], argv[4], argv[5])
		print('{0} 粗略估算'.format(s.estimate()))
		print('{0} 经典Harris Benedict公式'.format(s.harrisBenedict()))
		print('{0} 修正Harris Benedict公式'.format(s.revisedHarrisBenedict()))
		print('{0} Mifflin St Jeor公式'.format(s.mifflinStJeor()))
		print('{0} Katch-Mc Ardle公式(RMR)'.format(s.katchMcArdle()))
	except:
		print('参数类型可能不正确')
		pass
	finally:
		pass