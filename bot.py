import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def run_bot():
    # Akses credential Google
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # Buka spreadsheet
    sheet = client.open("Nama Spreadsheet Kamu").sheet1  # Ganti dengan nama sheet kamu

    # Ambil semua baris
    rows = sheet.get_all_records()

    # Cari baris pertama yang belum dikirim (status kosong)
    for i, row in enumerate(rows):
        if not row['status']:
            print(f"Proses link: {row['link']}")

            # --- Di sini nanti scraping website & submit komentar ---
            # Tambahkan scraping pakai Selenium di sini

            # Update status di sheet
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.update_cell(i+2, 6, "sukses")        # kolom status
            sheet.update_cell(i+2, 7, waktu)           # kolom waktu_kirim
            break
