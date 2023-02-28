# -*- coding:utf-8 -*-
import string


def gen_slurm_nodes(num):
    hostnames = []
    slurm_nodes = []
    ips = []
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                slurm_nodes.append(
                    "NodeName={i}0[1-2]{j}[2-6]{k}0[0-9] CPUs=32 Boards=1 SocketsPerBoard=4 CoresPerSocket=8 ThreadsPerCore=1 RealMemory=126536".format(
                        i=i, j=j, k=k))
                for a in range(1, 3):
                    for b in range(2, 7):
                        for c in range(0, 10):
                            hostnames.append("{i}0{a}{j}{b}{k}0{c}".format(i=i, j=j, k=k, a=a, b=b, c=c))
    for l in range(10, 111):
        for m in range(10, 111):
            ips.append("10.250.{l}.{m}".format(l=l, m=m))
    with open("slurm_node.conf", 'a+', encoding='utf-8') as fa:
        for n in range(num // 100):
            fa.write(slurm_nodes[n] + "\n")
    with open("hosts", 'a+', encoding='utf-8') as fa:
        for n in range(num):
            fa.write("{ip}  {hostname}".format(ip=ips[n], hostname=hostnames[n]) + "\n")


# 默认生成10000个slurm_node节点，如需修改数量，最好为100的倍数
gen_slurm_nodes(10000)
