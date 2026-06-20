# 💳 Stripe — Como ativar o pagamento (passo a passo)

> O site é **estático** (GitHub Pages). Usamos **Stripe Payment Links**: um link de
> checkout hospedado pelo Stripe por produto. Sem servidor, sem mensalidade — só
> taxa por venda (~2.9% + $0.30 nos EUA). A estrutura já está pronta; falta só
> criar a conta, os produtos e colar os links.

## Pré-requisitos (do fundador)
- **Conta Stripe** ativada para receber nos EUA. Stripe US normalmente exige uma
  **empresa + conta bancária americana** (ex: LLC). Se a fundadora não tiver,
  alternativas: abrir LLC (Stripe Atlas faz isso), usar um parceiro/EOR, ou um
  gateway que aceite a situação dela. **Confirmar isso antes.**
- Decidir **preços e SKUs** (hoje estão como placeholder).

## Passo 1 — Criar a conta
1. https://dashboard.stripe.com/register
2. Completar o cadastro do negócio (dados da empresa + banco) e ativar a conta.
3. Em **Settings → Tax**, ativar o **Stripe Tax** (calcula imposto de venda dos EUA automaticamente).

## Passo 2 — Cadastrar os produtos
1. **Products → Add product**.
2. Nome (ex: `Brazilian Cheese Bread — Traditional`), foto, descrição.
3. Preço (ex: `$14.00`, one-time). Para assinatura, criar também um preço **recurring**.
4. Repetir para cada SKU (ex: o bundle "The Comfort Box").

## Passo 3 — Criar os Payment Links
1. **Payment Links → New**.
2. Selecionar o produto/preço.
3. Em opções, ativar:
   - **Collect shipping address** (endereço de entrega)
   - **Allow promotion codes** (cupons), se quiser
   - **Adjustable quantity** (cliente escolhe quantidade)
   - **Shipping rates** — criar taxas de frete (e a regra de **frete grátis acima de $59**)
4. Copiar a URL gerada (ex: `https://buy.stripe.com/xxxxxxxx`).

## Passo 4 — Colar os links no site
No arquivo [`site/shop-section.html`](../site/shop-section.html), trocar os placeholders:

| Placeholder | Onde |
|-------------|------|
| `REPLACE_WITH_STRIPE_PAYMENT_LINK_TRADITIONAL` | botão "Buy now" do produto Traditional |
| `REPLACE_WITH_STRIPE_PAYMENT_LINK_BUNDLE` | botão "Buy now" do The Comfort Box |

Também atualizar **preços** (`$14.00` / `$36.00`) e remover as tags `placeholder`.

## Passo 5 — Publicar
```bash
python3 site/build_homepage.py     # regenera o index.html
git add -A && git commit -m "Conecta Stripe (payment links + preços)"
git push
```
O site atualiza sozinho em ~1 min. **Pronto — vendendo.**

---

## Notas
- **Assinatura ("Subscribe & save"):** dá pra fazer com um Payment Link de preço
  *recurring*. O texto já está no card como "em breve"; é só criar o link recorrente.
- **Carrinho com vários itens numa compra só:** Payment Links são por produto. Se
  quiser um carrinho unificado (vários produtos num checkout), aí precisa de uma
  função serverless criando *Checkout Sessions* — é o próximo nível, posso montar
  quando quiser (ex: Cloudflare Workers / Vercel, ainda barato).
- **Teste:** o Stripe tem **modo de teste** (cartão `4242 4242 4242 4242`) pra
  validar o fluxo antes de ir ao vivo.
- **Webhooks/recibos:** o Stripe já manda recibo por e-mail automaticamente.
