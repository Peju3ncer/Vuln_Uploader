import requests
import argparse
import os

def upload_file(target, file_path):
    if not os.path.exists(file_path):
        print(f"[!] File '{file_path}' tidak ditemukan!")
        return
    
    url = target
    file_name = os.path.basename(file_path)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": url.rsplit("/", 1)[0],
        "Referer": url,
        "Connection": "keep-alive",
    }

    # Coba persis pakai field "upload"
    files = {
        "upload": (file_name, open(file_path, "rb"), "application/octet-stream")
    }

    try:
        r = requests.post(url, headers=headers, files=files, timeout=15)
        print(f"[+] Status: {r.status_code}")
        if r.status_code == 200:
            print(f"[+] File '{file_name}' dikirim!")
            print("[*] Response server:")
            print(r.text[:800])  # print maksimal 800 karakter respon
        else:
            print("[!] Upload gagal")
            print(r.text[:800])
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    # ASCII Art
    print(r"""
▗▖ ▗▖▗▄▄▖     ▗▖  ▗▖▗▖ ▗▖▗▖   ▗▖  ▗▖
▐▌ ▐▌▐▌ ▐▌    ▐▌  ▐▌▐▌ ▐▌▐▌   ▐▛▚▖▐▌
▐▌ ▐▌▐▛▀▘     ▐▌  ▐▌▐▌ ▐▌▐▌   ▐▌ ▝▜▌
▝▚▄▞▘▐▌        ▝▚▞▘ ▝▚▄▞▘▐▙▄▄▖▐▌  ▐▌
                                    
☬ 𝑀𝒶𝒹𝑒 𝒷𝓎: 𝒫𝑒𝒿𝓊𝟥𝓃𝒸𝑒𝓇 - 𝓋𝟣.𝟢☬
    """)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="URL upload target")
    parser.add_argument("--file", required=True, help="Path file yang mau diupload")
    args = parser.parse_args()

    upload_file(args.target, args.file)
