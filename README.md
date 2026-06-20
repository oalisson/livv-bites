# LIVV BITES

Premium frozen Brazilian cheese bread — *Comfort food, thoughtfully made.*

🔗 **Site (homepage de validação):** https://oalisson.github.io/livv-bites/

## Estrutura
- `index.html` — homepage publicada (gerada, arquivo único com imagens embutidas)
- `site/` — seções-fonte (`*-section.html`) + `build_homepage.py` (gera a homepage)
- `brand/` — brand guide, brand kit, design tokens
- `research/` — análises competitivas (Rocky's Matcha, Erewhon)
- `docs/` — status do projeto
- `LIVV-BITES-KNOWLEDGE-BASE.md` — contexto completo do projeto

## Como editar e publicar
```bash
# 1. edite as seções em site/*-section.html
# 2. gere a homepage (atualiza index.html da raiz e de site/)
python3 site/build_homepage.py
# 3. publique
git add -A && git commit -m "ajuste" && git push
# o GitHub Pages atualiza o site sozinho em ~1 min
```

## Ambiente na nuvem (Codespace)
No GitHub: botão **Code → Codespaces → Create codespace on main**.
Abre um VS Code no navegador com o projeto pronto; o site sobe na porta 8000.
