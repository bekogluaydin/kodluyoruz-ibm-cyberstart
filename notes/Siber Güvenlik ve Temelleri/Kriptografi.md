# Kriptografiye giriş

Kriptografi bir matematik alanınıdır, bu konuda kriptografiyi tanıtacağız. Kriptografi, bilgi güvenliği kapsamındaki hayati kavramların temelini oluşturur ve başarılı olmak isteyen tüm siber güvenlik uzmanlarınca anlaşılması gerekir.

Kriptografi, kod yazma ve çözme sanatı olarak tanımlanır.

bilgileri gizli tutmanın bilgi güvenliğinin temel amaçlarından biri olduğunu belirtmiştik. Sırların tutulup saklanması, binlerce yıldır var olan bir zorluktur. Bunu başarmaya yönelik yöntemler yıllar boyunca değişmiş olsa da, amaçlar genel olarak aynı kalmıştır.

## 1. Güvenli iletişimlerin tanımlanması

Alice, Bob ve Eve adlı üç katılımcının olduğu bir durum hayal edin. Bu üç karakter, kavramları örneklerle açıklamak amacıyla şifreleme alanında yıllardır kullanılıyor. Alice ve Bob gizli iletişim kurmak ister, Eve ise konuşmaya kulak misafiri olmak (eavesdrop) ister, "Eve" adı da buradan gelir.


![image](https://github.com/user-attachments/assets/fe5d7802-6b37-4c9f-a4d5-7060742faccd)

Güvenli iletişim kurmak için gözetilmesi gereken **üç temel özellik** vardır.

### 1. Özellik: Gizlilik

Alice, Bob'a içeriği Eve tarafından anlaşılamayan bir mesaj gönderebilir. Bu özellik, mesajın gizli ve özel olduğu anlamına gelir.

### 2. Özellik: Gerçeklik

Eve, Bob'a Alice olduğunu iddia ederek mesaj gönderemez. Bu özellik, yanıltmanın ya da taklit etmenin imkansız olmasını sağlamakla alakalıdır.

### 3. Özellik: Bütünlük

Eve, Alice ile Bob arasındaki bir mesajı değiştirirse, alıcı mesajın değiştirildiğini fark edebilir. İçeriği bilmeden mesajları kurcalamak mümkündür. Örneğin insanlar, anlamadıkları bir dildeki konuşmayı engellemek için yüksek sesle konuşabilirler.

Bu üç özellik, bir dizi matematiksel algoritma ve diğer tekniklerle elde edilir. Geçmişte kilitli kutular ya da mumdan mühürler vardı, ancak bu derste daha çok matematiksel seçeneklere odaklanacağız!

### 2. Şifreleme

Şifreleme, bir mesajın süreci tersine çevirecek şifre çözme anahtarına sahip kişiler haricinde anlaşılamayacak farklı bir şeye dönüştürülmesidir. Bir mesaj okunamayacak duruma getirildiğinde, şifrelendiği söylenir. Genel hatlarıyla, günümüz dünyasında kullanılan iki şifreleme biçimi bulunur: simetrik ve asimetrik.

#### 2_A. Simetrik şifreleme

Simetrik şifrelemede, bilginin şifrelenmesine yönelik algoritma, şifre çözme işlemiyle ***aynı anahtarı*** kullanır. Simetrik şifreleme hızlıdır ve uygulanması kolaydır. Hem göndericinin hem de alıcının aynı anahtara erişimi olmasına dayanır, gizli bilgi bağlantısını korumaya yönelik bir tür parola veya "paylaşılan gizli anahtar" gibidir.

***Bir örnek verelim;***
Karakterlerin alfabede sabit sayıda ileri veya geri yönde artırılıp azaltıldığı rotasyon tabanlı şifre buna basit bir örnektir. İleri veya geriye doğru yapılacak hareket sayısı anahtar işlevi görür. Gönderen +1'lik bir anahtar kullanıyorsa her bir karakteri alfabede kendinden 1 sonraki karakter ile değiştirir ve daha sonra alıcı, asıl mesajı almak için -1'lik rotasyon uygular. Bu şifrede, "TATİL" sözcüğü alfabede +1'lik bir kaydırma yoluyla şifrelenerek "UBUJM" olarak değiştirilir.


![image](https://github.com/user-attachments/assets/30e1e0c1-85af-420b-9f32-39faad7adbcb)

Günümüzde kullanılan ve simetrik modelleri izleyen algoritmalar, Otomatik Şifreleme Standardının (AES) versiyonlarını içerir. Tarayıcınız da bu sayfayı güvenli olarak görüntülemek için muhtemelen bunu kullanıyor!

#### 2_B. Asimetrik şifreleme

Asimetrik şifrelemede, bilgiyi şifreleme işlemi, bilginin şifresini çözmek için ***farklı bir anahtar*** kullanır. Bu anahtarlar, ***genel anahtarlar*** ve ***özel anahtarlar*** olarak bilinir. Aynı anda üretilirler. Bir genel anahtar üretildiğinde, bunu herkesle paylaşabilirsiniz. Genel anahtarın bir kopyasına sahip herkes mesajı şifreleyebilir, bu mesajın şifresi ise sadece özel anahtara sahip kişi tarafından çözülebilir.

***Bir örnek verelim;***
Bu grafikte Alice gönderici, Bob da alıcıdır. Grafik, iletim işlemini gösterir. Alice, mesajı Bob'un genel anahtarıyla şifreler. Mesaj şifrelendikten sonra ancak Bob'un özel anahtarı kullanılarak çözülebilir. Şifrelenen mesaj, Bob'a gönderilir. Ardından Bob kendi özel anahtarını kullanarak mesajın şifresini çözebilir. Bob'un özel anahtarını hiç kimseyle paylaşmaması gerekir, aksi takdirde gelen tüm mesajları okunabilir.

![image](https://github.com/user-attachments/assets/13200ec8-5e92-42ab-a5b1-a0a604ac2ddb)

Asimetrik şifrelemenin sunduğu temel avantaj, kuruluşların daha önce bir "anahtar" alışverişinde bulunmadıkları bir kişi veya kurumla gizli olarak iletişim kurabilmeleridir. Ayrıca bu şifreleme türü, bir mesajın doğru kişiye gönderilmesini garanti edebilir.

***Bir örnek verelim;***
Asimetrik şifrelemenin avantajlarından biri, çevrimiçi alışveriş yoluyla açıklanabilir. Müşteriler, paylaşılan, benzersiz ve simetrik bir anahtar oluşturmak için bizzat mağazaya gitmeden alışveriş yapabilirler.

Simetrik kriptografi tek seçenek olsaydı, müşteri ile mağaza arasında gelecekte gerçekleşecek tüm işlemleri şifreleyip çözmek için kabul edilen simetrik anahtarın kullanılması gerekirdi.

Buna kıyasla asimetrik şifreleme kullanmak daha kolaydır ve bizzat buluşmaya gerek olmadığından vakit kazandırır. Bu avantaj olmasaydı, çevrimiçi alışverişi güvenli bir şekilde kullanmak neredeyse imkansız olurdu.

### 3. Kriptografi Aktivite 

Şifrelemeyi öğrenmenin en kolay yolu, onu denemektir! CyberChef adlı araç, Birleşik Krallık Devlet İletişim Merkezi (GCHQ) tarafından, şifreleme gibi veri işleme operasyonlarına yardımcı olmak üzere yazılmış web tabanlı bir araçtır. CyberChef'te şifrelenmiş bir mesaj, bir tarifte bir dizi adım uygulanarak "pişirilecek" malzemeyi temsil eder. Şu adımları izleyin.

+ [CyberChef](https://gchq.github.io/CyberChef/)'e gidin.
+ Şu şifrelenmiş mesajı kopyalayıp Input  alanına yapıştırın: ftue ue m fqef eqzfqzoq 
+ Soldaki gezinme bölmesinde listelenen işlemlerde aşağıya doğru inerek Encryption / Encoding bölümünü bulun ve genişletin.
+ ROT13 öğesini seçip Recipe kutusundaki boş alana sürükleyin. Bu, aracın karakterleri alfabede 13 sıra ilerideki karakterlerle değiştireceği anlamına gelir. Auto Bake seçeneği varsayılan olarak etkindir, böylece Output alanının değiştiğini görürsünüz.
+ Şimdi Amount alanındaki yukarı ve aşağı oklara tıklayarak, Output alanında mesajın nasıl değiştiğine bakın. Mesajın şifresini çözmek istiyorsunuz. Output  bölümündeki mesaj, İngilizce kısa bir cümle olarak anlam kazandığında durun.

Şifresi çözülen mesaj ne? Cevap olarak neyi buldunuz? Cevabı kontrol etmek için bu [CyberChef web sayfasını](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,true,14)&input=ZnR1ZSB1ZSBtIGZxZWYgZXF6ZnF6b3Eg) ziyaret edin. 

