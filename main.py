#conda install -c conda-forge fastapi uvicorn #파이썬일때 terminal에서 설치 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # FastAPI가 app으로 인스턴스화에서 uvicorn에서 app으로 쓰임 

# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/") # app이 갖고 있는 get이라는 function에 쏨 
async def root():
    return {"message": "Hello World"}

#app.post('/api_v1/mlmodel') #여기에 버젼을 붙여주는 이유는 서비스하는 버젼이 여러개 있을 수도 있어서
import pickle

#먼저 파이썬에서 동작하는지 확인 후, 여기서 바꿔줌
#캡 씌워줘야함 
#json형식/딕셔너리로 받고 보내주고 

#/api_v1/mlmodelwithregression with dict params 
#method : post
#http://127.0.0.1:8000/api_v1/mlmodelwithregression
@app.post('/api_v1/mlmodelwithregression') 
def mlmodelwithregression(data:dict) :  #data가 dict로 대치 
    print('data with dict {}'.format(data))

    # data dict to 변수 할당 
    texture_mean = float(data['texture_mean'])
    perimeter_mean = float(data['perimeter_mean'])

    #pkl 파일 존재 확인 코드 필요

    result_predict = 0
    #학습 모델 불러와 예측 
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict)) #array(차원이 있는것)으로 리턴, 딕셔너리 리턴이 더 좋음(여러값을 넣을 수 있게)
        pass

    #예측값 리턴 
    result = {'radius_mean': result_predict[0]}
    return result #리턴은 묶음으로 하는 게 좋음 
   

#내부에서 동작시켜보고 확인