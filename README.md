# AMUNRA
**amunra** is a tool that aims to simplify the process of data gathering on news website. Data gathering itself is time consuming, *I intend to make it quicker*. 

It automatically gathers links from a given search query, and also extract the content of a page from a link. Please note that currently **amunra** can only gather data from [Detik.com](https://www.detik.com) (Thanks Detik!). 

**More websites are coming soon!**

Installation
------------

Install with `pip`
```
$ pip install amunra
```

Now you can load the scrapper!
```
import amunra

ra = amunra.DetikScrapper()
```

Usage
------
### Gather data instantly
```
ra.gather_data("detik_saham.csv", "saham", "detik", 2)
```
Open `detik_saham.csv` and you will have a nice csv file ready for [pandas](https://pandas.pydata.org/)
```
url,title,body,word_count
"https://news.detik.com/berita/d-4441490/kampanye-di-bali-sandiaga-janji-tolak-reklamasi","Kampanye di Bali Sandiaga Janji Tolak Reklamasi",bali cawapres sandiaga uno mengatakan menolak proyek reklamasi yang merusak lingkungan alam khusus untuk tanjung benoa bali sandiaga janji akan mereview kebijakan itu jika lebih banyak merugikan nelayanhal itu disampaikan sandiaga saat berdialog dengan masyarakat tanjung benoa bendesa adat tanjung benoa made wijaya meminta sandiaga untuk meninjau kembali peraturan untuk proyek yang merusak lingkungan jika terpilih nanti kami berharap jika terpilih pak sandi bisa meninjau kembali proyek yang merusak terumbu karang dan kelangsungan hidup anak cucu juga kesejahteraan para nelayan ucap made wijaya di tanjung benoa bali minggu 2422019baca juga sandiaga ingin kembangkan pariwisata halal di balisandiaga menuturkan isu reklamasi ini juga dia bawa saat kampanye pilgub dki 2017 lalu pemberhentian reklamasi teluk jakarta pun akhirnya dia penuhi saat menjabat sebagai wagub dki jakarta bersama gubernur dki anies baswedan kalau masyarakat bali merasa reklamasi merusak lingkungan dan mengancam penghidupan para nelayan bersama masyarakat bali prabowosandi akan menolak reklamasi tegas sandi baca juga instruksi sandiaga ke emakemak kawal tps selfie dengan form c1sandiaga berjanji dia akan konsisten memenuhi janji kampanyenya apalagi jika proyek reklamasi itu lebih banyak merugikan masyarakat karena janji itu utang jika tidak ditagih di dunia akan kena di akhirat ucap sandisimak juga catat nih sandiaga janji tak lagi makan apel imporgambasvideo 20detik,204
...
```
---

### Getting links from a search term
```
ra.get_urls("urls.txt", "saham", "detik", 2)
```
Open `urls.txt` and you should see this:
```
https://finance.detik.com/bursa-dan-valas/d-4422865/balik-ke-zona-merah-ihsg-parkir-di-6515
https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei
https://finance.detik.com/bursa-dan-valas/d-4422490/ihsg-dibuka-menguat-tipis-di-awal-pekan
https://finance.detik.com/foto-bisnis/d-4414756/mengintip-bangunan-lantai-bursa-di-china
https://finance.detik.com/foto-bisnis/d-4379933/melantai-di-bursa-saham-kibif-naik-4118
https://finance.detik.com/foto-bisnis/d-4375140/bank-mandiri-angkat-direktur-komersial-baru
https://finance.detik.com/foto-bisnis/d-4370450/bri-kembali-tunjuk-wadirut-baru
https://finance.detik.com/foto-bisnis/d-4354330/sah-kini-51-saham-freeport-milik-indonesia
https://finance.detik.com/perencanaan-keuangan/d-4421163/gaji-rp-3-juta-mau-naik-haji-bisa-kok
https://finance.detik.com/bursa-dan-valas/d-4420943/dirut-bank-danamon-dapat-hibah-saham-rp-3-miliar
...
```
---
### Getting content from a link
```
ra.parse_from_url("output.csv", 
"https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei")
```
Open `output.csv` and you will have a nice csv file ready for [pandas](https://pandas.pydata.org/)
```
url,title,body,word_count
"https://finance.detik.com/bursa-dan-valas/d-4422769/menguat-140-saham-smartfren-dipelototi-bei","Menguat 140% Saham Smartfren Dipelototi BEI",jakarta  pt bursa efek indonesia bei meningkatkan pengawasan terhadap saham pt smartfren telecom tbk fren saham fren kini masuk dalam daftar unusual market activity umabei memandang adanya pergerakan harga yang di luar kewajaran di saham fren oleh karena itu pelaku pasar diminta untuk mencermati lebih dalam terhadap saham frensehubungan dengan terjadinya uma atas saham fren tersebut perlu kami sampaikan bahwa bursa saat ini sedang mencermati perkembangan pola transaksi saham ini kata kepala divisi pengawasan transaksi bei lidia m pandjaitan dilansir dari keterbukaan informasi senin 1122019jika dilihat saham fren memang terus menguat setidaknya selama sebulan ini tercatat saham fren yang kini bertengger di level rp 228 sudah meningkat 140 dalam waktu 1 bulanpeningkatan drastis terjadi pada seminggu kebelakang ini pada perdagangan 6 februari 2018 saham fren dalam sehari bisa meroker 333baca juga tips memilih saham zombiehingga siang ini saham fren tercatat sudah menguat 755 ke posisi rp 228 di posisi itu saham fren sudah ditransaksikan sebanyak rp 712 miliar        ,158
```

You can also do a batch operation by loading up a file from the above `get_urls()` function and load it to **amunra**:
```
ra.parse_from_file("output.csv", "urls.txt")
```
