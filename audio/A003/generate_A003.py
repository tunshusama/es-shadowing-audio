import asyncio
import os
import edge_tts

VOICE = 'es-MX-DaliaNeural'
RATE = '+0%'
VOLUME = '+0%'

LESSON_ID = 'A003'
OUT_DIR = 'A-003_audio'

SENTENCES = [
    ('Hoy tengo muchas cosas que hacer.', '今天我有很多事情要做。'),
    ('Por la mañana fui al supermercado.', '早上我去了超市。'),
    ('Compré comida para la semana.', '我买了一周的食物。'),
    ('El supermercado estaba muy lleno.', '超市里人很多。'),
    ('Después volví a casa.', '然后我回家了。'),
    ('Cociné algo sencillo para comer.', '我做了点简单的饭。'),
    ('Por la tarde quedé con un amigo.', '下午我和一个朋友约好了。'),
    ('Nos vimos en una cafetería.', '我们在一家咖啡馆见面。'),
    ('Hablamos de trabajo y de la vida.', '我们聊了工作和生活。'),
    ('Mi amigo vive en otra ciudad.', '我的朋友住在另一个城市。'),
    ('Vino aquí por unos días.', '他来这里待几天。'),
    ('Le gusta mucho esta ciudad.', '他很喜欢这座城市。'),
    ('Caminamos por el centro.', '我们在市中心散步。'),
    ('Tomamos muchas fotos.', '我们拍了很多照片。'),
    ('Había mucha gente en la calle.', '街上有很多人。'),
    ('Por la noche cenamos fuera.', '晚上我们在外面吃饭。'),
    ('El restaurante era pequeño pero bonito.', '餐厅很小，但很漂亮。'),
    ('La comida estaba muy rica.', '食物很好吃。'),
    ('Volví a casa un poco cansado.', '我回家时有点累。'),
    ('Pero fue un buen día.', '但这是美好的一天。'),
]

async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for i, (es, zh) in enumerate(SENTENCES, start=1):
        filename = f"{LESSON_ID}_{i:02d}.mp3"
        out_path = os.path.join(OUT_DIR, filename)
        communicate = edge_tts.Communicate(
            text=es,
            voice=VOICE,
            rate=RATE,
            volume=VOLUME
        )
        await communicate.save(out_path)
        print(f"[OK] {filename} | {es} -> {zh}")
    print(f"\nDone. Audio files saved to: {os.path.abspath(OUT_DIR)}")

if __name__ == "__main__":
    asyncio.run(main())
