# Tudo ao mesmo tempo agora: Python Assíncrono

Luciano Ramalho - twitter: @ramalhoorg - github: ramalho

Python 3.4 incorporou um loop de eventos e a biblioteca *AsyncIO*. No 3.5 ganhamos 4 construções sintáticas novas: **await**, **async def**, **async for** e **async with**, junto com vários métodos especiais para suportar essas construções, como **__anext__** e **__aenter__**. E agora temos o pacote *uvloop*, que traz para o Python o alto desempenho da biblioteca *libuv* -- o motor assíncrono do Node.js. Estamos mais preparados do que nunca para resolver problemas envolvendo alta concorrência de I/O. Vejam o que diz a engenharia de infra-estrutura do Facebook:

> We are increasingly relying on AsyncIO, which was introduced in Python 3.4,
> and seeing huge performance gains as we move codebases away from Python 2.
> (Estamos contando cada vez mais com AsyncIO, que foi lançado no Python 3.4, 
> e observando grandes ganhos de desempenho à medida que convertemos nosso 
> legado de Python 2).

Vamos falar sobre isso, e -- com sorte -- até ouvir depoimentos dos presentes sobre usos de AsyncIO!

## Fontes

- Slides: [Speaker Deck](https://speakerdeck.com/ramalho/python-assincrono-pybr2016)
- Código: [Github](https://github.com/ramalho/tudo-agora/tree/master/countries)
