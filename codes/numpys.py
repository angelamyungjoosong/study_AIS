#2차원 리스트, 행이 3개 열이 2개 
py_list= [[1,2]
	    ,[3,4]
	    ,[5,6]] #list 

import numpy as np

np_array = np.array([[7,8]
           	        ,[9,10]
	   	            ,[11,12]]) #행렬 = array

pass #breakpoint

#debug console 
type(py_list)
#list
type(np_array)
#numpy.ndarray

#리스트- 열에 대한 평균을 구하려면  루핑 돌려서 sum을 하고 길이만큼 나눠
#array- 루핑이 아니고 행렬 계산법으로 한꺼번에 계산 가능/ 속도면에서 훨씬 더 빠르다 

#여기엔 리스트 넣으면 안됨
np.mean(np_array)
#9.5 #전체에 대한 평균

#우리는 열/행 방식의 평균을 구하고 싶음 
np.mean(np_array, axis=0)
#array([9,10])
#각 열의 평균이 나옴 
np.mean(np_array, axis=1)
#array([7.5, 9.5, 11.5)
#각 행의 평균이 나옴 

#병합(넌파이)
#두개의 array를 행으로 붙이려면 행의 개수가 같아야하고 열로 붙이려면 열의 개수가 같아야한다. 
np_array02 = np.array(py_list) #두번째 array변수 

#debug console
#concat할 array두개, 어느 축으로 붙일지 넣기  
#변수가 가로로 시작하면 튜플 
np.concatenate((np_array, np_array02), axis=0) #열 기준으로 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array, np_array02), axis=1) #행 기준으로 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])


#google: concatenate numpy api

pass 
