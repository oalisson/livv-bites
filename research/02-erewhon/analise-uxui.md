# Análise UX/UI — Erewhon (Ship Nationwide)
> Site: https://ship.erewhon.com/  
> Data: 2026-06-19  
> Metodologia: 168 princípios UX/UI research-backed + inspeção via Firecrawl scraper

---

## 1. Pontuação Geral por Categoria

| Categoria | Nota | Observação |
|-----------|------|------------|
| **Hierarquia Visual** | 9/10 | Layout editorial premium, hierarquia clara com hero impactante e headline forte |
| **Tipografia** | 7/10 | Sharp Sans é premium, mas body 12px e H2 13px são muito pequenos |
| **Paleta de Cores** | 7/10 | Preto + branco é sofisticado mas genérico — pouca diferenciação cromática |
| **Navegação** | 9/10 | Nav horizontal visível no desktop com dropdown completo — padrão ideal |
| **Product Cards** | 8/10 | Grid limpo com "Sold Out" badge, swatches de variantes, mas sem Quick Add |
| **Página de Produto** | 9/10 | Subscription toggle, Affirm BNPL, cross-sell, FAQ integrado, descrição tabs |
| **Cart / Checkout** | 8/10 | Cart drawer com "Pair with" cross-sell, subtotal claro, mas sem progress bar de frete |
| **Footer** | 7/10 | Newsletter + contato + links, mas poderia ter mais categorias e trust signals |
| **Acessibilidade** | 5/10 | Fontes pequenas (12px body), UserWay widget como band-aid em vez de a11y nativa |
| **Performance Visual** | 9/10 | Fotografia lifestyle de altíssimo nível, imagens profissionais em todas as seções |
| **Média Geral** | **7.8/10** | |

---

## 2. Análise Detalhada por Área

### 2.1 Homepage — Hero / Above the Fold

**O que funciona bem ✅**
- **Vídeo/animação do Smoothie Kit** como hero — visualmente impactante e em movimento
- **Headline textual poderosa:** "YOUR FAVORITE SMOOTHIE, DELIVERED NATIONWIDE" — comunica valor + proposta imediatamente
- **CTA claro:** "SHOP SMOOTHIE KIT" — ação específica, não genérica
- **Header com navegação horizontal visível** — Shop (dropdown), About, Account, Cart, Search
- **Logo branco sobre fundo preto** — alto contraste, premium
- **Sem pop-ups invasivos** na primeira visita

**O que precisa melhorar ⚠️**
- **Sem announcement bar** — oportunidade perdida para frete grátis ($75+) ou promoção
- **Hero é 100% focado no Smoothie Kit** — novos visitantes podem não saber que vendem grocery, wellness, accessories
- **CTA único** — "SHOP SMOOTHIE KIT" serve apenas 1 categoria; falta "SHOP ALL" ou segunda opção
- **Scroll necessário** para entender a amplitude do catálogo

> [!NOTE]
> **Princípio: Value Proposition Above the Fold**  
> Diferente do Rocky's Matcha que não tem headline nenhum, o Erewhon comunica valor imediato. Porém, foca exclusivamente no smoothie kit, deixando 90% do catálogo invisível no primeiro contato.

---

### 2.2 Navegação & Information Architecture

**O que funciona bem ✅**
- **Nav horizontal visível no desktop** — Shop, About, Account, Search, Cart
- **Dropdown de categorias completo:** Accessories, Best Sellers, Beverages, Gift Sets, Grocery, Home & Body, New Arrivals, Smoothie, Wellness
- **9 categorias claras** no dropdown — organização intuitiva
- **Sub-menu About** com Our Story, FAQs, Locations, Manage Subscription
- **Search bar** integrada ao header com campo de busca
- **Account e Cart** posicionados no padrão e-commerce (direita)

**O que precisa melhorar ⚠️**
- **Dropdown simples (lista)** — sem imagens de categoria no mega-menu (padrão em grocery premium)
- **"New Arrivals"** não indica quantos itens ou datas — poderia mostrar badge "NEW" mais contexto
- **Nenhuma indicação de quantos produtos** por categoria no menu
- **Falta "All Products"** — usuário que quer browsear tudo precisa clicar em cada categoria

> [!TIP]
> **Benchmark: Mega-menu com imagens**  
> Sites como Thrive Market e Whole Foods mostram imagens de categoria no dropdown. Isso aumenta a taxa de clique em categorias secundárias em até 25%.

---

### 2.3 Seção "Curated by Erewhon" (Homepage Mid-section)

**O que funciona bem ✅**
- **Grid horizontal scrollável** com 20+ produtos — muito mais conteúdo que Rocky's Matcha
- **Headline "CURATED BY EREWHON"** — posiciona como curadoria, não catálogo genérico
- **"VIEW COLLECTION"** como CTA secundário
- **Preços visíveis** em cada card abaixo do nome
- **"Sold Out"** badge visível em produtos esgotados (ex: Shopper Bag Eggshell)
- **"From $X"** para produtos com variantes de preço — informativo

**O que precisa melhorar ⚠️**
- **Sem botão Quick Add** — precisa clicar no produto → PDP → Add to Cart
- **Sem ratings/reviews** nos cards — a prova social está completamente ausente em todo o site
- **Scroll horizontal sem indicação de quantos itens** — falta paginação ou "1 de 20"
- **Sem hover effects** visíveis — cards parecem estáticos (sem animação de zoom ou overlay)

---

### 2.4 Categorias Visuais (Carousel Lifestyle)

**O que funciona bem ✅**
- **Fotografias lifestyle de altíssima qualidade** — fridge com produtos, lifestyle outdoors, velas premium
- **5 categorias com imagem:** Grocery, Wellness, Home & Body, Accessories, Gifts
- **Labels claros** em bold sobre cada imagem
- **Carousel com navegação** (Previous/Next)
- **Estilo editorial/magazine** — cada foto parece campanha de revista

**O que precisa melhorar ⚠️**
- **Carousel pode esconder categorias** — Gifts provavelmente não é visível sem scroll/swipe
- **Sem contagem de produtos** — "Grocery (45 products)" ajudaria
- **Sem hover animation** — imagens estáticas

---

### 2.5 Seção de Accessories (Homepage Bottom)

**O que funciona bem ✅**
- **Grid de produtos extenso** com 18+ itens de accessories
- **Variantes de cor visíveis** via color swatches (ex: bottles com 6 cores, cups com 4 cores)
- **"See All" e contagem de cores** ("6 colors") — excelente UX de variantes
- **Preço visível** em cada card
- **Mix de categorias** — hats, bags, bottles, hoodies, cups

**O que precisa melhorar ⚠️**
- **Desproporcionalmente grande** — accessories domina a homepage mais que grocery ou wellness
- **"Sold Out" sem alternativa** — poderia ter "Notify me" ou "Similar items"
- **Sem filtragem** dentro da seção — por tipo (hats, bags, bottles) ou por preço

---

### 2.6 Página de Produto (PDP) — Strawberry Glaze Smoothie Kit

**O que funciona bem ✅**
- **Layout 50/50 limpo** — galeria à esquerda, informações à direita
- **3 imagens** com thumbnails e carousel — produto, conteúdo do kit, ingredientes
- **Subscription toggle integrado:** "One-time purchase $100.00" vs "Subscribe & save 10% $90.00" — excelente conversão
- **Affirm Buy Now Pay Later** — "Pay in 4 interest-free installments of $25.00"
- **Tabs de conteúdo:** Description, Ingredients, Care Instructions — organização limpa
- **Cross-sell inline** — "Recommended:" com 3 produtos e botão "Add" direto
- **FAQ integrado** na PDP com accordion — reduz dúvidas sem sair da página
- **"About Us" seção** com 3 cards (Our Story, Our Standards, Our Commitment) — constrói confiança
- **Shipping info contextual** — "Ships 6/22 - 6/24 in order of purchase"
- **"Recommended" + "Recently Viewed"** tabs no final da PDP
- **Quantity selector** com dropdown (1-10+)
- **Add to Cart com preço** visível no botão ("Add to cart $100.00")

**O que precisa melhorar ⚠️**
- **Zero reviews/ratings** — nenhuma prova social em todo o site (ponto fraco grave)
- **Sem vídeo do produto** — para um smoothie kit de $100, um vídeo de preparação seria esperado
- **Botão "Add to cart"** não usa cor de destaque — parece usar estilo mais neutro
- **Sem badge de urgência** — "Ships 6/22-6/24" é informativo mas não urgente ("Only X left" seria mais eficaz)
- **Subscription obriga 3 meses mínimo** — pode assustar novos clientes (deveria estar mais claro)
- **Preço regular riscado ($90) vs one-time ($100)** — a hierarquia visual da economia de 10% poderia ser mais clara
- **Nenhum selo ou certificação** visível na PDP (B-Corp, Certified Organic poderia estar aqui)

> [!CAUTION]
> **Problema Crítico: Ausência total de reviews/ratings**  
> O Rocky's Matcha tem ⭐ 4.9 com 421 reviews proeminente na PDP. O Erewhon — um site que vende Smoothie Kits de $100 — não tem NENHUMA review em todo o site. Para um produto de alto valor, reviews são o fator #1 de conversão após preço.

---

### 2.7 Cart Drawer (Sidebar Slide-in)

**O que funciona bem ✅**
- **Cart drawer sem refresh** — experiência fluida
- **"Pair with" cross-sell** — sugere produtos complementares dentro do cart
- **Order notes** — campo "Leave a note about your order" disponível
- **Subtotal claro** com link para checkout
- **"Check Out"** como botão proeminente
- **Info de shipping/taxes** — "Shipping, taxes, and discount codes are calculated at checkout"

**O que precisa melhorar ⚠️**
- **Sem barra de progresso de frete grátis** — Rocky's Matcha mostra "You're $49 away from free shipping!" com progress bar visual. Erewhon não mostra nada
- **Sem thumbnails** visíveis dos produtos no cart (baseado no scrape)
- **Sem quantity controls** (+/-) visíveis no cart drawer
- **"Check Out" parece usar estilo padrão** — poderia ser mais visualmente dominante

> [!IMPORTANT]
> **Quick Win: Barra de progresso de frete grátis**  
> Com threshold de $75 para frete grátis, uma barra de progresso visual no cart drawer poderia aumentar AOV significativamente. Este é um padrão já implementado pelo Rocky's Matcha com sucesso.

---

### 2.8 Footer

**O que funciona bem ✅**
- **Logo preto** no footer — reforço de marca
- **Newsletter** com campo de email e botão "Join" — clean e funcional
- **hCaptcha** integrado — segurança contra spam
- **Contato segmentado** — "Order Related: ship@erewhon.com" e "General: customerservice@erewhon.com"
- **Currency selector** com bandeiras — suporte internacional

**O que precisa melhorar ⚠️**
- **Faltam links de categorias** — Grocery, Wellness, Accessories não estão no footer
- **Sem trust signals** — nenhum selo B-Corp, Certified Organic, ou ícones de pagamento
- **Sem redes sociais** no footer — Instagram, TikTok ausentes (estranho para uma marca de lifestyle)
- **Footer relativamente curto** para um marketplace — poderia ter 3-4 colunas

---

## 3. Antipatterns Detectados

| # | Antipattern | Severidade | Localização | Descrição |
|---|-------------|-----------|-------------|-----------|
| 1 | **Zero Social Proof** | 🔴 Alta | Global (PDP, cards) | Nenhuma review, rating ou depoimento em todo o site — gravíssimo para produtos de $100 |
| 2 | **Hero Tunnel Vision** | 🟠 Média | Homepage Hero | Hero 100% focado no Smoothie Kit — visitantes podem não descobrir as 8+ categorias restantes |
| 3 | **Missing Free Shipping Progress** | 🟠 Média | Cart Drawer | Sem barra de progresso para frete grátis ($75+) — oportunidade de AOV perdida |
| 4 | **Tiny Typography** | 🟠 Média | Global | Body 12px e H2 13px — abaixo do mínimo recomendado de 14-16px |
| 5 | **No Quick Add** | 🟡 Baixa | Product Cards | Obriga 3 cliques (card → PDP → add) em vez de 1 clique no hover |
| 6 | **Subscription Lock-in** | 🟡 Baixa | PDP (Smoothie Kit) | Mínimo de 3 meses para subscription — pode assustar novos clientes |
| 7 | **No Announcement Bar** | 🟡 Baixa | Header | Sem banner de frete grátis ou promoção no topo — padrão esperado em e-commerce |
| 8 | **Missing Social Links in Footer** | 🟡 Baixa | Footer | Sem links de Instagram/TikTok no footer — estranho para marca lifestyle LA |

---

## 4. Pontos Fortes da Marca (O que copiar)

| Aspecto | Por que funciona |
|---------|-----------------|
| **Navegação horizontal visível** | Dropdown com 9 categorias claras no desktop — sem hamburger menu |
| **Hero com headline + CTA** | "YOUR FAVORITE SMOOTHIE, DELIVERED NATIONWIDE" comunica valor imediatamente |
| **Subscription toggle na PDP** | "One-time vs Subscribe & save 10%" integrado ao botão de compra |
| **Buy Now Pay Later (Affirm)** | "4 installments of $25.00" reduz barreira de preço para itens de $100 |
| **Cross-sell contextual** | "Recommended" com botão "Add" direto na PDP e "Pair with" no cart |
| **FAQ integrada na PDP** | Accordion com respostas — reduz abandono e suporte |
| **Color swatches nos cards** | Variantes visíveis sem clicar no produto (bottles, cups) |
| **Sold Out handling** | Badge claro em produtos esgotados em vez de esconder |
| **Fotografia lifestyle editorial** | Estilo de revista (magazine-quality) — cada foto parece campanha |
| **Curadoria editorial** | "CURATED BY EREWHON" posiciona como curador, não catálogo genérico |
| **Shipping date na PDP** | "Ships 6/22 - 6/24" dá expectativa clara de entrega |
| **About us na PDP** | 3 cards (Story, Standards, Commitment) constroem confiança direto na página de compra |

---

## 5. Recomendações Priorizadas

### 🔴 Prioridade Alta (Impacto direto em conversão)

1. **Implementar sistema de reviews/ratings** — Yotpo, Judge.me ou Stamped.io para prova social
2. **Adicionar barra de progresso de frete grátis** no cart drawer ("$X away from free shipping!")
3. **Diversificar o hero** — adicionar segundo slide ou banner mostrando Grocery/Wellness/Accessories

### 🟠 Prioridade Média (Melhoria de experiência)

4. **Aumentar font sizes globalmente** — body mínimo 14px, H2 proporcional
5. **Adicionar announcement bar** no topo — "Free shipping on non-perishable orders $75+"
6. **Quick Add nos product cards** — botão "ADD" no hover do card
7. **Mega-menu com imagens** — foto de cada categoria no dropdown para aumentar exploração
8. **Adicionar redes sociais** ao footer — Instagram, TikTok, YouTube

### 🟡 Prioridade Baixa (Polish)

9. **Hover animations nos cards** — zoom sutil na imagem + aparição do botão Add
10. **Vídeo de preparação** do Smoothie Kit na PDP — reduce return rate para perecíveis
11. **Trust badges** no footer — B-Corp, Certified Organic, ícones de pagamento (Visa, MC, Amex, Affirm)
12. **"Notify me" para Sold Out** — em vez de dead-end, capturar email para restock

---

## 6. Comparação com Rocky's Matcha

| Critério | Erewhon | Rocky's Matcha |
|----------|---------|----------------|
| Value proposition na hero | ✅ Headline forte | ❌ Ausente |
| Nav visível no desktop | ✅ Horizontal nav + dropdown | ❌ Hamburger menu |
| Quick Add to Cart | ❌ Ausente | ❌ Ausente |
| Reviews nos cards | ❌ Ausente em todo o site | ❌ Ausente nos cards, ✅ na PDP |
| CTA filled na PDP | ⚠️ Parcial | ❌ Ghost/outline |
| Cart com cross-sell | ✅ "Pair with" | ✅ Cross-sell + progress bar |
| Progress bar frete grátis | ❌ Ausente | ✅ Presente |
| Express checkout | ⚠️ Via Affirm BNPL | ✅ Shop/PayPal/GPay |
| Subscription na PDP | ✅ Toggle integrado | ❌ Separado em /collections |
| Footer informativo | ⚠️ Contato bom, falta categorias | ❌ Minimalista demais |
| Conteúdo educacional | ⚠️ About/FAQ na PDP | ✅ Guias, receitas, playlists |
| Photography quality | ✅ Editorial/lifestyle excepcional | ✅ Produto/packaging excepcional |
| Color swatches | ✅ Presente nos cards | ❌ Ausente |
| BNPL | ✅ Affirm 4x | ❌ Não mencionado |
| Sold Out handling | ✅ Badge claro | ⚠️ Parcial |

---

## 7. Comparação de Notas

| Categoria | Erewhon | Rocky's Matcha | Vantagem |
|-----------|---------|----------------|----------|
| Hierarquia Visual | 9/10 | 8/10 | 🏆 Erewhon |
| Tipografia | 7/10 | 6/10 | 🏆 Erewhon |
| Paleta de Cores | 7/10 | 9/10 | 🏆 Rocky's |
| Navegação | 9/10 | 7/10 | 🏆 Erewhon |
| Product Cards | 8/10 | 7/10 | 🏆 Erewhon |
| Página de Produto | 9/10 | 8/10 | 🏆 Erewhon |
| Cart / Checkout | 8/10 | 9/10 | 🏆 Rocky's |
| Footer | 7/10 | 6/10 | 🏆 Erewhon |
| Acessibilidade | 5/10 | 5/10 | Empate |
| Performance Visual | 9/10 | 8/10 | 🏆 Erewhon |
| **Média Geral** | **7.8/10** | **7.3/10** | 🏆 Erewhon |

---

> **Resumo:** O Erewhon supera o Rocky's Matcha em navegação, hierarquia visual e funcionalidades de PDP (subscription, BNPL, cross-sell contextual, FAQ). Porém, **a ausência total de reviews é uma falha gravíssima** para um marketplace que vende itens de $100. O Rocky's Matcha ganha em identidade cromática (azul royal memorável) e otimização de cart (progress bar de frete grátis). Ambos compartilham problemas de acessibilidade (fontes pequenas) e falta de Quick Add nos cards. Para a **Livv Bites**, o ideal seria combinar: a **navegação e PDP do Erewhon** com a **identidade visual forte e cart otimizado do Rocky's Matcha**, adicionando reviews e Quick Add que ambos negligenciam.
