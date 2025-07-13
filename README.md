# CPU-Logic-Circuit-Simulator

## 소개
이 프로젝트는 CPU 및 ALU 동작, 논리회로 연산, 메모리 입출력, 간단한 프로그램 로딩, 그리고 GPU 벡터 연산 시뮬레이션을 하나로 통합한 파이썬 기반 시뮬레이터입니다.

## 기능

### 논리 회로
AND, OR, XOR, NOT 연산을 0과 1로 직접 실습

### CPU & ALU
기본 산술 연산: ADD, SUB

논리 연산: AND, OR, XOR

오버플로우, 캐리 플래그 표시

레지스터 값 LOAD/STORE 및 출력

### Memory
주소 기반 저장 및 불러오기

### 프로그램 로더
간단한 명령 시퀀스를 자동 실행 (예: LOAD → ADD → SUB …)

### GPU 벡터 연산
NumPy 기반 벡터 연산 시뮬레이션

## 실행 방법

```CMD
pip install colorama numpy
python simulator.py
```

## 참고

colorama 모듈로 컬러 출력 지원
numpy 모듈로 벡터 연산 지원
Python 3.x 환경에서 실행 권장
