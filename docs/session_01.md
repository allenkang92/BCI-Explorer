# 세션 1: 뉴런 기초와 시뮬레이션

## 뉴런 기초 (session_01_neuron_basics.py)

1. 상수랑 변수 정의함
   - NEURON_COUNT, THRESHOLD_VOLTAGE, RESTING_POTENTIAL 같은 거
   - is_excited, neuron_type 이런 변수들

2. 뉴런 상태 결정하는 함수 만듦
   - membrane_potential 받아서 "excited", "hyperpolarized", "rest" 중 하나 리턴

3. 뉴런 상태 테스트함
   - 초기 상태랑 전위 변경 후 상태 출력해봄

4. 시간에 따른 뉴런 상태 변화 시뮬레이션
   - random 모듈 써서 임의의 전위 생성하고 상태 출력

## 뉴런 시뮬레이션 (session_01_neuron_simulation.py)

1. 상수 정의함
   - RESTING_POTENTIAL, THRESHOLD_POTENTIAL, ACTION_POTENTIAL

2. simulate_neuron 함수 만듦
   - 랜덤한 자극 주고 뉴런 상태 결정
   - 발화하면 활동 전위 발생시키고 휴지 전위로 복귀

3. 시뮬레이션 실행하고 결과 출력
   - 20번 반복해서 각 단계마다 전위랑 상태 보여줌

이렇게 뉴런의 기본적인 동작이랑 상태 변화를 코드로 구현해봄.