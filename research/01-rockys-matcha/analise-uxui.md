# Análise UX/UI — Rocky's Matcha
> Site: https://www.rockysmatcha.com/  
> Data: 2026-06-18  
> Metodologia: 168 princípios UX/UI research-backed + inspeção visual

---

## Screenshots do Fluxo Completo

````carousel
![Homepage — Hero / Above the fold](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/homepage_hero.png)
<!-- slide -->
![Homepage — Categorias (Matcha, Best Sellers, Accessories)](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/homepage_categories.png)
<!-- slide -->
![Homepage — Footer e Newsletter](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/homepage_footer.png)
<!-- slide -->
![Página da Loja — Product Grid](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/shop_page.png)
<!-- slide -->
![Página de Produto — Ceremonial Blend 20g](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/product_page.png)
<!-- slide -->
![Cart Drawer — Slide-in com cross-sell](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/cart_drawer.png)
<!-- slide -->
![Checkout — Shopify standard com express options](/Users/pedroneto/.gemini/antigravity-ide/brain/dd049e0e-9954-43f5-b63c-84a686c5a5f6/checkout_page.png)
````

---

## 1. Pontuação Geral por Categoria

| Categoria | Nota | Observação |
|-----------|------|------------|
| **Hierarquia Visual** | 8/10 | Design limpo e intencional, mas hero carece de proposta de valor textual |
| **Tipografia** | 6/10 | Helvetica funcional, mas tamanhos muito pequenos (11-13px) prejudicam legibilidade |
| **Paleta de Cores** | 9/10 | Azul royal + branco é sofisticado, consistente e memorável |
| **Navegação** | 7/10 | Simples mas escondida no "MENU" hamburger (desktop deveria ter nav visível) |
| **Product Cards** | 7/10 | Limpos mas sem hover states claros, sem badges, sem Quick Add |
| **Página de Produto** | 8/10 | Reviews, variantes, descrição detalhada — bem estruturada |
| **Cart / Checkout** | 9/10 | Cart drawer com cross-sell, progresso de frete grátis, express checkout |
| **Footer** | 6/10 | Minimalista demais — falta informação e links de conteúdo |
| **Acessibilidade** | 5/10 | Fontes muito pequenas, contraste parcialmente inadequado, área de toque limitada |
| **Performance Visual** | 8/10 | Imagens de alta qualidade, carregamento limpo |
| **Média Geral** | **7.3/10** | |

---

## 2. Análise Detalhada por Área

### 2.1 Homepage — Hero / Above the Fold

**O que funciona bem ✅**
- Fotografia de produto impressionante e profissional (close-up da caixa de sachês)
- Identidade visual coesa — o azul royal (`#192FA4`) domina de forma impactante
- CTA "SHOP ALL" com pill button branco é claramente visível e clicável
- Banner de frete grátis visível no topo
- Logo tipográfico centralizado cria senso de marca premium

**O que precisa melhorar ⚠️**
- **Falta proposta de valor textual** — nenhum headline, subtitle ou copy explicando a marca
- **Novo visitante não sabe o que é Rocky's Matcha** — a imagem mostra uma caixa azul mas não comunica "matcha japonês ceremonial grade"
- **Pop-up "10% OFF"** no canto inferior esquerdo compete com o CTA principal
- **CTA genérico** — "SHOP ALL" não cria urgência nem desejo. Alternativa: "Discover Our Matcha" ou "Start Your Ritual"
- **Sem breadcrumb de navegação** para novas categorias

> [!WARNING]
> **Princípio violado: First Impression / Value Proposition Clarity**  
> Visitantes de primeira vez têm ~3 segundos para entender o que o site oferece. Sem headline textual, a homepage depende 100% de interpretação visual.

---

### 2.2 Navegação & Information Architecture

**O que funciona bem ✅**
- Header sticky com logo centralizado (padrão premium reconhecível)
- Busca acessível no header (SEARCH)
- Conta e carrinho posicionados no padrão esperado (canto direito)

**O que precisa melhorar ⚠️**
- **Menu hamburger no DESKTOP** — em telas grandes, a navegação principal deveria estar visível
- **"MENU" e "SEARCH" como texto** — sem ícones, pode confundir usuários internacionais
- **Sem mega-menu dropdown** — categorias como Matcha, Teaware, Best Sellers ficam escondidas
- **Duplicação de páginas** — `/pages/about-us` e `/pages/about` e `/pages/resources` apontam para conteúdos similares

> [!IMPORTANT]
> **Princípio violado: Visibility of System Status (Nielsen #1)**  
> O menu hamburger no desktop esconde a navegação primária, forçando um clique extra para descobrir categorias. Em e-commerce, isso reduz taxa de exploração.

---

### 2.3 Seção de Categorias (Homepage Mid-section)

**O que funciona bem ✅**
- Grid de 3 colunas com fotografias de alta qualidade (matcha no copo, latas, chasen)
- Labels claros: "MATCHA", "BEST SELLERS", "ACCESSORIES"
- Texto branco sobre imagens com boa legibilidade
- CTA "SHOP ALL" reforçado abaixo das categorias

**O que precisa melhorar ⚠️**
- **Apenas 3 categorias mostradas** — Houjicha, Bundles, Subscriptions, Gift Cards ficam invisíveis
- **Sem hover effects** nas cards de categoria — parecem estáticas
- **Sem contagem de produtos** — "Matcha (12 produtos)" ajudaria a informar
- **Imagens cortadas no topo quando o scroll está no limite** — possível issue de CSS

---

### 2.4 Página da Loja (Shop / Collection)

**O que funciona bem ✅**
- Grid de 4 colunas limpo e organizado
- Produtos com imagem clara do packaging em fundo neutro
- Nome do produto e preço visíveis abaixo de cada card
- "SHOW FILTERS" e "SORT BY" disponíveis
- Segundo image swap no hover (mostra ângulo alternativo do produto)

**O que precisa melhorar ⚠️**
- **Sem badges** — sem "Best Seller", "New", "Sale", "Sold Out" visualmente destacados
- **Sem botão Quick Add** — obriga clique → página de produto → add to cart (3 cliques vs. 1)
- **Sem ratings/reviews nos cards** — a prova social só aparece na página de produto
- **Preço sem contexto** — $36 por 20g vs. $108 por 100g precisa de "$/g" para comparação
- **Nomes de produto muito longos** — "rocky's matcha Ceremonial Blend Matcha 20g" é repetitivo (a marca já está no header)
- **Pop-up "10% OFF" sobrepõe produto cards** no canto inferior esquerdo

> [!TIP]
> **Quick Win: Adicionar Quick Add to Cart**  
> Product cards com botão "ADD" no hover poderiam reduzir 2 cliques do fluxo de compra, especialmente para clientes recorrentes que já sabem o que querem.

---

### 2.5 Página de Produto (PDP)

**O que funciona bem ✅**
- **Rating proeminente**: ⭐ 4.9 com 421 reviews — excelente prova social
- **Variante de tamanho** clara: 20G / 100G com toggle
- **Quantity picker** com +/- ao lado do "ADD TO CART"
- **Descrição detalhada** com cultivars, região de origem (Yame, Japan)
- **Layout 50/50** — imagem à esquerda, informações à direita (padrão reconhecido)
- **Thumbnails** de múltiplos ângulos na parte inferior

**O que precisa melhorar ⚠️**
- **"ADD TO CART" com estilo outline/ghost** — deveria ser o botão mais visualmente dominante da página (filled, azul #192FA4)
- **Sem indicação de estoque** — "Only 5 left" cria urgência
- **Sem informação de frete** na PDP — "Free shipping on $85+" deveria ser repetido aqui
- **Sem seção "You May Also Like"** visível acima do fold
- **Sem vídeo do produto** — para matcha, um video de preparação seria poderoso
- **Subscription option** não aparece na PDP principal — apenas em /collections/subscriptions

> [!CAUTION]
> **Problema Crítico: CTA "ADD TO CART" com baixo contraste**  
> O botão "ADD TO CART" usa estilo outline (borda cinza, fundo branco) — é o botão MAIS importante da página e tem o MENOR peso visual. Deveria ser filled com a cor primária (#192FA4).

---

### 2.6 Cart Drawer (Slide-in Sidebar)

**O que funciona bem ✅**
- **Barra de progresso de frete grátis** — "You're $49.00 away from free shipping!" com progress bar visual azul
- **Cross-sell "Customers also purchased"** — Bamboo Whisk ($20.00) com botão "ADD" direto
- **Thumbnail do produto** com nome e preço claros
- **Quantity controls** (+/-) dentro do cart
- **Route Package Protection** integrado ($1.95) — transparente e confiável
- **"CHECKOUT"** com botão filled azul escuro — grande e proeminente ✅

**O que precisa melhorar ⚠️**
- **"Checkout without Coverage"** como link de texto — pode confundir (opt-out deveria ser mais claro)
- **Sem estimativa de prazo de entrega** no cart
- **Sem campo de cupom** no cart drawer — apenas no checkout

---

### 2.7 Checkout (Shopify Standard)

**O que funciona bem ✅**
- **Express Checkout** com Shop, PayPal e Google Pay — reduz fricção significativamente
- **Order summary** com thumbnails, quantidades e preços claros
- **Campo de cupom** acessível ("Discount code or gift card")
- **Newsletter opt-in** pré-selecionado (controverso mas eficaz)
- **Layout limpo** de 2 colunas (formulário + resumo)
- **Detecção automática de país** (Brazil)

**O que precisa melhorar ⚠️**
- **Route Package Protection** aparece no checkout sem ter sido opt-in explícito no PDP
- **Frete não calculado** até inserir endereço — poderia mostrar estimativa baseada em país
- **Sem trust badges** visíveis (SSL, segurança do pagamento)

---

### 2.8 Footer

**O que funciona bem ✅**
- Newsletter com campo de email e botão "JOIN →" minimalista
- Links institucionais presentes: About, Store Locator, FAQ, Policies
- Redes sociais: Instagram, TikTok, Pinterest, YouTube

**O que precisa melhorar ⚠️**
- **Extremamente minimalista** — falta:
  - Links para categorias de produto (Matcha, Teaware, Bundles)
  - Descrição breve da marca
  - Informação de contato (email/telefone)
  - Trust signals (certificações, reviews agregados)
  - Bandeiras de pagamento aceitas (Visa, MC, Amex)
- **Links muito pequenos** e agrupados horizontalmente — difícil escanear
- **Sem logo da marca** no footer

> [!NOTE]
> **Princípio: Footer como "safety net"**  
> Pesquisas mostram que 60%+ dos usuários scrollam até o footer quando não encontram o que procuram. Um footer informativo reduz bounce rate e aumenta confiança.

---

## 3. Antipatterns Detectados

| # | Antipattern | Severidade | Localização | Descrição |
|---|-------------|-----------|-------------|-----------|
| 1 | **Ghost CTA** | 🔴 Alta | PDP | "ADD TO CART" com estilo outline em vez de filled — menor peso visual que botões secundários |
| 2 | **Hidden Navigation** | 🟠 Média | Header (Desktop) | Menu hamburger no desktop esconde toda a navegação primária |
| 3 | **Missing Value Proposition** | 🔴 Alta | Homepage Hero | Zero texto explicativo — visitante novo não sabe o que a marca vende |
| 4 | **Tiny Touch Targets** | 🟠 Média | Global | Fontes de 11-13px com links e buttons que podem não atingir 44x44px mínimo |
| 5 | **Pop-up Obstruction** | 🟡 Baixa | Global | "10% OFF" badge fixo no canto inferior esquerdo sobrepõe conteúdo |
| 6 | **Forced Opt-in** | 🟡 Baixa | Cart → Checkout | Route Package Protection adicionado automaticamente sem consentimento explícito |
| 7 | **Redundant Brand Naming** | 🟡 Baixa | Product Cards | "rocky's matcha" repetido em cada nome de produto (já está no header) |
| 8 | **Dead-end Footer** | 🟠 Média | Footer | Footer minimalista sem links de produto, contato ou trust signals |

---

## 4. Pontos Fortes da Marca (O que copiar)

| Aspecto | Por que funciona |
|---------|-----------------|
| **Identidade visual coesa** | Azul royal + branco + packaging diferenciado cria reconhecimento instantâneo |
| **Fotografia de produto excepcional** | Close-ups profissionais com iluminação de estúdio — sensação premium |
| **Packaging como diferencial** | Latas azuis com labels coloridos = instagramável e reconhecível |
| **Prova social forte** | 421 reviews a 4.9/5 na PDP — transmite confiança imediata |
| **Cart drawer inteligente** | Cross-sell, progress bar de frete grátis, checkout rápido — otimizado para conversão |
| **Express checkout** | Shop, PayPal, Google Pay — reduz abandono de checkout |
| **Conteúdo educacional** | Matcha Guide, receitas, playlists — construção de comunidade e SEO |
| **Colaborações culturais** | Tom Sachs, Stone Island, Rimowa — posiciona como lifestyle brand, não só chá |

---

## 5. Recomendações Priorizadas

### 🔴 Prioridade Alta (Impacto direto em conversão)

1. **Mudar "ADD TO CART" para botão filled** — background `#192FA4`, texto branco, full-width
2. **Adicionar headline na homepage** — ex: "Ceremonial Grade Matcha, Sourced from Japan" 
3. **Mostrar navegação primária no desktop** — Matcha | Teaware | Best Sellers | About

### 🟠 Prioridade Média (Melhoria de experiência)

4. **Aumentar font sizes globalmente** — body mínimo 14px, headings proporcionais
5. **Quick Add nos product cards** — botão "ADD" no hover do card
6. **Badges nos cards** — "Best Seller", "New", "Sale", "Sold Out"
7. **Expandir footer** — adicionar categorias, contato, trust badges, payment icons
8. **Mostrar reviews nos product cards** — ⭐ 4.9 (421) abaixo do preço

### 🟡 Prioridade Baixa (Polish)

9. **Remover "rocky's matcha" dos nomes de produto** nos cards (já está no header)
10. **Adicionar subscription toggle na PDP** — "Subscribe & Save 15%"
11. **Adicionar vídeo de preparação** na PDP do Ceremonial Blend
12. **Hover animations nos cards de categoria** — scale + overlay opacity

---

## 6. Comparação com Benchmarks do Segmento

| Critério | Rocky's Matcha | Benchmark D2C Premium |
|----------|---------------|----------------------|
| Value proposition na hero | ❌ Ausente | ✅ Headline + subtitle |
| Nav visível no desktop | ❌ Hamburger | ✅ Horizontal nav |
| Quick Add to Cart | ❌ Ausente | ✅ Hover button |
| Reviews nos cards | ❌ Ausente | ✅ Stars + count |
| CTA filled na PDP | ❌ Outline/ghost | ✅ Filled + cor primária |
| Cart com cross-sell | ✅ Presente | ✅ Presente |
| Express checkout | ✅ Shop/PayPal/GPay | ✅ Múltiplas opções |
| Footer informativo | ❌ Minimalista | ✅ Multi-coluna completo |
| Conteúdo educacional | ✅ Guias, receitas | ✅ Blog + vídeo |
| Photography quality | ✅ Excepcional | ✅ Padrão alto |

---

> **Resumo:** Rocky's Matcha acerta na identidade visual, fotografia e estratégia de marca (collabs + conteúdo). Os gaps principais estão em **UX de conversão** — o botão de compra mais importante (ADD TO CART) é o menos visível, a navegação está escondida, e novos visitantes não recebem context textual sobre a marca. Correções de alto impacto são simples de implementar e podem melhorar significativamente as métricas de conversão.
