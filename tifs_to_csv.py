import glob
from osgeo import gdal
import csv
import os


def GetTifInfo(filename):
    datafile = gdal.Open(filename)
    im_width = datafile.RasterXSize  # 栅格矩阵的列数
    im_height = datafile.RasterYSize  # 栅格矩阵的行数
    extent = datafile.GetGeoTransform()  # 仿射矩阵，左上角像素的大地坐标和像素分辨率 extent=(-180.0, 0.05, 0.0, 90.0, 0.0, -0.05)
    img = datafile.GetRasterBand(1).ReadAsArray()  # dataset.GetRasterBand(1) 用于获取数据集的第一个波段，而 ReadAsArray()
    # 方法用于将这个波段的像素数据读取为一个数组。
    datafile = None
    return img, im_height, im_width, extent


def WriteCsv(filename, csv_file):
    img, height, width, extent = GetTifInfo(filename)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Lon", "lat", "value"])
        for row in range(height):
            for col in range(width):
                value = img[row, col]
                lon = float(round(col * 0.05 + extent[0], 2))
                lat = float(round(extent[3] - row * 0.05, 2))
                writer.writerow([lon, lat, float(value)])


def OpenTif(tif_pattern, csv_dir):
    # 使用glob获取所有匹配的文件路径
    tif_files = glob.glob(tif_pattern)
    for tif_file in tif_files:
        csv_file_time = os.path.splitext(os.path.basename(tif_file))[0]
        WriteCsv(tif_file, csv_dir + csv_file_time + ".csv")
        print("写入文件:" + csv_file_time + ".csv" + " ,Ok!")


if __name__ == '__main__':
    # 设置tif文件的路径模式
    tif_pattern = "D:\\study\\COD\\*.tif"
    csv_dir = "D:\\study\\COD_CSV\\"
    OpenTif(tif_pattern, csv_dir)
