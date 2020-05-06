import sys
class HeartRate:
	max_groups = [
		(50,60,'一区', '热身区'),
		(60,70,'二区', '低强度有氧'),
		(70,80,'三区', '有氧耐力区'),
		(80,90,'四区', '阈值区，也叫马拉松配速区'),
		(90,100,'五区', '无氧区')
		]
	reserve_groups = [
			(59,74,'E区', 'Easy轻松'),
			(74,84,'M区', 'Marathon马拉松配速'),
			(84,88,'T区', 'Threshold阈值/节奏'),
			(88,95,'A区', 'Anaerbic无氧，无氧耐力'),
			(95,100,'I区', 'Interval间歇，无氧动力')
			]
	lthr_groups = [
		(65,81,'1区', 'Recovery恢复区'),
		(81,88,'2区', 'Aerobic有氧区'),
		(88,93,'3区', 'Tempo节奏区'),
		(93,100,'4区', 'Subthreshold亚阈值'),
		(100,100,'5区', 'LactateThreshold乳酸阈值'),
		(100,102,'5A区', 'SuperThreshold超阈值'),
		(102,105,'5B区', 'AerobicCapacity无氧耐力'),
		(105,sys.maxsize,'5C区', 'AnaerobicCapacity无氧能力'),
	]
	def __init__(self, age, max_heart_rate, resting_heart_rate, lactate_threshold_heart_rate):
		self.age = age
		self.max_heart_rate = max_heart_rate
		self.resting_heart_rate = resting_heart_rate
		self.lactate_threshold_heart_rate = lactate_threshold_heart_rate

	def maxHeartRatePercent(self): # MHR
		for group in self.max_groups:
			h_low = int(self.max_heart_rate * group[0] / 100)
			h_high = int(self.max_heart_rate * group[1] / 100)
			print('{0}: {1}%-{2}%, {3}-{4}, {5}'.format(group[2], group[0], group[1], h_low, h_high, group[3]))
			
	def heartRateReserve(self): # HRR，和VO2MAX（最大摄氧量）的百分比完全匹配
		for group in self.reserve_groups:
			h = self.max_heart_rate - self.resting_heart_rate
			h_low = int(h * group[0] / 100 + self.resting_heart_rate) 
			h_high = int(h * group[1] / 100 + self.resting_heart_rate)
			print('{0}: {1}%-{2}%, {3}-{4}, {5}'.format(group[2], group[0], group[1], h_low, h_high, group[3]))
			
	def lactateThreshold(self): # 乳酸阈值
		for group in self.lthr_groups:
			h_low = int(self.lactate_threshold_heart_rate * group[0] / 100) 
			h_high = self.max_heart_rate if (group[1] == sys.maxsize) else int(self.lactate_threshold_heart_rate * group[1] / 100)
			p_high = (group[1] if (group[1] != sys.maxsize) else 'max')
			print('{0}: {1}%-{2}%, {3}-{4}, {5}'.format(group[2], group[0], p_high, h_low, h_high, group[3]))
		
	
if __name__ == '__main__':
	
	h = HeartRate(35, 193, 50, 170)
	
	print('最大心率百分比计算法:(简单粗暴，不考虑个体差异)')
	h.maxHeartRatePercent()
	print('储备心率百分比计算法:(考虑个体差异，但是没考虑乳酸阈值，大部分会在84-88%之间出现，但有例外)')
	h.heartRateReserve()
	print('乳酸阈值百分比计算法:(根据乳酸阈值计算，比较科学，乳酸阈值基本等于功率)')
	h.lactateThreshold()