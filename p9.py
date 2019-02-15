# Score grade

def computegrade(score):
	if score >= 0.9:
		return 'A'
	elif score >= 0.8:
		return 'B'
	elif score >= 0.7:
		return 'C'
	elif score >= 0.6:
		return 'D'
	elif score < 0.6:
		return 'F'

score  = input('Enter the score: ')
grade = ''

# Handle exception if user enter alphabet instead decimal/number
try:
	score = float(score)
	grade = computegrade(score)
except:
  grade = 'Bad'

print('Score is : ', grade);

