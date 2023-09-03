#사용자로부터 입력받는 설명변수값 3개를 변수에 답기 
#input() return str() -> float() 
height = int(input('신장: '))  # 값을 받아(string) -> float형으로 바꿔야함
weight = float(input('체중: '))
hour = float(input('수술시간: '))

import pickle #pickle로 load해서 읽어야 함. 

with open('datasets/RecurrenceOfSurgery_regression_quest.pkl', 'rb') as regression_file:  #어떤 파일을 어떤 방식으로 as 영역에서 사용할 이름  
	loaded_model = pickle.load(regression_file) #파일을 로드 #메모리에 올려 인스턴스화 
	input_labels = [[height, weight, hour]] #학습했던 설명변수 형식 맞게 적용 
	result_predict = loaded_model.predict(input_labels)
	print('Predict 연령 Result : {}'.format(result_predict))
	pass 

#설명변수를 받아서 이 설명변수는 이런 목표변수를 나타낼 것이라고 서비스를 해주는 것 
#공식에 의한 것이기에 들어온 값이 같으면 나오는 값도 같다. 