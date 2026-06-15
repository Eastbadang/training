import os
import platform
import subprocess
import sys


def get_size(bytes_value, suffix="B"):
    """바이트 단위를 보기 좋은 GB 단위로 변환합니다."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_value < factor:
            return f"{bytes_value:.2f} {unit}{suffix}"
        bytes_value /= factor


def check_system_specs():
    print("=" * 25, " 시스템 사양 확인 결과 ", "=" * 25)

    # 1. OS 정보
    print(
        f"[OS] 운영체제: {platform.system()} {platform.release()} ({platform.architecture()[0]})"
    )

    # 2. CPU 정보
    print(f"[CPU] 프로세서: {platform.processor()}")
    try:
        import psutil

        print(f" - 물리 코어 수: {psutil.cpu_count(logical=False)}개")
        print(f" - 논리 코어 수 (스레드): {psutil.cpu_count(logical=True)}개")

        # 3. RAM 정보
        svmem = psutil.virtual_memory()
        print(f"[RAM] 전체 메모리: {get_size(svmem.total)}")
        print(f" - 사용 가능한 메모리: {get_size(svmem.available)}")
    except ImportError:
        print("[경고] psutil 라이브러리가 설치되지 않아 RAM 정보를 생략합니다.")

    # 4. GPU 정보 (Local LLM의 핵심)
    print("\n" + "=" * 25, " GPU (VRAM) 정보 ", "=" * 25)
    gpu_detected = False

    # Windows / Linux 환경에서 nvidia-smi 명령어 확인
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        lines = result.stdout.strip().split("\n")
        for i, line in enumerate(lines):
            if line.strip():
                name, total_mem = line.split(",")
                vram_gb = float(total_mem.strip()) / 1024
                print(f"[GPU #{i}] 모델명: {name.strip()}")
                print(f" - 전용 VRAM: {vram_gb:.2f} GB")
                gpu_detected = True
    except (FileNotFoundError, subprocess.CalledProcessError):
        # nvidia-smi가 없는 경우 (Mac 또는 AMD GPU 등)
        pass

    # Apple Silicon Mac인 경우 예외 처리
    if platform.system() == "Darwin" and platform.machine() in ["arm64", "x86_64"]:
        try:
            # macOS 시스템 프로필에서 GPU 정보 추출 시도
            cmd = "system_profiler SPDisplaysDataType"
            res = subprocess.run(
                cmd, shell=True, capture_output=True, text=True
            )
            if "Chipset Model" in res.stdout:
                print("[GPU] Apple Silicon (통합 메모리 사용)")
                for line in res.stdout.split("\n"):
                    if "Chipset Model" in line or "Memory" in line:
                        print(f" {line.strip()}")
                gpu_detected = True
        except Exception:
            pass

    if not gpu_detected:
        print(
            "[안내] 외장 NVIDIA GPU 또는 Apple Silicon 정보를 찾지 못했습니다."
        )
        print(
            "       (CPU 모드로 구동은 가능하나 속도가 많이 느릴 수 있습니다.)"
        )

    print("=" * 70)


if __name__ == "__main__":
    check_system_specs()
