# Deploy — LP Obras 400 m² (One Office)

## O que vai ao ar

Só a **LP Obras 400 m²**. O site publicado é o conteúdo de `dist/`:

```
dist/
├── index.html          ← a LP (HTML estático, sem dependência de build)
├── favicon.svg
└── fonts/              ← Neue Einstellung (5 pesos, .otf)
```

Tudo o que está fora de `dist/` é material de autoria e não é publicado
(`vercel.json` aponta `outputDirectory: dist`, e o `.vercelignore` corta o resto do upload).

## Estrutura do repositório

| Caminho | Função |
| --- | --- |
| `dist/` | **build publicado** |
| `LP Obras 400m2.dc.html` | fonte editável da LP (template `x-dc`, precisa do `support.js`) |
| `Home OneOffice.dc.html` | fonte da Home — fora do escopo deste deploy |
| `support.js` | runtime de preview dos arquivos `.dc.html` |
| `fonts/` | fontes originais (copiadas para `dist/fonts/`) |
| `_arquivo/home-standalone/` | builds antigos da Home, arquivados |
| `vercel.json` | config do deploy |

## Publicar

### Via CLI

```bash
npm i -g vercel        # uma vez
vercel login
vercel                 # preview
vercel --prod          # produção
```

### Via Git

Conecte o repositório na Vercel. Configuração no dashboard:

- **Framework Preset:** Other
- **Build Command:** vazio (não há build)
- **Output Directory:** `dist` (já vem do `vercel.json`)

Cada push na `main` publica em produção.

## Editar a LP

Duas fontes de verdade convivem hoje:

- `LP Obras 400m2.dc.html` — original, com props (`showRetrofit`, `showFaq`) e loops `sc-for`.
- `dist/index.html` — o mesmo conteúdo já **renderizado** em HTML puro.

O que está no ar é o `dist/index.html`. Para textos, imagens e ajustes de estilo,
edite direto ele. Se alterar o `.dc.html`, é preciso refletir a mudança no
`dist/index.html` (os loops estão expandidos e os handlers viraram um `<script>`
no fim do arquivo).

## Pontos de atenção

- **Mídias externas.** Fotos, logos e vídeos são carregados de
  `lpp.oneoffice.com.br` e `oneoffice.com.br`. Todos os `<img>`/`<video>` usam
  `referrerpolicy="no-referrer"` (e há o header `Referrer-Policy: no-referrer`)
  para contornar a proteção de hotlink do WordPress. Se o time da One Office
  endurecer essa proteção, as mídias precisarão ser copiadas para `dist/assets/`
  e os endereços trocados.
- **Formulário.** Abre uma conversa no WhatsApp `+55 11 96415-0693` com os dados
  preenchidos. O número está no `<script>` ao final do `dist/index.html`
  (procure por `wa.me/`). Não há back-end nem envio de e-mail.
- **Merlin.** O popup do gomerlin.com.br é carregado de CDN externa
  (`scripts.gomerlin.com.br`). Se adicionar CSP, libere esse host.
- **Sem tags de analytics.** GTM / GA4 / Meta Pixel ainda não estão instalados.
