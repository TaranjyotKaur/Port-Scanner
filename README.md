# Python Port Scanner

This is a simple multithreaded port scanner written in Python. It scans the TCP ports in the range 1-1000 on a target IP address or hostname and reports the open ports.

## Features

- **Automatic IP detection:** The script can automatically detect and use the local machine’s IP address for scanning.
- **Manual IP input:** Alternatively, you can manually enter any target IP address or hostname.
- **Multithreaded scanning:** Uses Python’s `ThreadPoolExecutor` to speed up the scanning process by scanning multiple ports concurrently.
- **Error handling:** Handles invalid hostnames and network errors gracefully.
- **Executable included:** A Python executable file is included for ease of use without needing a Python environment. (in the dist folder)

## Usage

### Automatic IP detection

By default, when you run the program, it fetches the IP address of the machine it's running on automatically and scans that IP.

The output will display the detected IP address and scan results for ports 1 to 1000 on that IP.

### Manual IP input

If you want to scan a different target, uncomment the following line in the `main()` function and comment out the automatic IP detection line: ```target = input("Enter the target host (e.g., 127.0.0.1 or example.com): ").strip()```

This allows you to enter any host or IP address manually when running the scanner.

## Requirements

- Python 3.x
- No external libraries required (uses standard library modules like `socket`, `concurrent.futures`, and `time`)

## Included Files

- `port_scanner.py` — The Python source code file containing the scanner.
- `port_scanner.exe` — A standalone executable file generated using PyInstaller for easy use on Windows without needing Python installed.


## How to Create Executable Yourself (Optional)

If you want to generate the executable yourself, use PyInstaller:
```pip install pyinstaller
    pyinstaller --onefile portscanner.py
```

This will create a `dist` folder containing the standalone executable.

## Disclaimer

Use this tool only on devices and networks you own or have explicit permission to test. Unauthorized scanning can be illegal and unethical.




