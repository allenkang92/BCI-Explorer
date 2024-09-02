import random

# 상수 정의
RESTING_POTENTIAL = -70  # mV
THRESHOLD_POTENTIAL = -55  # mV
ACTION_POTENTIAL = 40  # mV

def simulate_neuron(simulation_time):
    potential = RESTING_POTENTIAL
    states = []
    potentials = []
    
    for _ in range(simulation_time):
        # 랜덤한 자극 생성 (-5mV에서 20mV 사이)
        stimulus = random.uniform(-5, 20)
        potential += stimulus
        
        # 뉴런 상태 결정
        if potential >= THRESHOLD_POTENTIAL:
            state = "firing"
            potential = ACTION_POTENTIAL  # 활동 전위 발생
        elif potential < RESTING_POTENTIAL:
            state = "hyperpolarized"
        else:
            state = "rest"
        
        states.append(state)
        potentials.append(potential)
        
        # 다음 단계를 위한 전위 조정
        if state == "firing":
            potential = RESTING_POTENTIAL  # 발화 후 휴지 전위로 복귀
        elif state == "rest":
            potential = max(potential - 2, RESTING_POTENTIAL)  # 서서히 휴지 전위로 복귀
    
    return potentials, states

# 시뮬레이션 실행
simulation_time = 20
potentials, states = simulate_neuron(simulation_time)

# 결과 출력
for i in range(simulation_time):
    print(f"Time step {i}: 전위 = {potentials[i]:.2f} mV, 뉴런 상태 = {states[i]}")