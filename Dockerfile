# Python image kullanılıyor
FROM python:3.9-slim

# Çalışma dizinini ayarlıyoruz
WORKDIR /app

# Gereksinim dosyası varsa yükleyebiliriz (pip ile modüller kurulacak)
# Eğer herhangi bir `requirements.txt` dosyan yoksa, bu adımı atlayabilirsin
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Python script'i container'a kopyalıyoruz
COPY collector.py .

# Uygulamayı başlatma
CMD ["python", "collector.py"]
