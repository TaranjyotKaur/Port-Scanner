import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

#local machine's IP address
def get_local_ip():
    try:
        #connect to public DNS server to get outbound IP 
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        return ip
    except Exception:
        #fallback if no network connectivity
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)


# for single port scan
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  #1-second timeout
            result = s.connect_ex((host, port))
            if result == 0:
                return port
    except socket.gaierror:
        raise ValueError("Invalid hostname or IP address.")
    except socket.error:
        raise ConnectionError("Network error or unreachable host.")
    return None


def main():
    #fetch ip
    target = get_local_ip()

    #if in case u want to manually search an IP adress use this line instead of automatic fetching:
    #target = input("Enter the target host (e.g., 127.0.0.1 or example.com): ").strip() 
    
    print(f"Target IP detected: {target}")

    ports_to_scan = range(1, 1001)  #Ports 1-1000

    print(f"\nStarting scan on {target}...\n")

    start_time = time.time()
    open_ports = []

    #ThreadPoolExecutor (10 threads)
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:  # More threads for faster scan
            futures = {executor.submit(scan_port, target, port): port for port in ports_to_scan}
            for future in as_completed(futures):
                port = futures[future]
                try:
                    result = future.result()
                    if result:
                        print(f"Port {result}: Open")
                        open_ports.append(result)
                except ValueError as ve:
                    print(f"Error: {ve}")
                    return
                except ConnectionError as ce:
                    print(f"Error: {ce}")
                    return

        end_time = time.time()
        duration = end_time - start_time

        
        print("\nScan complete.")
        print(f"Time taken: {duration:.2f} seconds")
        if open_ports:
            print("Open ports:")
            for port in open_ports:
                print(f"- Port {port}")
        else:
            print("No open ports found.")

    except KeyboardInterrupt:
        print("\nScan aborted by user.")


if __name__ == "__main__":
    main()