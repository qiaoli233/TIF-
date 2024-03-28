import csv
import os
import glob


def get_cod(input_lon, input_lat, date):
    csv_file = get_file(date)  # 根据输入日期查询对应csv文件的地址
    if csv_file is not None:  # 判断查找到的文件
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # 跳过第一行表头
            for row in reader:  # 按行读取csv数据
                lon, lat = float(row[0]), float(row[1])  # 转换成浮点类型的数据方便匹配
                if lon == float(input_lon) and lat == float(input_lat):  # 判断该行经度和纬度是否与输入的经纬度一致
                    print("时间:" + date + "\n经度:" + row[0] + "\n纬度：" + row[1] + "\n光学厚度：" + row[2])  # 打印时间、经纬度、和该点光学厚度
                    return None  # 找到之后停止遍历


def get_file(date):
    files = glob.glob(filepath)  # 读取路径下所有的文件
    for file in files:
        filename = os.path.splitext(os.path.basename(file))[0]  # filename赋值文件的名字，去除后缀名
        filetime = filename[:filename.index('_')]  # 从文件名截取文件日期
        if filetime == str(date):  # 如果匹配成功，打印文件地址，返回文件地址
            print("找到文件：", file)
            return file
    print("找不到该日期对应的csv文件！！！")
    return None  # 找不到文件返回None


def get_info():
    data = input("请输入时间：")
    lon = input("请输入经度：")
    lat = input("请输入纬度：")
    get_cod(lon, lat, data)


if __name__ == "__main__":
    filepath = "D:\\study\\COD_CSV\\*.csv"
    get_info()
