
# Documentation for the Authorized DoS Testing Script for SAMP Server

## Overview
This Python script is designed to perform **Authorized DoS (Denial of Service)** testing on **SAMP** (San Andreas Multiplayer) servers to assess their security and resilience. The script sends **HTTP GET** and **POST** request packets to overload the server's capacity and can be used to identify vulnerabilities or limitations in controlled and authorized environments.

This type of testing **should only be performed with explicit permission** from the server owner, in a **testing or staging environment**, never on production servers without proper consent.

---

## Features

1. **Authorized DoS Testing:**
   - Sends **GET** and **POST** requests in large quantities.
   - Allows you to test the server's behavior under heavy load.
   - Performs tests in continuous loops to simulate constant pressure on the server.

2. **Server Status Monitoring:**
   - Checks if the server is online.
   - Performs a **ping** to check network connectivity.
   - Displays the server status, including the HTTP response from the server (200, 404, etc.).

3. **Colored and Informative Messages:**
   - Messages displayed in the terminal are colored for easy interpretation of the status.
   - Colors help highlight issues like server **offline**, **connection errors**, or **status responses**.

4. **Looped Execution:**
   - The script runs in a continuous loop, sending packets to test the server’s ability to maintain stability under load.

5. **High Customization:**
   - Variables in the code can be easily modified to adjust the number of requests or the interval between them.

---

## How to Use

1. **Prerequisites:**
   - Python 3.x installed.
   - The `requests` and `termcolor` libraries are required. You can install them with:

     ```bash
     pip install requests termcolor
     ```

2. **Running the Script:**
   - After installing the dependencies, run the script and provide the **IP** and **port** of the SAMP server to start the authorized DoS testing.

     **Command to run the script:**

     ```bash
     python dos_test.py
     ```

3. **User Input:**
   - During execution, the script will ask for:
     - **SAMP server IP address** (Example: `190.102.41.96`).
     - **SAMP server port** (Example: `7015`).

4. **Expected Output:**
   - The script will display information about the server's connectivity, including whether it is online or offline, the server's HTTP response (status), and the status of the requests sent.

---

## Example Execution

When running the script, you will see output like this:

```
Enter the SAMP server IP to test: 190.102.41.96
Enter the SAMP server port: 7015
Starting authorized DoS test on the server...

Server 190.102.41.96 is ONLINE.
Ping to 190.102.41.96 successful.
Sending GET and POST requests...

GET request 1/50 sent. Status: 200
POST request 1/50 sent. Status: 200
GET request 2/50 sent. Status: 200
...
```

---

## How to Modify the Script

You can easily modify the script to change its behavior as needed. Here are some possible customizations:

### 1. **Change the Number of GET and POST Requests**
The variables `RQS_GET` and `RQS_POST` control the number of GET and POST requests sent, respectively.

```python
RQS_GET = 50  # Number of GET requests to send
RQS_POST = 50  # Number of POST requests to send
```

### 2. **Change the Interval Between Requests**
The interval between requests can be adjusted with the `REQUEST_INTERVAL` variable:

```python
REQUEST_INTERVAL = 1  # Interval in seconds between each request
```

### 3. **Configure the Timeout for Connections**
The timeout for connections and requests can be set in the `REQUEST_TIMEOUT` variable:

```python
REQUEST_TIMEOUT = 5  # Timeout in seconds for connections and HTTP requests
```

### 4. **Modify the Displayed Messages**
You can modify the messages displayed in the terminal. The messages are colored using the `termcolor` library, and you can change both the text and the colors:

```python
print(colored(f"Server {ip} on port {port} is ONLINE.", 'green'))
```

### 5. **Add More Functionality**
- **Add More Request Types:** You can add other types of HTTP requests, such as `PUT` or `DELETE`, to test different aspects of the server.
- **Log Writing:** To store the request results in a log file, you can add code to record information in a text file.

---

## Explanation of Functions

### 1. **`check_server_online(ip, port)`**
   - Checks if the server is reachable on the specified port.
   - Returns `True` if the server is online, or `False` if the server is offline.

### 2. **`send_requests(ip)`**
   - Sends **GET** and **POST** requests to the server.
   - The requests are sent according to the `RQS_GET` and `RQS_POST` variables.
   - Displays the status of each request sent, indicating whether the request was successful.

### 3. **`ping_server(ip)`**
   - Performs a **ping** to check the connectivity to the server.
   - Displays the ping result in the terminal, indicating if the server is reachable.

### 4. **`monitor_server(ip, port)`**
   - Performs continuous monitoring of the server.
   - Checks the status and sends requests in a continuous loop.
   - Displays the status of each operation in the terminal.

### 5. **`dos_attack(ip, port)`**
   - Performs the authorized DoS attack by sending a large number of requests to overload the server.
   - Displays the number of packets sent and the status of each one.

---

## Important Considerations

1. **Explicit Permission:** This script **should only be used on servers that you have explicit permission** to perform DoS tests on. Using this script on servers without proper authorization is **illegal** and could result in legal actions against the user.

2. **Use in Controlled Environments:** Ideally, the script should be run in **testing environments** or **staging servers**, where the impact of a potential **DoS** does not affect users or other services.

3. **User Responsibility:** The use of this script is the **sole responsibility of the user**. Make sure to obtain the necessary consent before performing any DoS testing.
