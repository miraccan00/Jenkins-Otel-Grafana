import requests

def fetch_metrics():
    # Prometheus'tan verileri al
    try:
        response = requests.get("http://prometheus:9090/metrics")
        response.raise_for_status()  # Hata olup olmadığını kontrol et
        return response.text  # Prometheus verileri metin formatında döner
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Prometheus: {e}")
        return None

def log_build_duration():
    metrics_data = fetch_metrics()
    if metrics_data:
        # Metin olarak gelen Prometheus metriklerini log dosyasına yaz
        with open("build_durations.log", "a") as log_file:
            log_file.write(metrics_data)

if __name__ == "__main__":
    log_build_duration()
