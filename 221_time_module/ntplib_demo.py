import ntplib
from datetime import datetime

def get_atomic_clock_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')  # You can use any NTP server you prefer
    
    atomic_time = datetime.fromtimestamp(response.tx_time)
    return atomic_time

if __name__ == "__main__":
    atomic_time = get_atomic_clock_time()
    print("Atomic Clock Time:", atomic_time)

"""
The pool.ntp.org project is a big virtual cluster of timeservers providing reliable easy to use NTP service for millions of clients.

The pool is being used by hundreds of millions of systems around the world. It's the default "time server" for most of the major 
Linux distributions and many networked appliances.
"""
"""
The NTP pool is a dynamic collection of networked computers that volunteer to provide highly accurate time via the Network Time Protocol 
to clients worldwide. The machines that are "in the pool" are part of the pool.ntp.org domain as well as of several subdomains divided by 
geographical zone and are distributed to NTP clients via round robin DNS. Work is being done to make the geographic zone selection 
unnecessary, via customized authoritative DNS servers that utilize geolocation software.

As of May 2022 the pool consists of 3,126 active time servers on IPv4 and 1,534 servers on IPv6. Because of the decentralization of 
this project accurate statistics on the number of clients cannot be obtained, but according to the project's website the pool provides 
time to 5–15 million systems.Because of client growth the project is in perpetual need of more servers. ~ Wikipedia
"""