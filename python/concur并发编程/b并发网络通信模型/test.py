import os

FTP = "/home/pc/FTP/"  # 文件库路径


class FtpServer:
    def __init__(self, FTP_PATH):
        self.path = FTP_PATH

    def do_list(self):
        # 获取目录下所有文件并组成列表
        files = os.listdir(self.path)
        print(files)  #
        if not files:
            print("该文件类别为空")
            return
        else:
            print(b'OK')
        for file in files:
            if file[0] != '.' and os.path.isfile(self.path + file):
                print(file)

        print(b'##')


def handle():
    FTP_PATH = FTP + "Data" + '/'
    ftp = FtpServer(FTP_PATH)
    print(FTP_PATH)
    data = "LData"
    print(data[0])
    if data[0] == 'L':
        ftp.do_list()


if __name__ == '__main__':
    handle()
