import asyncio, os, edge_tts
async def m():
    c=edge_tts.Communicate("Olá, aqui é o narrador do canal. Hoje a gente vai falar de uma história antiga, contada com calma, do jeito que se conversa na varanda no fim da tarde.","pt-BR-AntonioNeural",proxy=os.environ.get('HTTPS_PROXY'))
    await c.save("ref.mp3")
asyncio.run(m())
