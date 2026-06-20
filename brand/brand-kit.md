# LIVV BITES — Brand Kit (Design System)

> **Status:** 🟡 PLACEHOLDER — proposta inicial aguardando aprovação do fundador
> **Última atualização:** 2026-06-19
> **Base conceitual:** [brand-guide.md](brand-guide.md) · **Referência visual:** Packaging Example (Premium Bone Broth Collection) · Paleta: Forest Green + Warm Cream + Soft Beige + Natural Wood + Soft Gold

Este documento traduz a direção visual **conceitual** do brand guide em valores **concretos e utilizáveis** (hex codes, fontes, escalas). Tudo aqui é uma proposta fundamentada — não uma decisão final. Cada item marcado com 🟡 precisa de confirmação do fundador antes de virar verdade definitiva no site e no packaging.

---

## 🟡 O que ainda depende do fundador

| Item | Status | Bloqueia |
|------|--------|----------|
| Hex codes finais | 🟡 Proposto (alinhado ao packaging) | Design tokens, site, packaging |
| Tipografia final | 🟡 Proposto (Cormorant Garamond + Inter) | CSS, design system |
| Logo / logotipo | ✅ **Feito** — SVG vetorial (wordmark + trigo) em `brand/assets/logo/`, integrado ao header + favicon | — |
| Fatos de produto (ver §0.1) | ✅ Oficial — incorporado ao brand-guide | — |

> Enquanto não houver aprovação, **tratar todos os valores deste arquivo como provisórios.** O site pode ser construído sobre eles e re-tematizado com um único ponto de troca (`design-tokens.json`).

---

## 0. Referência: Packaging Example

O fundador forneceu um mockup de packaging ("Premium Bone Broth Collection") que ancora a direção visual abaixo.

### 0.1 ✅ Fatos de produto extraídos do packaging — OFICIAL

Confirmados pelo fundador e incorporados ao [brand-guide.md](brand-guide.md) (Key Messages + Product Facts):

- **"Made with Bone Broth"** — diferencial de produto em destaque na frente
- **Ingredientes:** tapioca starch, grass-fed cheddar & parmesan, organic bone broth, organic olive oil, organic eggs, salt
- **Contém:** leite, ovos
- **"Woman-Owned"** — atributo de marca (selo)
- Descritor **"GOURMET"** sob o wordmark
- **Specs:** 12 peças · Net Wt 13 oz (370g) · 159 cal/serving (2 peças/50g) · 5g proteína
- **Instagram:** @livv.bites
- **Headline alternativa:** "Real food. Real ingredients. Made to fuel your life."
- **Selos usados:** Gluten Free · Clean Ingredients · No Artificial Preservatives · Made in Small Batches · Woman-Owned

### 0.2 Logo / wordmark (referência)

- **Wordmark:** `LIVV BITES` em serif clássico, caixa alta, tracking amplo
- **Descritor:** `GOURMET` abaixo, menor, mais espaçado
- **Ornamento:** raminho de trigo dourado (`Soft Gold`) acima do wordmark
- **Cor:** Forest Green sobre cream; versão clara (cream) sobre fundo verde
- ✅ **Vetorizado:** `brand/assets/logo/livv-bites-logo.svg` (primary), `-logo-light.svg` (fundo escuro), `-mark.svg` (selo/favicon). Trigo desenhado como vetor; wordmark em Cormorant Garamond.
- ⬜ **Falta (opcional):** OG image dedicada; versão do wordmark em paths (outline) para uso fora da web/print

---

## 1. Cores

### 1.1 Paleta principal (proposta 🟡)

> Valores alinhados ao **Packaging Example** fornecido pelo fundador (deep forest + cream quente + ornamentos gold).

| Token | Hex | Conceito | Uso |
|-------|-----|----------|-----|
| **Forest Green** | `#22402F` | Primária | Botões primários, headers, links, logo, barras |
| Forest Green (dark) | `#16291E` | Primária escura | Hover, estados ativos |
| Forest Green (deep) | `#122019` | Quase-preto verde | Texto de alto contraste, footer |
| **Warm Cream** | `#F4EEE0` | Fundo | Background principal do site (cream quente do packaging) |
| **Soft Beige** | `#EFE6D2` | Secundária | Cards, label cards, seções alternadas, inputs |
| Beige (deep) | `#E2D6BC` | Secundária forte | Bordas suaves, divisores, badges neutros |
| **Natural Wood** | `#A9794F` | Accent quente | Detalhes, ícones, ilustração, hover de accent |
| **Soft Gold** | `#BFA063` | Accent premium | Ornamentos (trigo), filetes, selos, "premium" cues |

### 1.2 Escala do verde (tonal)

Para sombras, estados e profundidade sem sair da paleta.

| Step | Hex | Uso típico |
|------|-----|-----------|
| green-900 | `#122019` | Texto máximo contraste / footer |
| green-800 | `#173124` | Barra inferior / faixas escuras |
| green-700 | `#1D3A2B` | Hover de botão primário |
| **green-600** | `#22402F` | **Primária (default)** |
| green-500 | `#36513F` | Bordas ativas |
| green-400 | `#577061` | Ícones secundários |
| green-300 | `#88A091` | Disabled / placeholder text sobre cream |
| green-200 | `#BDCEC4` | Backgrounds sutis |
| green-100 | `#E3EAE4` | Highlight muito suave |

### 1.3 Texto e neutros

| Token | Hex | Uso |
|-------|-----|-----|
| text-primary | `#22302A` | Corpo de texto (verde-carvão, mais quente que preto puro) |
| text-muted | `#6E6657` | Texto secundário, legendas, metadados |
| text-on-dark | `#F4EEE0` | Texto sobre fundos verde/escuro |
| border | `#DBD0BB` | Bordas e divisores padrão |
| surface | `#FFFFFF` | Cards que precisam saltar do cream |

### 1.4 Cores semânticas (on-brand)

Mantidas dentro do universo natural — sem vermelhos/verdes "de sistema" gritantes (o brand guide pede evitar harsh colors).

| Token | Hex | Uso |
|-------|-----|-----|
| success | `#3D7A53` | Confirmações, "in stock", free-shipping atingido |
| warning | `#C6A961` | Avisos suaves (reusa o gold) |
| error | `#9B3B33` | Erros, sold out (tijolo terroso, não vermelho puro) |

### 1.5 Acessibilidade (contraste)

- `text-primary #22302A` sobre `Warm Cream #F4EEE0` → contraste ~10:1 ✅ (AAA)
- `text-on-dark #F4EEE0` sobre `Forest Green #22402F` → ~9:1 ✅ (AAA texto normal)
- ⚠️ `Soft Gold #BFA063` e `Natural Wood #A9794F` **não** têm contraste suficiente para texto pequeno sobre cream — usar só em detalhes, ícones grandes ou sobre fundo escuro.

---

## 2. Tipografia

### 2.1 Famílias (proposta 🟡)

| Papel | Fonte | Fonte | Por quê |
|-------|-------|-------|---------|
| **Display / Headings** | **Cormorant Garamond** | Serif | Serif clássico de alto contraste — combina com o wordmark delicado e os títulos do packaging. Elegante, premium. Google Fonts (grátis). |
| **Body / UI** | **Inter** | Sans | Altíssima legibilidade em telas, neutra e moderna. Contrasta bem com o serif. Google Fonts (grátis). |

> **Match com o packaging:** o logo "LIVV BITES" e o título "Brazilian Cheese Bread" usam um serif clássico e delicado — Cormorant Garamond é o equivalente livre mais próximo. (Fraunces, mais encorpado/caloroso, fica como alternativa se quiser mais peso.)
>
> **Alternativas se o fundador quiser revisar:**
> - Serif display: *EB Garamond*, *Playfair Display*, *Fraunces* (grátis) · *Canela*, *Ogg* (pagas)
> - Sans body: *Hanken Grotesk*, *Figtree*, *Work Sans* (grátis, um pouco mais quentes que Inter)

```html
<!-- Google Fonts (placeholder) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

### 2.2 Escala tipográfica

> **Regra herdada da pesquisa:** corpo **mínimo 16px**. Rocky's (11px) e Erewhon (12px) erraram nisso — é uma das poucas falhas que ambos os benchmarks compartilham.

| Token | Tamanho | Line-height | Peso | Fonte | Uso |
|-------|---------|-------------|------|-------|-----|
| display | 56px | 1.05 | 500 | Fraunces | Hero headline |
| h1 | 40px | 1.1 | 500 | Fraunces | Título de página |
| h2 | 30px | 1.15 | 500 | Fraunces | Seção |
| h3 | 22px | 1.25 | 600 | Fraunces | Subseção / card title |
| body-lg | 18px | 1.6 | 400 | Inter | Parágrafo de destaque |
| **body** | **16px** | **1.6** | 400 | Inter | **Texto padrão** |
| small | 14px | 1.5 | 400 | Inter | Legendas, metadados |
| label | 13px | 1.4 | 600 | Inter | Labels, uppercase tracking |

- Tracking sugerido para labels/uppercase: `+0.06em`
- Mobile: reduzir `display` → 36px, `h1` → 30px, `h2` → 24px (clamp recomendado no CSS).

---

## 3. Forma e espaçamento

| Token | Valor | Nota |
|-------|-------|------|
| base unit | 4px | Grid de espaçamento (4/8/12/16/24/32/48/64) |
| radius-sm | 6px | Inputs, badges |
| radius-md | 12px | Cards, botões |
| radius-lg | 20px | Cart drawer, modais |
| radius-pill | 999px | Botões pill (CTA principal) |
| shadow-sm | `0 1px 2px rgba(22,39,30,0.06)` | Cards em repouso |
| shadow-md | `0 6px 20px rgba(22,39,30,0.10)` | Hover, drawer |

> Direção: cantos suaves (não retos como Erewhon, nem totalmente pill em tudo). Premium acolhedor.

---

## 4. Componentes-chave (defaults)

Corrigindo as falhas apontadas na pesquisa de ambos os benchmarks (CTA ghost/baixo contraste).

| Componente | Spec |
|-----------|------|
| **Button primary** | bg `Forest Green #22402F` · texto `Cream #F4EEE0` · radius-pill · hover `#16291E` · **filled, alto contraste** (nunca ghost) |
| Button secondary | bg transparente · borda `#22402F` · texto `#22402F` · radius-pill |
| Add to cart | = button primary, sempre o elemento mais visível da PDP |
| Input | bg `surface #FFFFFF` · borda `#DBD0BB` · radius-sm · foco borda `#22402F` |
| Card | bg `#FFFFFF` ou `Soft Beige` · radius-md · shadow-sm · hover shadow-md |
| Badge "Best Seller" | bg `Soft Gold #BFA063` · texto `green-900` |
| Badge "Sold Out" | bg `Beige deep #E2D6BC` · texto `text-muted` |
| Free-shipping bar | track `#E2D6BC` · preenchimento `success #3D7A53` |

---

## 5. Pendências / próximos passos

1. 🟡 **Fundador aprova/ajusta** hex codes e par tipográfico acima.
2. ⬜ Definir **logo** (assim que existir: gerar favicon, OG image, versões mono).
3. ⬜ Aplicar tokens aprovados no `site/` (CSS variables a partir de `design-tokens.json`).
4. ⬜ Estender para packaging.

> Ponto único de troca: ao mudar qualquer valor, editar **`design-tokens.json`** — o site deve consumir os tokens de lá, não hardcoded.
