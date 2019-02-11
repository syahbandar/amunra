# AmunRa
AmunRa: A web scraping tool for Indonesian news website

Installation
------------

1. Clone this repository
2. From the directory:
```
from main import amunra

ar = amunra()
```

Usage
------

### Getting links from a search term
```
ar.get_urls("urls.txt", "saham", "detik", 2)
```
Open `urls.txt` and you should see this:
```
https://finance.detik.com/bursa-dan-valas/d-4422865/balik-ke-zona-merah-ihsg-parkir-di-6515
https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei
https://finance.detik.com/bursa-dan-valas/d-4422490/ihsg-dibuka-menguat-tipis-di-awal-pekan
https://finance.detik.com/market-research/d-4422470/oso-securities-ihsg-diperkirakan-menguat-ke-6581
https://finance.detik.com/foto-bisnis/d-4414756/mengintip-bangunan-lantai-bursa-di-china
https://finance.detik.com/foto-bisnis/d-4379933/melantai-di-bursa-saham-kibif-naik-4118
https://finance.detik.com/foto-bisnis/d-4375140/bank-mandiri-angkat-direktur-komersial-baru
https://finance.detik.com/foto-bisnis/d-4370450/bri-kembali-tunjuk-wadirut-baru
https://finance.detik.com/foto-bisnis/d-4354330/sah-kini-51-saham-freeport-milik-indonesia
https://finance.detik.com/perencanaan-keuangan/d-4421163/gaji-rp-3-juta-mau-naik-haji-bisa-kok
https://finance.detik.com/bursa-dan-valas/d-4420943/dirut-bank-danamon-dapat-hibah-saham-rp-3-miliar
https://finance.detik.com/bursa-dan-valas/d-4419643/seharian-di-zona-merah-ihsg-ditutup-di-level-6521
https://finance.detik.com/bursa-dan-valas/d-4419379/sampai-7-februari-modal-asing-masuk-ri-rp-496-triliun
https://finance.detik.com/berita-ekonomi-bisnis/d-4419348/crazy-rich-kakak-beradik-perang-tarif-sang-adik-bangkrut
https://finance.detik.com/berita-ekonomi-bisnis/d-4419262/perang-dagang-deadpool-vs-wolverine
https://finance.detik.com/foto-bisnis/d-4102417/pt-transcoal-pacific-tbk-melantai-di-bursa
https://finance.detik.com/foto-bisnis/d-4094609/anak-usaha-pelindo-ii-tawarkan-saham
...
```

### Getting content from a link
```
ar.parse_from_url("output.csv", 
"https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei")
```
Open `output.csv` and you will have a nice csv file ready for pandas
```
"id", "url", "title", "body", "word_count"
"1","https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei","Menguat 140% Saham Smartfren Dipelototi BEI","\nJakarta - PT Bursa Efek Indonesia (BEI) meningkatkan pengawasan terhadap saham PT Smartfren Telecom Tbk (FREN). Saham FREN kini masuk dalam daftar unusual market activity (UMA).BEI memandang adanya pergerakan harga yang di luar kewajaran di saham FREN. Oleh karena itu pelaku pasar diminta untuk mencermati lebih dalam terhadap saham FREN.Sehubungan dengan terjadinya UMA atas saham FREN tersebut perlu kami sampaikan bahwa Bursa saat ini sedang mencermati perkembangan pola transaksi saham ini kata Kepala Divisi Pengawasan Transaksi BEI Lidia M. Pandjaitan dilansir dari keterbukaan informasi Senin (11/2/2019).\nJika dilihat saham FREN memang terus menguat setidaknya selama sebulan ini. Tercatat saham FREN yang kini bertengger di level Rp 228 sudah meningkat 140% dalam waktu 1 bulan.Peningkatan drastis terjadi pada seminggu kebelakang ini. Pada perdagangan 6 Februari 2018 saham FREN dalam sehari bisa meroker 333%.Baca juga: Tips Memilih Saham 'Zombie'Hingga siang ini saham FREN tercatat sudah menguat 755% ke posisi Rp 228. Di posisi itu saham FREN sudah ditransaksikan sebanyak Rp 712 miliar.        (das/dna)\n\n\n\n\n \n",1135
```

You can also do a batch operation by loading up a file from the above `get_urls()` function and load it to **amunra**:
```
ar.parse_from_file("output.csv", "urls.txt")
```
