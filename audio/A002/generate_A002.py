import asyncio
import os
import edge_tts

VOICE = 'es-MX-DaliaNeural'
RATE = '+0%'
VOLUME = '+0%'

LESSON_ID = 'A002'
OUT_DIR = 'A-002_audio'

SENTENCES = [
    ('Me levanto a las siete de la mañana.', '我早上七点起床。'),
    ('Desayuno en casa todos los días.', '我每天在家吃早饭。'),
    ('Tomo café y como pan.', '我喝咖啡，吃面包。'),
    ('Después voy al trabajo.', '然后我去上班。'),
    ('Trabajo de lunes a viernes.', '我周一到周五上班。'),
    ('Mi trabajo está cerca de mi casa.', '我的工作离家很近。'),
    ('Voy al trabajo en metro.', '我坐地铁去上班。'),
    ('Trabajo con muchas personas.', '我和很多人一起工作。'),
    ('Mis compañeros son muy amables.', '我的同事很友好。'),
    ('Al mediodía comemos juntos.', '中午我们一起吃饭。'),
    ('Por la tarde trabajo un poco más.', '下午我再工作一会儿。'),
    ('Salgo del trabajo a las seis.', '我六点下班。'),
    ('Por la noche vuelvo a casa.', '晚上我回家。'),
    ('Ceno con mi familia.', '我和家人一起吃晚饭。'),
    ('Después descanso un poco.', '然后我休息一会儿。'),
    ('A veces veo la televisión.', '有时候我看电视。'),
    ('Otras veces leo un libro.', '有时我看书。'),
    ('Me acuesto a las once.', '我十一点睡觉。'),
    ('Duermo bien por la noche.', '我晚上睡得很好。'),
    ('Mañana es otro día.', '明天又是新的一天。'),
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
