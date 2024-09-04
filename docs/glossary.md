# BCI 관련 용어집

resting_potential (휴지 전위)
- 뉴런이 자극 없을 때의 전기적 상태
- 보통 -70mV 정도 (mV는 밀리볼트)
- 이때 뉴런은 정보 전달 안 하고 그냥 쉬는 중

threshold_potential (역치 전위)
- 뉴런이 활동 전위 일으키는 최소 전위
- 대략 -55mV 정도
- 이거 넘으면 활동 전위 발생

action_potential (활동 전위)
- 뉴런이 정보 전달할 때 생기는 급격한 전위 변화
- +40mV까지 올라감
- 이때 뉴런이 발화(Fire)했다고 함

neuron_state (뉴런 상태)
- 현재 뉴런 상태 나타내는 문자열
- "rest": 뉴런 쉬는 중
- "firing": 뉴런 활동 전위 발생 중
- "hyperpolarized": 뉴런 전위가 휴지 전위보다 더 낮아진 상태

BCI (Brain-Computer Interface)
- 뇌랑 컴퓨터 직접 연결하는 기술
- 뇌 신호 해석해서 외부 장치 제어함