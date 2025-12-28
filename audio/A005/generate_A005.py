import asyncio
import os
import edge_tts

VOICE = 'es-MX-DaliaNeural'
RATE = '+0%'
VOLUME = '+0%'

LESSON_ID = 'A005'
OUT_DIR = 'A-005_audio'

SENTENCES = [
    ('Vivo en una ciudad bastante grande.', '我住在一座比较大的城市。'),
    ('Aquí hay muchas tiendas y restaurantes.', '这里有很多商店和餐馆。'),
    ('La ciudad es cómoda para vivir.', '这座城市生活起来很方便。'),
    ('El transporte público funciona bien.', '公共交通运行得很好。'),
    ('Normalmente uso el metro o el autobús.', '我通常坐地铁或公交车。'),
    ('No tengo coche.', '我没有车。'),
    ('Para mí no es un problema.', '对我来说这不是问题。'),
    ('Todo está relativamente cerca.', '一切都比较近。'),
    ('Los fines de semana salgo a caminar.', '周末我会出去走走。'),
    ('Me gusta descubrir lugares nuevos.', '我喜欢发现新地方。'),
    ('A veces voy a parques.', '有时候我去公园。'),
    ('Otras veces voy a museos.', '有时我去博物馆。'),
    ('La ciudad puede ser ruidosa.', '城市有时会很吵。'),
    ('Especialmente por la noche.', '尤其是晚上。'),
    ('Pero ya estoy acostumbrado.', '但我已经习惯了。'),
    ('Cada lugar tiene sus ventajas.', '每个地方都有优点。'),
    ('Y también sus desventajas.', '也有缺点。'),
    ('Lo importante es sentirse bien.', '重要的是感觉舒服。'),
    ('Por ahora me gusta vivir aquí.', '目前我喜欢住在这里。'),
    ('Veremos qué pasa en el futuro.', '以后再看会怎样。'),
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
