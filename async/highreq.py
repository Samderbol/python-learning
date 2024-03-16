from scapy.layers.inet import TCP, IP, sr1
from time import sleep

# 定义目标 IP 地址和端口号
target_ip = "47.122.22.52"
target_port = 80

while True:
    # 发送 TCP SYN 数据包
    syn = sr1(IP(dst=target_ip) / TCP(dport=target_port, flags="S"), timeout=2)

    # 检查 TCP SYN 数据包的响应
    if syn is None:
        print("目标主机未响应 TCP SYN 数据包")
    else:
        print("目标主机已响应 TCP SYN 数据包")

    # 发送 TCP ACK 数据包
    ack = sr1(IP(dst=target_ip) / TCP(dport=target_port, flags="A"), timeout=2)

    # 检查 TCP ACK 数据包的响应
    if ack is None:
        print("目标主机未响应 TCP ACK 数据包")
    else:
        print("目标主机已响应 TCP ACK 数据包")

    # 睡眠 1 秒
    # sleep(1)
