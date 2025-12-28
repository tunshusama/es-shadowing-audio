import asyncio
import os
import edge_tts

VOICE = 'es-MX-DaliaNeural'
RATE = '+0%'
VOLUME = '+0%'

LESSON_ID = 'A004'
OUT_DIR = 'A-004_audio'

SENTENCES = [
    ('Trabajo en una empresa internacional.', '我在一家国际公司工作。'),
    ('Mi trabajo es interesante, pero a veces difícil.', '我的工作很有意思，但有时也很难。'),
    ('Cada día aprendo cosas nuevas.', '我每天都会学到新东西。'),
    ('Trabajo con personas de diferentes países.', '我和来自不同国家的人一起工作。'),
    ('A veces hablamos en inglés.', '有时候我们用英语交流。'),
    ('Otras veces hablamos en español.', '有时我们说西班牙语。'),
    ('Quiero mejorar mi español para el trabajo.', '我想为了工作提升我的西语。'),
    ('Por eso practico todos los días.', '所以我每天都练习。'),
    ('Escucho audios cuando tengo tiempo.', '有空的时候我会听音频。'),
    ('También practico hablando solo.', '我也会自己练习说话。'),
    ('No siempre es fácil.', '这并不总是容易的。'),
    ('A veces me equivoco mucho.', '有时候我会犯很多错。'),
    ('Pero creo que es normal.', '但我觉得这很正常。'),
    ('Lo importante es no rendirse.', '重要的是不要放弃。'),
    ('Poco a poco me siento más seguro.', '慢慢地我感觉更自信了。'),
    ('Entiendo mejor a la gente.', '我能更好地理解别人了。'),
    ('Puedo expresarme con más claridad.', '我能更清楚地表达自己。'),
    ('Todavía tengo mucho que aprender.', '我还有很多要学的。'),
    ('Pero voy por buen camino.', '但我走在正确的路上。'),
    ('Seguiré practicando.', '我会继续练习。'),
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
