# pip install speedtest-cli

import speedtest

def measure_internet_speed():
    st = speedtest.Speedtest()
    print("Testing download speed...")
    download_speed = st.download() / 10**6  # Convert to Mbps
    print("Testing upload speed...")
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    print("Speed Test Results:")
    print("Download Speed: {:.2f} Mbps".format(download_speed))
    print("Upload Speed: {:.2f} Mbps".format(upload_speed))

measure_internet_speed()
