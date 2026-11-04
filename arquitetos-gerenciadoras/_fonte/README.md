# LP Arquitetos e Gerenciadoras (One Office)

Esta LP nasceu da copy `Copy_LP_Arquitetos_Gerenciadoras_One_Office.docx` (Google Ads) e foi montada sobre a base da LP Obras Corporativas: mesmo `<head>`, com fontes embutidas, GTM-TQ9MJK33 e o Merlin popup `0f964186…`.

## Como editar

- `body.html` é o corpo da página e `scripts.html` são os comportamentos.
- `montar.py` gera o `../index.html`. Rode da raiz do repo:

```bash
python3 arquitetos-gerenciadoras/_fonte/montar.py
```

- Preview: configuração `oneoffice-lp-arquitetos` (porta 6421) no `.claude/launch.json`. Abra em `/arquitetos-gerenciadoras/`.

## Decisões

- **CTA:** é o Merlin, como nas outras LPs. O formulário com anexo de plantas da copy não entrou.
- **Rolagem:** é nativa. Saíram o Lenis e o easing por JS da LP base, e não há seção com pin.
- **Clientes:** faixas cruzadas de logos em loop, com botão de pausa, no estilo da Cardoso.
- **Imagens:** as fotos das obras estão em `img/`, vindas da apresentação comercial, com caminho root-relative (`/arquitetos-gerenciadoras/img/…`).
- **Texto aprovado pelo usuário em 04/11/2026:** os itens [CONFIRMAR] da copy saíram e o texto ficou como afirmado. As lacunas sem valor foram preenchidas com o que já está publicado nas LPs da One Office:
  - porte mínimo de 400 m², o "porte mínimo das obras corporativas" da LP atual;
  - proposta em 5 a 7 dias úteis, o prazo que a LP atual promete.
- **Lista de obras:** são as da apresentação (Asper, Criteria, NSTech e Ciari Moreira), sem região.
- **Depoimento:** o espaço saiu, porque não há depoimento real.

## Publicação

O passo `Deploy — Arquitetos e Gerenciadoras` do `.github/workflows/deploy-hostinger.yml` publica a pasta por FTP em `lpp.oneoffice.com.br/arquitetos-gerenciadoras/` a cada merge na main que mexa nela. A pasta `_fonte/` fica de fora do upload. Mudanças entram por branch + PR, nunca direto na main.
