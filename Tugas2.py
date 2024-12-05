# Tugas 2 Intern Bengawan UV Aero
# Nama    : Muhammad Daffa Rahman
# NIM     : L0124062
# Prodi   : Informatika
# Program : Implementasi OOP dan Menggunakan OpenCV

import cv2
from datetime import datetime

class Camera:
    cam = None
    ret = False
    frame = None
    __textpos = 30

    def setup(self):
        self.cam = cv2.VideoCapture(0)

    def capture(self):
        self.ret, self.frame = self.cam.read()
    
    def show(self, title = "Camera"):
        self.__textpos = 30
        cv2.imshow(title, self.frame)

    def save(self, filename):
        cv2.imwrite(filename, self.frame)

    def wait(self, key):
        return not cv2.waitKey(1) & 0xFF == ord(key)
    
    def release(self):
        self.cam.release()
    
    def close(self):
        cv2.destroyAllWindows()
    
    def addText(self, text):
        self.frame = cv2.putText(
            self.frame, text,
            (20, self.__textpos),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (255, 0, 0), 1,
            cv2.LINE_AA)
        self.__textpos += 30


class Ayah:
    def __init__(self, nama, hobi):
        self.nama = nama
        self.hobi = hobi

    def __str__(self):
        return f"{self.__class__.__name__} yang bernama {self.nama}"

    def lakukanHobi(self):
        print(f"{self} sedang melakukan hobinya yaitu {self.hobi}")

    def makan(self, makanan):
        print(f"{self} sedang makan {makanan}")

    def melihat(self):
        cam = Camera()
        cam.setup()
        while cam.wait('q'):
            cam.capture()
            cam.addText(f"{self} sedang melihat")
            cam.show(str(self))
        
        cam.release()
        cam.close()


class Ibu(Ayah):
    def memasak(self, makanan):
        print(f"{self} sedang memasak {makanan}")


class Anak(Ayah):
    def fotoin(self):
        cam = Camera()
        cam.setup()

        while cam.wait('c'):
            cam.capture()
            cam.addText(f"{self} lagi ngefotoin")
            cam.addText("Tekan 'c' untuk mengambil gambar")
            cam.show(f"Kamera milik {self}")
        
        cam.close()

        cam.capture()
        while cam.wait('q'):
            cam.show(f"Hasil foto dari {self}")

        cam.save(f"{self.__class__.__name__}-{self.nama.replace(' ','')}-{str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')}.jpg")
        cam.release()
        cam.close()


if __name__ == "__main__":
    ayah = Ayah("Tom Cruise", "Rock Climbing")
    ibu = Ibu("Ritsuki", "Memasak")
    anak = Anak("Daffa", "Ngoding")

    ayah.lakukanHobi()
    ayah.makan("Nasi Goreng")
    ayah.melihat()

    ibu.lakukanHobi()
    ibu.memasak("Soto Ayam")
    ibu.melihat()

    anak.lakukanHobi()
    anak.makan("Nasi Padang")
    anak.fotoin()
