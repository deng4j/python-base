import psutil
import datetime
import os


def monitor(interval):
    print(psutil.cpu_times())

    # 获取cpu硬件信息，定时获取
    cpu_info = psutil.cpu_percent(interval=interval)

    # 获取内存使用情况
    virtual_memory = psutil.virtual_memory()

    # 保存内存使用情况
    disk_usage = psutil.disk_usage("C:\\")

    # 获取网络收发数量
    io_counters = psutil.net_io_counters()

    # 获取系统时间
    now__strftime = datetime.datetime.now().strftime("%F %T")

    # 6、拼接字符串显示
    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
        psutil.cpu_count(logical=False), virtual_memory.total / 1024 / 1024 / 1024,
        disk_usage.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
        now__strftime, cpu_info, virtual_memory.percent, disk_usage.percent, io_counters.bytes_recv,
        io_counters.bytes_sent)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    print(log_str)


if __name__ == "__main__":
    while True:
        os.system('cls')  # 清除控制台
        monitor(3)
