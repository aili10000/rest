import os


def fun(binpath, fpath):
    file_path = os.walk(fpath)
    for name in file_path:
        print(name[2])
        for filename in name[2]:
            # os.popen()
            jpg_name = filename.split('.')
            jpg_name_name = jpg_name[0]
            jpg_jpg = jpg_name[1]

            if not jpg_jpg == 'jpg':
                cmd = binpath + " -ss 2 -i " + fpath + filename + " -y -f  image2 -t 0.001 -s 720x576 " + fpath + jpg_name_name + ".jpg"
                print(cmd)
                os.popen(cmd)


# 将视频第2秒的图像截取
def cut(binpath, fpath, picpath):
    file_list = os.listdir(fpath)
    for item in file_list:
        try:
            filename = item.split('.')[0]
            cmd = binpath + " -ss 2 -i " + fpath + item + " -y -f  image2 -t 0.001 -s 720x576 " + picpath + filename + ".jpg"
            print(cmd)
            er = os.popen(cmd)
            print(er.read())
        except Exception as e:
            print(e)


# 给MP4加上文件头，运行拖动
def mp4Start(binpath, fpath, moviepath):
    file_list = os.listdir(fpath)
    for item in file_list:
        if not os.path.isdir(os.path.join(fpath, item)):
            cmd = binpath + ' ' + fpath + item + ' ' + moviepath +item
            print(cmd)
            pt = os.popen(cmd)
            print(pt.read())


# 防止MP4文件加文件头是报错，先用ffmpeg转换一下
def mp4start1(binpath, fpath):
    file_list = os.listdir(fpath)
    new_path = fpath[:-4]
    for it in file_list:
        # cmd = ffmpeg -i D:\1\mp4\old\3.mp4 -acodec copy -vcodec copy D:\1\movie\11.mp4
        cmd = binpath + ' -i ' + fpath + it + ' -acodec copy -vcodec copy ' + new_path + it
        print(cmd)
        cmd_info = os.popen(cmd)
        print(cmd_info.read())


if __name__ == '__main__':
    # fun("D:\\1\\ffmpeg\\bin\\ffmpeg", "d:\\1\\mp4\\")
    # cut("D:\\1\\ffmpeg\\bin\\ffmpeg","d:\\1\\mp4\\",'d:\\1\pic\\')

    # mp4start1('D:\\1\\ffmpeg\\bin\\ffmpeg', 'd:\\1\\mp4\\old\\')
    mp4Start('D:\\1\\ffmpeg\\bin\\qt-faststart', 'd:\\1\\mp4\\', 'd:\\1\\movie\\')
