# Telegram Mentions Bot

Bot Telegram untuk mention otomatis anggota group dengan fitur partner, batching, dan template custom.

## Fitur Utama
- Mention anggota group secara otomatis sesuai link partner
- Batching: mention beberapa user per interval
- Template /start custom (caption, gambar, tombol multi-baris)
- Owner dapat mengatur semua konfigurasi via command
- Statistik harian dan total
- Dukungan tombol JSON multi-baris
- Variabel template: `{mention}`, `{user}`, `{user_id}`, `{link}`
- Tombol ❌ Close otomatis

## Instalasi
1. Clone repo:
   ```bash
   git clone https://github.com/iamnolimit/telegrammentionsbot.git
   cd telegrammentionsbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Isi `config.py` dengan BOT_TOKEN, API_ID, API_HASH, OWNER_ID.

## Menjalankan Bot
```bash
python main.py
```

## Konfigurasi Owner
- Semua command owner via chat private:
  - `/setbasegroup <group_id>`: Set group utama
  - `/setmaxmention <jumlah>`: Limit mention per partner per hari
  - `/setusersbatch <jumlah>`: User per batch
  - `/setloggroup <group_id>`: Set group log
  - `/setusermsg <pesan>`: Pesan notifikasi user
  - `/setlogmsg <pesan>`: Template log
  - `/partners`: Lihat partner
  - `/addpartner <link> <durasi_menit>`: Tambah partner
  - `/removepartner <link>`: Hapus partner
  - `/mentions`: Lihat mention aktif
  - `/clearmention <user_id|all|expired>`: Hapus mention
  - `/resetdaily <link|all>`: Reset counter harian
  - `/dailystats`: Statistik harian
  - `/stats`: Statistik total
  - `/setstart <caption> | <image_url> | <button_json>`: Atur template /start

### Format /setstart
- Caption bisa pakai variabel:
  - `{mention}`: mention user
  - `{user}`: username
  - `{user_id}`: user ID
  - `{link}`: link partner
- Tombol format JSON multi-baris:
  ```json
  [[{"text": "Info", "url": "https://t.me/botinfo"}], [{"text": "Close", "callback": "close"}]]
  ```
- Gambar opsional.
- Tombol ❌ Close otomatis ditambah jika belum ada.

## File & Struktur
- `main.py`: Entry point bot
- `handlers/`: Semua handler command
- `database.py`: Database logic
- `config.py`: Konfigurasi bot
- `taskmanager.py`: Task mention
- `utils.py`: Helper

## .gitignore
- Database, session, cache, dan file sensitif tidak ikut git.

## Lisensi
MIT