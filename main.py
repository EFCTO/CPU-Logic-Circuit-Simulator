# 필요한 패키지
from colorama import Fore, Back, Style, init
init(autoreset=True)

# 논리연산 저장용 함수
def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 1 - a
def XOR(a, b): return a ^ b

# ALU 계산 클래스
class ALU:
    def __init__(self):
        self.carry = 0
        self.overflow = 0

    def operate(self, a, b, op):
        self.carry = 0
        self.overflow = 0
        result = None

        if op == "ADD":
            result = a + b
            if result > 255:
                self.carry = 1
                result = result & 0xFF
            if (a > 127 and b > 127 and result < 128) or (a < 128 and b < 128 and result >= 128):
                self.overflow = 1
        elif op == "SUB":
            result = a - b
            if result < 0:
                self.carry = 1
                result = (result + 256) & 0xFF
        elif op == "AND":
            result = AND(a, b)
        elif op == "OR":
            result = OR(a, b)
        elif op == "XOR":
            result = XOR(a, b)
        else:
            print(Fore.RED + "지원하지 않는 연산입니다.")
            return None

        return result

# Memory 클래스
class Memory:
    def __init__(self):
        self.storage = {}

    def store(self, addr, value):
        self.storage[addr] = value
        print(Fore.GREEN + f"메모리[{addr}] ← {value}")

    def load(self, addr):
        value = self.storage.get(addr, 0)
        print(Fore.CYAN + f"메모리[{addr}] → {value}")
        return value

# CPU 클래스
class CPU:
    def __init__(self):
        self.register = 0
        self.ALU = ALU()
        self.memory = Memory()

    def execute(self, instruction, value=None):
        if instruction == "LOAD":
            self.register = value
            print(Fore.YELLOW + f"[LOAD] 레지스터 ← {value}")
        elif instruction == "STORE":
            addr = input(Fore.MAGENTA + "저장할 메모리 주소 입력: ")
            self.memory.store(addr, self.register)
        elif instruction in ["ADD", "SUB", "AND", "OR", "XOR"]:
            alu_result = self.ALU.operate(self.register, value, instruction)

            op_symbol = {
                "ADD": "+",
                "SUB": "-",
                "AND": "&",
                "OR": "|",
                "XOR": "^"
            }.get(instruction, "?")

            print(Fore.BLUE + f"[{instruction}] {self.register} {op_symbol} {value} → {alu_result} (Carry: {self.ALU.carry}, Overflow: {self.ALU.overflow})")
            self.register = alu_result
        elif instruction == "PRINT":
            print(Fore.GREEN + f"레지스터: {self.register}, Carry: {self.ALU.carry}, Overflow: {self.ALU.overflow}")
        else:
            print(Fore.RED + "알 수 없는 명령어입니다.")

# 논리 메뉴
def logic_menu():
    print(Fore.CYAN + Style.BRIGHT + "논리 회로")
    a = int(input("a 입력 (0 또는 1): "))
    b = int(input("b 입력 (0 또는 1): "))
    print(Fore.YELLOW + f"AND: {AND(a, b)}")
    print(Fore.YELLOW + f"OR : {OR(a, b)}")
    print(Fore.YELLOW + f"XOR: {XOR(a, b)}")
    print(Fore.YELLOW + f"NOT a: {NOT(a)}")

# CPU 메뉴
def cpu_menu(cpu):
    print(Fore.CYAN + Style.BRIGHT + "CPU - 명령 실행")
    while True:
        print(Fore.WHITE + "\nCPU 명령어: LOAD, ADD, SUB, AND, OR, XOR, STORE, PRINT, EXIT")
        cmd = input("명령어 입력: ").upper()
        if cmd == "EXIT":
            break
        elif cmd == "LOAD":
            val = int(input("값 입력: "))
            cpu.execute(cmd, val)
        elif cmd in ["ADD", "SUB", "AND", "OR", "XOR"]:
            val = int(input("연산할 값 입력: "))
            cpu.execute(cmd, val)
        elif cmd in ["STORE", "PRINT"]:
            cpu.execute(cmd)
        else:
            print(Fore.RED + "지원하지 않는 명령어입니다.")

# 메모리 메뉴
def memory_menu(cpu):
    print(Fore.CYAN + Style.BRIGHT + "Memory")
    while True:
        print(Fore.WHITE + "\n메모리 명령어: LOAD, STORE, EXIT")
        cmd = input("명령어 입력: ").upper()
        if cmd == "EXIT":
            break
        elif cmd == "STORE":
            addr = input("메모리 주소 입력: ")
            val = int(input("저장할 값 입력: "))
            cpu.memory.store(addr, val)
        elif cmd == "LOAD":
            addr = input("메모리 주소 입력: ")
            cpu.memory.load(addr)
        else:
            print(Fore.RED + "지원하지 않는 명령어입니다.")

# 프로그램 로더
def program_loader(cpu):
    print(Fore.CYAN + Style.BRIGHT + "간단한 프로그램 로딩 시뮬레이션")
    program = [
        ("LOAD", 10),
        ("ADD", 5),
        ("SUB", 3),
        ("AND", 7),
        ("OR", 12),
        ("XOR", 8),
        ("PRINT", None),
    ]
    print(Fore.YELLOW + "간단한 명령 시퀀스를 실행합니다...")
    for instr, val in program:
        cpu.execute(instr, val)
    print(Fore.GREEN + "프로그램 실행 완료.")

# GPU 메뉴
def gpu_menu():
    print(Fore.CYAN + Style.BRIGHT + "GPU 벡터 연산 시뮬레이션")
    import numpy as np
    data = list(map(int, input("벡터 데이터 입력 (예: 1 2 3 4): ").split()))
    factor = int(input("곱할 값 입력: "))
    np_data = np.array(data)
    result = np_data * factor
    print(Fore.YELLOW + f"결과: {result}")

# 메인 메뉴
def main():
    cpu = CPU()
    while True:
        print(Fore.MAGENTA + "\n==============================")
        print(Fore.CYAN + Style.BRIGHT + "논리회로 / ALU / CPU / Memory / Program / GPU")
        print(Fore.MAGENTA + "==============================")
        print(Fore.YELLOW + "1. 논리 회로")
        print(Fore.YELLOW + "2. CPU (ALU 포함)")
        print(Fore.YELLOW + "3. Memory")
        print(Fore.YELLOW + "4. 간단한 프로그램 로딩")
        print(Fore.YELLOW + "5. GPU 벡터 연산")
        print(Fore.YELLOW + "6. 도움말")
        print(Fore.YELLOW + "7. 종료")
        choice = input(Fore.GREEN + "선택: ")

        if choice == "1":
            logic_menu()
        elif choice == "2":
            cpu_menu(cpu)
        elif choice == "3":
            memory_menu(cpu)
        elif choice == "4":
            program_loader(cpu)
        elif choice == "5":
            gpu_menu()
        elif choice == "6":
            print(Fore.CYAN + Style.BRIGHT + """
[HELP - 전체 메뉴 및 명령어 설명]

1. 논리 회로
    - AND : 두 입력의 논리 AND 연산
    - OR  : 두 입력의 논리 OR 연산
    - XOR : 두 입력의 논리 XOR 연산
    - NOT : 입력의 논리 반전

2. CPU (ALU 포함)
    - LOAD  : 레지스터에 값 로드
    - ADD   : 레지스터 값에 값 더하기
    - SUB   : 레지스터 값에서 값 빼기
    - AND   : 레지스터와 값의 비트 AND
    - OR    : 레지스터와 값의 비트 OR
    - XOR   : 레지스터와 값의 비트 XOR
    - STORE : 레지스터 값을 메모리에 저장
    - PRINT : 레지스터 및 플래그 상태 출력
    - EXIT  : CPU 메뉴 종료

3. Memory
    - STORE : 지정한 주소에 값 저장
    - LOAD  : 지정한 주소에서 값 불러오기
    - EXIT  : Memory 메뉴 종료

4. Program Loader
    - 미리 작성된 간단한 명령 시퀀스를 자동 실행

5. GPU 벡터 연산
    - 벡터 데이터 입력 후 값 곱셈 수행

6. 도움말
    - 전체 설명 다시 출력

7. 종료
    - 프로그램 종료
""")
        elif choice == "7":
            print(Fore.RED + Style.BRIGHT + "시뮬레이터 종료.")
            break
        else:
            print(Fore.RED + "잘못된 선택입니다.")

if __name__ == "__main__":
    main()
