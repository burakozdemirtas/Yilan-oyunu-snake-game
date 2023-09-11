import turtle  # Turtle grafik kütüphanesini içe aktarıyoruz.
import time  # Zaman işlemleri için "time" modülünü içe aktarıyoruz.
import random  # Rastgele sayı üretmek için "random" modülünü içe aktarıyoruz.

hiz = 0.15  # Yılanın hareket hızını belirleyen değişkeni tanımlıyoruz.

# Turtle penceresini oluşturuyoruz ve bazı özellikleri ayarlıyoruz.
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)  # Ekran güncellemesini kapatıyoruz (pencereyi donduruyoruz).

# Yılanın başını temsil eden bir "kafa" Turtle'ı oluşturuyoruz ve başlangıç konumunu belirliyoruz.
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'  # Yılanın başlangıçta hareket etmediğini belirliyoruz.

# Yemi temsil eden bir "yemek" Turtle'ı oluşturuyoruz ve başlangıç konumunu ve görünümünü ayarlıyoruz.
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

# Yılanın kuyruğunu temsil eden bir liste olan "kuyruklar"ı tanımlıyoruz ve başlangıçta boş bir liste olarak başlatıyoruz.
kuyruklar = []

# Oyundaki puanı saklayacak olan "puan" değişkenini başlatıyoruz ve ekranda görünen puanı göstermek için bir "yaz" Turtle'ı oluşturuyoruz.
puan = 0
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

# Yılanın hareketini yönlendiren "move" fonksiyonunu tanımlıyoruz.
def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)

    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)

    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)

    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)

# Yılanın yukarı gitmesini sağlayan "goUp" fonksiyonunu tanımlıyoruz.
def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'

# Yılanın aşağı gitmesini sağlayan "goDown" fonksiyonunu tanımlıyoruz.
def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'

# Yılanın sağa gitmesini sağlayan "goRight" fonksiyonunu tanımlıyoruz.
def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'

# Yılanın sola gitmesini sağlayan "goLeft" fonksiyonunu tanımlıyoruz.
def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

# Klavye olaylarını dinlemek için "pencere.listen()" komutunu kullanıyoruz ve klavye ok tuşlarına basıldığında ilgili yönlendirme fonksiyonlarını çağırıyoruz.
pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')

while True:
    pencere.update()  # Ekran güncellemesini tekrar açıyoruz.

    # Yılanın başı pencerenin sınırlarına ulaştığında veya dışına çıktığında oyunun yeniden başlaması gerektiğini kontrol ediyoruz.
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)  # 1 saniye bekleme süresi ekliyoruz.
        kafa.goto(0, 0)  # Yılanın başını başlangıç noktasına taşıyoruz.
        kafa.direction = 'stop'

        # Kuyruk parçalarını ekrandan uzak bir yere taşıyoruz.
        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []  # Kuyruk listesini sıfırlıyoruz.
        puan = 0  # Puanı sıfırlıyoruz.
        yaz.clear()  # Puanı ekrandan temizliyoruz.
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

        hiz = 0.15  # Yılanın hızını başlangıç hızına geri döndürüyoruz.

    # Yılanın yemi yemesi durumunu kontrol ediyoruz.
    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)  # Yemi yeni bir konuma taşıyoruz.
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        puan = puan + 10  # Puanı artırıyoruz.
        yaz.clear()  # Puanı ekrandan temizliyoruz.
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

        hiz = hiz - 0.001  # Yılanın hızını artırıyoruz.

        yeniKuyruk = turtle.Turtle()  # Yeni bir kuyruk parçası oluşturuyoruz.
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)  # Yeni kuyruk parçasını listeye ekliyoruz.

    # Kuyruk parçalarını güncelliyoruz (birbirini takip etmesi için).
    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x, y)

    # Eğer yılanın kuyruğunda en az bir parça varsa, başın konumunu güncelliyoruz.
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()  # Yılanın hareketini uyguluyoruz.
    time.sleep(hiz)  # Belirlediğimiz hızda bir bekleme süresi ekliyoruz.
