import random # 난수 생성을 위한 모듈 사용
import numpy as np # 수치 계산을 위한 라이브러리 == numpy
import matplotlib.pyplot as plt # 그래프 그리기
from sklearn.model_selection import train_test_split # 사이킷런 == 머신러닝을 위한 라이브러리
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 해당 시뮬레이션은 왼손 움직임, 오른손 움직임에 대한 뇌 신호를 가정하고 생성하는 것.

def generate_bci_data(num_sample, num_channels):
    """간단한 BCI 데이터 생성 함수"""
    data = []
    labels = []

    for _ in range(num_sample):
        # 0(왼손 움직임) 또는 1(오른손 움직임) 중 랜덤 선택
        label = random.choice([0, 1])

        # 채널별 신호 생성
        sample = []
        for channel in range(num_channels):
            if label == 0: # 왼손
                signal = random.gauss(0, 1) # 평균 0, 표준편차 1의 가우시안 분포
            else: # 오른손
                signal = random.gauss(0.5, 1) # 평균 0.5, 표준편차 1의 가우시안 분포
            sample.append(signal)

        data.append(sample)
        labels.append(label)

    return np.array(data), np.array(labels)

# 데이터 생성
num_samples = 100
num_channels = 3
X, y = generate_bci_data(num_samples, num_channels)

# 결과 출력
print("생성된 데이터 형태:", X.shape)
print("생성된 레이블 형태:", y.shape)
print("\n처음 5개의 샘플:")
for i in range(5):
    print(f"샘플 {i+1}: {X[i]}, 레이블: {'왼손' if y[i] == 0 else '오른손'}")



plt.figure(figsize=(10, 6))
for i in range(num_channels):
    plt.subplot(num_channels, 1, i+1)
    plt.plot(X[:, i])
    plt.title(f"Channel {i+1}")

plt.tight_layout()
plt.savefig("bci_simulation_visualization.png")
plt.close()

print("데이터 시각화 이미지가 bci_simulation_visualization.png로 저장되었습니다.")

# 특징 추출 : 각 채널의 평균값 계ㅅ산
features = np.mean(X, axis=1)

print("\n추출된 특징 (처음 5개 샘플):")
for i in range(5):
    print(f"샘플 {i+1} 특징: {features[i]:.4f}, 레이블: {'왼손' if y[i] == 0 else '오른손'}")


# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(features.reshape(-1, 1), y, test_size=0.2, random_state=42)

# 모델 훈련
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측 및 정확도 계산
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n분류기 정확도: {accuracy:.2f}")