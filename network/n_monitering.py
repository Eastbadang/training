import os
import csv
from datetime import datetime
from collections import Counter
from scapy.all import sniff, ARP, IP, TCP, UDP, DNS, DNSQR

# ==============================================================================
# [사용자 설정] 모니터링할 제한 시간을 '초(Seconds)' 단위로 설정하세요.
# 예: 60 = 1분, 300 = 5분, 3600 = 1시간
MONITORING_TIMEOUT = 60
# ==============================================================================

# 1. 환경 설정 및 파일명 유니크화 (날짜_시간 기반)
OUTPUT_PATH = r"C:\temp"
current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
FILE_NAME = f"network_local_{current_time_str}.csv"  # 실행 시점마다 고유한 파일명 생성
FULL_PATH = os.path.join(OUTPUT_PATH, FILE_NAME)

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# CSV 헤더 초기화
with open(FULL_PATH, mode='a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Protocol", "Length", "Src IP", "Src Port", "Dst IP", "Dst Port", "Extra Info"])

# 실시간 분석용 통계 저장소
dns_counter = Counter()
ip_traffic = Counter()
port_counter = Counter()
total_packets = 0
start_time = datetime.now()


def print_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    elapsed_time = (datetime.now() - start_time).seconds
    remaining_time = max(0, MONITORING_TIMEOUT - elapsed_time)

    print("=" * 65)
    print(f"   [ 시간 제한 모드: 내 PC 연관 네트워크 모니터링 시스템 ]   ")
    print(f"       로그 저장 파일: {FILE_NAME}")
    print(f"       진행 상황: {elapsed_time}초 경과 / {remaining_time}초 후 자동 종료")
    print("=" * 65)
    print(f" 현재까지 수집된 패킷 수: {total_packets} 개\n")

    print("[1. 내가 요청한 상위 도메인]")
    for domain, count in dns_counter.most_common(3):
        print(f"  ▶ {domain:<40} : {count}회 요청")
    if not dns_counter: print("  (아직 외부 도메인 요청(DNS)이 감지되지 않았습니다.)")

    print("\n[2. 트래픽 유발 상위 장비 (바이트 수)]")
    for ip, bytes_sum in ip_traffic.most_common(3):
        print(f"  ▶ {ip:<40} : {bytes_sum:,} Bytes")

    print("\n[3. 가장 활성화된 서비스 포트]")
    for port, count in port_counter.most_common(3):
        print(f"  ▶ 포트 {port:<37} : {count}회 통신")
    print("=" * 65)
    print(" ※ 최근 감지된 패킷 흐름:")


def packet_handler(packet):
    global total_packets
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        pkt_len = len(packet)
        total_packets += 1

        protocol = "UNKNOWN"
        src_ip, src_port = "", ""
        dst_ip, dst_port = "", ""
        extra_info = ""

        if packet.haslayer(IP):
            protocol = "IP"
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            ip_traffic[src_ip] += pkt_len

            if packet.haslayer(TCP):
                protocol = "TCP"
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                extra_info = f"Flags:{packet[TCP].flags}"
                port_counter[dst_port] += 1

            elif packet.haslayer(UDP):
                protocol = "UDP"
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                port_counter[dst_port] += 1

                if packet.haslayer(DNS) and packet.haslayer(DNSQR):
                    protocol = "DNS"
                    qname = packet[DNSQR].qname.decode('utf-8', errors='ignore').strip('.')
                    extra_info = f"Query:{qname}"
                    dns_counter[qname] += 1

        elif packet.haslayer(ARP):
            protocol = "ARP"
            src_ip = packet[ARP].psrc
            dst_ip = packet[ARP].pdst
            extra_info = "Request" if packet[ARP].op == 1 else "Reply"

        if protocol != "UNKNOWN":
            with open(FULL_PATH, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, protocol, pkt_len, src_ip, src_port, dst_ip, dst_port, extra_info])

            if total_packets % 10 == 0:
                print_dashboard()

            print(f"  [{protocol}] {src_ip}:{src_port} -> {dst_ip}:{dst_port} ({pkt_len}B) {extra_info}")

    except Exception:
        pass


if __name__ == "__main__":
    print(f"시스템을 초기화 중입니다... ({MONITORING_TIMEOUT}초 동안만 수집)")
    try:
        # ★ promisc=False로 안전 모드를 유지하며, timeout 옵션으로 지정 시간 후 자동 종료
        sniff(prn=packet_handler, store=0, count=0, promisc=False, timeout=MONITORING_TIMEOUT)

        # 지정된 타임아웃 종료 후 최종 결과 화면 출력
        print_dashboard()
        print(f"\n[안내] 지정된 {MONITORING_TIMEOUT}초가 경과하여 모니터링이 자동 종료되었습니다.")
        print(f"[안내] 결과 파일: {FULL_PATH}")

    except KeyboardInterrupt:
        print("\n[안내] 사용자에 의해 모니터링이 도중에 종료되었습니다.")
