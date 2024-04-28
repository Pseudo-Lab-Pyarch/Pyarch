# DDD

### 유비쿼터스 언어 정리
|한국어|영어|설명|
|------|---|---|
|집	|house|	집 정보를 포함하고 있는 엔티티. 아이디, 건축연도, 1층 높이, 침실 개수, 실거래가 를 포함한다|
|모델 |model |실거래가를 예측하도록 학습된 회귀 모델. 학습된 모델 종류와 시기에 따라 pkl로 저장됨
|예측	|prediction	|집 정보를 모델에 입력하여 실거래가 값 회귀 예측|
|훈련	|train	|준비된 학습용 집 정보 데이터로 모델 훈련|

<img width="1018" alt="result" src="https://github.com/yoonjong12/DDD/blob/main/assets/fig1.png">

---
```bash
house/
├── domain/
│   ├── __init__.py
│   ├── house.py
│   └── model.py
├── service/
│   ├── __init__.py
│   ├── trainer.py
│   └── prediction.py
├── data/
├── models/
├── __init__.py
└── README.md
```

도메인 디렉토리:
* house.py : 집 정보와 관련된 속성 및 동작을 도메인 모델
* model.py : 예측 모델과 관련된 속성과 동작을 나타내는 도메인 모델

서비스 디렉토리:
* trainer.py : 데이터 가져오기, 모델 훈련을 처리하는 트레이너 서비스
* prediction.py : 모델 가져오기, 주택 정보 입력, 실거래가 추론 예측 서비스
