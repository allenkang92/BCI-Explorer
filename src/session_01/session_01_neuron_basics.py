# 상수 정의
NEURON_COUNT = 100
THRESHOLD_VOLTAGE = -55.0
RESTING_POTENTIAL = -70.0

# 변수 정의
is_excited = False
neuron_type = "pyramidal"

# 변수 출력하기
print(f"Number of neurons: {NEURON_COUNT}")
print(f"Threshold voltage: {THRESHOLD_VOLTAGE} mV")
print(f"Is the neuron excited? {is_excited}")
print(f"Type of neuron: {neuron_type}")

# 뉴런의 상태를 결정하는 함수
def determine_neuron_state(membrane_potential):
    if membrane_potential > THRESHOLD_VOLTAGE:
        return "excited"
    elif membrane_potential < RESTING_POTENTIAL:
        return "hyperpolarized"
    else:
        return "rest"

# 뉴런의 상태 테스트
current_potential = RESTING_POTENTIAL  # 초기 전위
neuron_state = determine_neuron_state(current_potential)
print(f"초기 상태: 전위 = {current_potential} mV, 뉴런 상태 = {neuron_state}")

current_potential = -50  # 전위 변경
neuron_state = determine_neuron_state(current_potential) 
print(f"변경 후 상태: 전위 = {current_potential} mV, 뉴런 상태 = {neuron_state}")

# 시간에 따른 뉴런 상태 변화 시뮬레이션
import random

time_steps = 10
for step in range(time_steps):
    current_potential = random.uniform(-80, -40)  # -80mV와 -40mV 사이의 임의의 전위 생성
    neuron_state = determine_neuron_state(current_potential)
    print(f"Time step {step}: 전위 = {current_potential:.2f} mV, 뉴런 상태 = {neuron_state}")