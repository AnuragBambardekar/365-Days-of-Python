import urllib.request
import time

def measure_internet_speed():
    url = "http://speedtest.ftp.otenet.gr/files/test10Mb.db"
    file_size = 10 * 1024 * 1024  # 10MB in bytes

    print("Testing download speed...")
    start_time = time.time()
    urllib.request.urlretrieve(url, "speed_test_file.db")
    end_time = time.time()

    download_time = end_time - start_time
    download_speed = file_size / download_time / 10**6  # Convert to Mbps

    print("Speed Test Results:")
    print("Download Speed: {:.2f} Mbps".format(download_speed))

measure_internet_speed()
