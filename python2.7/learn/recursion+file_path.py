# coding:utf-8
import os
# print os.getcwd()
# filename = '/home/cc/django1.10/include'
# print os.path.isdir(filename)

# 递归函数 注意开始标志与结束返回
"""
这个函数接受文件夹的名称作为输入参数，
返回该文件夹中文件的路径，
以及其包含文件夹中文件的路径。

"""


# 注意命名规范
def search_file(file_list):
    p_path = file_list[0]
    l = os.listdir(p_path)
    for each_path in l:
        # file = file_list[0]+'/'+each_file
        c_path = os.path.join(p_path, each_path)
        if os.path.isdir(c_path):
            temp_list = [c_path]
            t = search_file(temp_list)
            file_list.append(t)
        else:
            file_list.append(c_path)
    return file_list


def main():
    filename = ['/home/cc/django1.10']
    f = search_file(filename)
    for i in f:
        print i

if __name__ == '__main__':
    main()
