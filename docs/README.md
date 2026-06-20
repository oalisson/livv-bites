# Livv Bites — Estrutura do Projeto

## Organização de Pastas

```
Livv Bites/
│
├── brand/                    ← Identidade da marca
│   ├── brand-guide.md        ← Brand guide completo (missão, valores, voz, visual)
│   ├── brand-kit.md          ← Design system (cores hex, tipografia, componentes, logo)
│   ├── design-tokens.json    ← Design tokens estruturados (ponto único de tema)
│   └── assets/               ← Logo, ícones, favicons, OG images
│       ├── logo/
│       ├── icons/
│       └── social/
│
├── research/                 ← Análises competitivas (renomeado de analise-sites)
│   ├── 01-rockys-matcha/     ← Análise Rocky's Matcha
│   │   ├── analise-completa.md
│   │   ├── analise-uxui.md
│   │   ├── branding.json
│   │   ├── produtos.json
│   │   └── sitemap.json
│   └── 02-erewhon/           ← Análise Erewhon
│       ├── analise-completa.md
│       ├── analise-uxui.md
│       ├── branding.json
│       ├── produtos.json
│       └── sitemap.json
│
├── site/                     ← Website/E-commerce (em construção)
│   ├── ingredients-section.html  ← Seção "What's inside matters" (Editorial Spread) ✅
│   └── assets/
│       ├── ingredients/      ← Fotos da seção de ingredientes
│       └── lifestyle/        ← Packaging + lifestyle shots (hero/PDP)
│
└── docs/                     ← Documentação do projeto
    ├── README.md             ← Este arquivo
    └── decisoes.md           ← Log de decisões de design/tech
```

## 🧠 Knowledge Base (Context para IA)

> **Para qualquer nova sessão de IA, comece lendo:**  
> [`LIVV-BITES-KNOWLEDGE-BASE.md`](../LIVV-BITES-KNOWLEDGE-BASE.md)  
> Contém TODO o contexto consolidado: marca, pesquisa, decisões, status e próximos passos.

## Status do Projeto

| Fase | Status | Descrição |
|------|--------|-----------| 
| Research & Benchmarking | ✅ Completo | Análises de Rocky's Matcha e Erewhon |
| Brand Guide | ✅ Completo | Missão, valores, voz, posicionamento + product facts (packaging) |
| Knowledge Base | ✅ Completo | Contexto consolidado para handoff de IA |
| Brand Kit (cores, fontes) | 🟡 Proposto | Hex/tipografia alinhados ao packaging — aguardando aprovação formal |
| Design Tokens | 🟡 Proposto | `design-tokens.json` (placeholder, alinhado ao packaging) |
| Logo | 🔴 Recriar | Packaging é mockup gerado, sem vetor/SVG original |
| Website — seção Ingredientes | ✅ Completo | Editorial Spread com fotografia real |
| Website — demais seções (hero, PDP…) | ⬜ Pendente | Próximo passo |

## Onde paramos (sessão 2026-06-20)

**Feito:**
- Brand kit (`brand/brand-kit.md` + `design-tokens.json`) alinhado ao packaging — placeholder aguardando aprovação formal
- Homepage construída por seções (sistema visual: Cormorant Garamond + Inter, forest green/cream/gold):
  Hero (Opção 1 = balcão + chip "Bake in minutes"), How it works, What's inside (Editorial Spread), Our Story, Reviews, Footer
- **`site/index.html`** = homepage única navegável (1 arquivo, imagens em base64, nav fixa + scroll suave). Gerada por `site/build_homepage.py` (re-rodar após editar qualquer seção)
- Fotos reais aplicadas (`site/assets/`)

**Próximo (retomar por aqui):**
1. **Publicar URL** via Netlify Drop (arrastar `site/dist/livv-homepage/`) — OU subir túnel temporário `npx localtunnel`
2. **Logo SVG real** (o do packaging é mockup sem vetor) — item pendente do Fabio ("pode finalizar")
3. Pendências do fundador: nome/assinatura + foto da fundadora (TODO no Our Story), hex/fontes aprovação formal, catálogo (SKUs/preços) → destrava "Shop the collection"

## Referências

- [**Knowledge Base**](../LIVV-BITES-KNOWLEDGE-BASE.md) ← **Leia primeiro**
- [Brand Guide](../brand/brand-guide.md)
- [Rocky's Matcha — Análise Completa](../research/01-rockys-matcha/analise-completa.md)
- [Rocky's Matcha — Análise UX/UI](../research/01-rockys-matcha/analise-uxui.md)
- [Erewhon — Análise Completa](../research/02-erewhon/analise-completa.md)
- [Erewhon — Análise UX/UI](../research/02-erewhon/analise-uxui.md)
