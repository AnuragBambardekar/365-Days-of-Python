"""
Network usage per process

pip install scapy
"""

from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

all_macs = {iface.mac for iface in ifaces.values()} # MAC addresses of all network interfaces in my machine
connection2pid = {} # maps each connection (source:destination ports)
pid2traffic = defaultdict(lambda:[0,0]) # maps each process ID to a list of 2 values representing upload and download traffic
global_df = None # store previous traffic data
is_program_running = True # will set to False, when program exits

def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def process_packet(packet):
    global pid2traffic
    try:
        packet_connection = (packet.sport, packet.dport)
    except (AttributeError, IndexError):
        pass # sometimes packet does not TCP/UDP layers, so we ignore
    else:
        # get the PID
        packet_pid = connection2pid.get(packet_connection)
        if packet_pid:
            if packet.src in all_macs:
                pid2traffic[packet_pid][0] += len(packet)
            else:
                pid2traffic[packet_pid][1] += len(packet)

def get_connections():
    global connection2pid
    while is_program_running:
        for c in psutil.net_connections():
            if c.laddr and c.raddr and c.pid:
                connection2pid[(c.laddr.port, c.raddr.port)] = c.pid
                connection2pid[(c.raddr.port, c.laddr.port)] = c.pid
        time.sleep(1)

#calculate the network usage and print data
def print_pid2traffic():
    global global_df
    processes = []
    for pid, traffic in pid2traffic.items():
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            continue
    
        name=p.name()
        try:
            create_time = datetime.fromtimestamp(p.create_time())
        except OSError:
            create_time = datetime.fromtimestamp(psutil.boot_time())
        
        process = {
            "pid":pid,
            "name":name,
            "create_time":create_time,
            "Upload": traffic[0],
            "Download":traffic[1]
        }
        try:
            process["Upload Speed"] = traffic[0] - global_df.at[pid, "Upload"]
            process["Download Speed"] = traffic[1] - global_df.at[pid, "Download"]
        except (KeyError, AttributeError):
            process["Upload Speed"] = traffic[0]
            process["Download Speed"] = traffic[1]

        processes.append(process)

    df = pd.DataFrame(processes)
    try:
        df = df.set_index("pid")
        df.sort_values("Download", inplace=True, ascending=False)
    except KeyError as e:
        pass

    printing_df = df.copy()
    try:
        printing_df["Download"] = printing_df["Download"].apply(get_size)
        printing_df["Upload"] = printing_df["Upload"].apply(get_size)
        printing_df["Download Speed"] = printing_df["Download Speed"].apply(get_size).apply(lambda s: f"{s}/s")
        printing_df["Upload Speed"] = printing_df["Upload Speed"].apply(get_size).apply(lambda s: f"{s}/s")
    except KeyError as e:
        pass

    os.system("cls") if "nt" in os.name else os.system("clear")
    print(printing_df.to_string())
    global_df=df


def print_stats():
    """Simple function that keeps printing the stats"""
    while is_program_running:
        time.sleep(1)
        print_pid2traffic()
        

if __name__ == "__main__":
    # start the printing thread
    printing_thread = Thread(target=print_stats)
    printing_thread.start()
    # start the get_connections() function to update the current connections of this machine
    connections_thread = Thread(target=get_connections)
    connections_thread.start()
    
    # start sniffing
    print("Started sniffing")
    sniff(prn=process_packet, store=False)
    # setting the global variable to False to exit the program
    is_program_running = False   