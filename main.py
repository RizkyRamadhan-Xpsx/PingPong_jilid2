from pygame import *
# --- Kelas umum untuk semua sprite (bola dan paddle) ---
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
            self.rect.y += self.speed
# --- Pengaturan tampilan ---
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong - Tahap 1: Bola diam")

# --- Clock dan FPS ---
clock = time.Clock()
FPS = 60
game = True

# --- Membuat objek ---
left_paddle = Player('paddle.png', 30, 200, 5, 20, 100)
right_paddle = Player('paddle.png', 550, 200, 5, 20, 100)
ball = GameSprite('tenis_ball.png', 275, 225, 0, 50, 50)  # bola diam
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # isi background
    window.fill(back)

    # update posisi paddle
    left_paddle.update_left()
    right_paddle.update_right()

    # tampilkan semua sprite
    left_paddle.reset()
    right_paddle.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)