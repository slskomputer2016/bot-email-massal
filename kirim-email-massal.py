import smtplib
import time,datetime,os,random
from email.message import EmailMessage

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            item = [line.strip() for line in file if line.strip()]
        if not item:
            print("No item found in the file.")
            return []
        return item
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
def load_value(line,x):
    value = line.strip().split("#")
    return value[x]

def kirim_email(penerima,perusahaan):

    msg = EmailMessage()
    pengirim = "kantorkapbdg@gmail.com"
    msg["To"] = penerima
    msg["From"] = pengirim
    msg["Subject"] = "Penawaran Jasa Akuntan Publik"
    html = f"""
    <html>
    <body>
        <h2>Penawaran Jasa Akuntan Publik</h2>
        <p>Yth. Bapak/Ibu Pimpinan</p>
        <p>{perusahaan}</p>
        <p>
            Perkenalkan, saya Hendra dari Kantor Akuntan Publik (KAP) HSE Cabang Bandung, sebuah kantor akuntan publik yang telah berizin resmi dari Kementerian Keuangan dan terdaftar di Otoritas Jasa Keuangan (OJK).
            <br>Kami menawarkan layanan audit laporan keuangan, review laporan keuangan, serta jasa atestasi dan non-atestasi lainnya yang sesuai dengan standar profesional dan regulasi yang berlaku di Indonesia.
            <br>Dengan pengalaman tim auditor kami di berbagai sektor industri, kami berminat ikut partisipasi dalam Audit atau Penyusunan Laporan Keuangan {perusahaan}.

            <br><br>Beberapa keunggulan layanan kami:
            <br>- Tim auditor bersertifikat dan berpengalaman
            <br>- Pendekatan audit berbasis risiko dan efisiensi
            <br>- Komunikasi terbuka dan responsif selama proses audit

            <br><br>Apabila Bapak/Ibu berkenan, kami sangat terbuka untuk menjadwalkan pertemuan lebih lanjut, baik secara daring maupun langsung, 
            guna membahas kebutuhan audit di perusahaan Bapak/Ibu.
            Demikian perkenalan singkat dari kami. Besar harapan kami untuk dapat menjalin kerja sama dengan {perusahaan}.
        </p>
        <p>Terima kasih.</p>
        <p>A. Hendra</p><br>
        <p>085148329822</p>
        <p>https://kaphsebandung.com</p>
    </body>
    </html>
    """


    #-----------------------------------------
    #-----------------------------------------
    #-----------------------------------------
    msg.add_alternative(html, subtype="html")
    with open(r"D:\TUGAS_KANTOR\cp_hba.pdf", "rb") as file:
        data = file.read()
    msg.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename="cp_hba.pdf"
    )
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(pengirim, "hfxrijaatijhyajs")
        smtp.send_message(msg)
    print(f"Email berhasil dikirim ke {penerima}.")


if __name__ == "__main__":
    #hfxr ijaa tijh yajs
    file_email = load_file("./files/email-tes.txt")
    for line in file_email:
        email = load_value(line,0)
        perusahaan = load_value(line,1)
        kirim_email(email,perusahaan)
