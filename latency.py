import requests
import time

def measure_latency(url, num_requests=10):
    latencies = []

    for _ in range(num_requests):
        start_time = time.time()
        try:
            response = requests.get(url)
            # You can replace 'get' with the HTTP method you are testing
            response.raise_for_status()
            end_time = time.time()
            latency = end_time - start_time
            latencies.append(latency)
            print(f"Request took {latency:.4f} seconds")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    average_latency = sum(latencies) / len(latencies) if latencies else 0
    print(f"\nAverage Latency: {average_latency:.4f} seconds")

if __name__ == "__main__":
    # Replace 'http://your-app-url' with the actual URL of your application
    app_url = "http://your-app-url"
    measure_latency(app_url)
