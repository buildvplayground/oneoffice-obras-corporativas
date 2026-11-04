"""Monta arquitetos-gerenciadoras/index.html a partir das fontes desta pasta.

Uso (na raiz do repo):  python3 arquitetos-gerenciadoras/_fonte/montar.py

O <head> vem da LP Obras Corporativas (obras-corporativas/index.html): fontes Neue Einstellung
embutidas, GTM-TQ9MJK33, estilos de base e o Merlin (popup 0f964186…). Aqui só troco título
e descrição. O corpo vem de body.html e os scripts de scripts.html.
Edite as fontes e rode de novo; não edite o index.html à mão.
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
base = (RAIZ / 'obras-corporativas' / 'index.html').read_text(encoding='utf-8')
head = base[:base.index('<body')]

TITULO = 'Execução de obras corporativas para arquitetos e gerenciadoras | One Office'
DESC = ('A One Office executa obras corporativas de escritórios de arquitetura e gerenciadoras em São Paulo: '
        'obra civil, instalações e mobiliário de linha própria num só contrato, com o projeto compatibilizado em BIM.')
head = re.sub(r'<title>[^<]*</title>', f'<title>{TITULO}</title>', head, count=1)
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', head, count=1)

body = (AQUI / 'body.html').read_text(encoding='utf-8')
scripts = (AQUI / 'scripts.html').read_text(encoding='utf-8')
html = head + body.replace('<!--SCRIPTS-->', scripts)
(AQUI.parent / 'index.html').write_text(html, encoding='utf-8')
print('ok', AQUI.parent / 'index.html', f'{len(html) / 1024:.0f} KB')
