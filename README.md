# ChatKTI Backend

## Deskripsi
Proyek ini adalah backend untuk aplikasi ChatKTI yang menggunakan teknologi LLM (Large Language Model) dan LangChain.

## Instalasi
1. Clone repositori ini:
    ```bash
    git clone <URL_REPOSITORI>
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd chatkti_backend
    ```
3. Buat dan aktifkan virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # Untuk pengguna Unix atau MacOS
    .\env\Scripts\activate   # Untuk pengguna Windows
    ```
4. Install dependensi:
    ```bash
    pip install -r requirements.txt
    ```
5. Buat .env file
    Copy file `.env.example` menjadi `.env` dan isikan environment variable untuk ChatGroq.

## Penggunaan
1. Jalankan server:
    ```bash
    python main.py
    ```
2. Akses aplikasi di browser pada `http://localhost:8000`.

## Struktur Direktori
- `docs/`: Berisi dokumen pedoman penulisan karya tulis ilmiah
- `pkti23_db/`: Berisi vector database dari hasil embending dokumen
