from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# アプリケーションの初期化
app = Ursina()

# --- ウィンドウ設定 ---
window.title = 'MinePati - Minecraft Clone'
window.fps_counter.enabled = True
window.exit_button.visible = False
window.color = color.azure

# --- ブロックテクスチャの設定 ---
# Ursina標準のテクスチャを使用
textures = {
    '1': 'grass',
    '2': 'dirt',
    '3': 'stone',
    '4': 'brick'
}
current_texture = 'grass'

# --- ボクセル（ブロック）クラス ---
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.lime,
            scale=1
        )

    def input(self, key):
        if self.hovered:
            # 右クリックでブロック設置
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=current_texture)
            
            # 左クリックでブロック削除
            if key == 'left mouse down':
                destroy(self)

# --- ワールドの初期生成 ---
# 16x16の床を作成
for z in range(16):
    for x in range(16):
        Voxel(position=(x, 0, z), texture='grass')

# --- プレイヤー設定 ---
player = FirstPersonController()

# --- アップデート処理（ブロック切り替えなど） ---
def update():
    global current_texture
    if held_keys['1']: current_texture = textures['1']
    if held_keys['2']: current_texture = textures['2']
    if held_keys['3']: current_texture = textures['3']
    if held_keys['4']: current_texture = textures['4']
    
    # ESCでゲーム終了
    if held_keys['escape']:
        quit()

# アプリの実行
app.run()
