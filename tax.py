# -*- coding: utf-8 -*-
import sys

# 社保基数
social_security_base_low = 4279
social_security_base_high = 21396

# 五险一金比例
pension_rate = (0.08, 0.20)
medical_rate = (0.02, 0.095)
unemployment_rate = (0.005, 0.005)
fertility_rate = (0, 0.01)
work_injury_rate = (0, 0.001)
housing_fund_rate = (0.07, 0.07)

# 缴费比例
tax_not_in_count_2018 = 3500
tax_rates_2018 = [(0, 1500, 0.03),
(1500, 4500, 0.1),
(4500, 9000, 0.2),
(9000, 35000, 0.25),
(35000, 55000, 0.3),
(55000, 80000, 0.35),
(80000, sys.maxsize, 0.45)]

tax_not_in_count_2019 = 5000
tax_rates_2019 = [(0, 3000, 0.03),
(3000, 12000, 0.1),
(12000, 25000, 0.2),
(25000, 35000, 0.25),
(35000, 55000, 0.3),
(55000, 80000, 0.35),
(80000, sys.maxsize, 0.45)]
	
def social_security(salary, is_compony_part):
	base = social_security_base_high if salary > social_security_base_high else salary
	base = social_security_base_low if base < social_security_base_low else base
	index = 1 if is_compony_part else 0
	pension = base * pension_rate[index]
	medical = base * medical_rate[index]
	unemployment = base * unemployment_rate[index]
	fertility = base * fertility_rate[index]
	work_injury = base * work_injury_rate[index]
	housing_fund = base * housing_fund_rate[index]
	return pension + medical + unemployment + fertility + work_injury + housing_fund
	
def tax_step(total, start, end, rate):
	if total < start:
		return 0
	return (min([total, end]) - start) * rate

def tax_cal(salary_without_social_security, is_2019):
	tax_not_in_count = tax_not_in_count_2019 if is_2019 else tax_not_in_count_2018
	tax_rates = tax_rates_2019 if is_2019 else tax_rates_2018
	tax_salary = salary_without_social_security - tax_not_in_count
	total = 0
	for tax_rate in tax_rates:
		total += tax_step(tax_salary, tax_rate[0], tax_rate[1], tax_rate[2])
	return total
	
if __name__ == '__main__':
	salary = 10000 # default
	if len(sys.argv) > 1:
		salary = round(float(sys.argv[1]), 2)
	if salary < social_security_base_low:
		print('输入工资不能低于最低标准：' + str(social_security_base_low))
	else:
		social_security_personal = round(social_security(salary, 0), 2)
		social_security_compony = round(social_security(salary, 1), 2)
		tax_2018 = round(tax_cal(salary - social_security_personal, 0), 2)
		tax_2019 = round(tax_cal(salary - social_security_personal, 1), 2)
		print('个人工资：' + str(salary))
		print('单位总支出：' + str(salary + social_security_compony))
		print('单位五险一金：' + str(social_security_compony))
		print('个人五险一金：' + str(social_security_personal))
		print('----- 分隔符 -----')
		print('个税2018：' + str(tax_2018))
		print('个人到手2018：' + str(round(salary - social_security_personal - tax_2018, 2)))
		print('个税2019：' + str(tax_2019))
		print('个人到手2019：' + str(round(salary - social_security_personal - tax_2019, 2)))
		print('改革后少缴税：' + str(round(tax_2018 - tax_2019, 2)))