"""Tema do Dublê (antigo "Clone Studio") para o Gradio 6 (conta Pedro, 03/11/2026).

Uso no app.py (no Gradio 6, tema e CSS vão no launch(), não no Blocks):

    from identidade.tema import TEMA, CSS, CABECALHO
    with gr.Blocks(title='Dublê') as app:
        gr.HTML(CABECALHO)
        ...
    app.launch(theme=TEMA, css=CSS, favicon_path='identidade/favicon.svg')

Modo escuro sempre: os valores claros e os "_dark" são os mesmos, então o app fica escuro
mesmo que o navegador esteja no modo claro. Cores e fontes em identidade/IDENTIDADE.md.
"""
import gradio as gr

# Paleta (IDENTIDADE.md, seção 3)
GRAFITE = '#0B0B10'   # fundo, 60%
PAINEL = '#15151C'    # cartões e campos, 30%
PAINEL2 = '#1C1C25'   # hover e campo em foco
LINHA = '#2A2A35'     # bordas
PAPEL = '#F2F1EC'     # texto principal (17,4:1 no grafite)
APAGADO = '#9C9AAB'   # texto de apoio (7,1:1)
ECO = '#8B7CFF'       # destaque, 10%: botão principal, foco, barras de voz (6,0:1)
ECO_CLARO = '#A99DFF' # hover do botão e links
SELO = '#F5C518'      # só para o selo "Liberado" e avisos de consentimento (amarelo da Central)
OK = '#5CC98A'
ERRO = '#F0705C'

_eco = gr.themes.Color(name='eco', c50='#F1EFFF', c100='#E3DFFF', c200='#C9C1FF', c300='#A99DFF',
                       c400='#8B7CFF', c500='#7564F5', c600='#5B4BE0', c700='#4838B8', c800='#352A8A',
                       c900='#231C5C', c950='#15113A')
_grafite = gr.themes.Color(name='grafite', c50='#F2F1EC', c100='#DCDAE3', c200='#BEBCCB', c300='#9C9AAB',
                           c400='#77758A', c500='#55536A', c600='#3A3948', c700='#2A2A35', c800='#1C1C25',
                           c900='#15151C', c950='#0B0B10')

_fonte = [gr.themes.GoogleFont('Manrope'), 'ui-sans-serif', 'system-ui', 'Segoe UI', 'sans-serif']
_mono = [gr.themes.GoogleFont('Geist Mono'), 'ui-monospace', 'Consolas', 'monospace']

_v = dict(
    body_background_fill=GRAFITE, body_text_color=PAPEL, body_text_color_subdued=APAGADO,
    background_fill_primary=GRAFITE, background_fill_secondary=PAINEL,
    border_color_primary=LINHA, border_color_accent=ECO, border_color_accent_subdued=_eco.c800,
    color_accent=ECO, color_accent_soft=_eco.c950,
    link_text_color=ECO_CLARO, link_text_color_hover=_eco.c200, link_text_color_visited=ECO_CLARO,
    block_background_fill=PAINEL, block_border_color=LINHA, block_border_width='1px',
    block_label_background_fill=PAINEL2, block_label_text_color=APAGADO, block_label_border_color=LINHA,
    block_title_text_color=PAPEL, block_info_text_color=APAGADO,
    panel_background_fill=PAINEL, panel_border_color=LINHA,
    input_background_fill=GRAFITE, input_background_fill_focus=PAINEL2, input_border_color=LINHA,
    input_border_color_focus=ECO, input_placeholder_color='#77758A',
    checkbox_background_color=GRAFITE, checkbox_background_color_selected=ECO,
    checkbox_border_color=LINHA, checkbox_border_color_selected=ECO, checkbox_label_text_color=PAPEL,
    slider_color=ECO,
    table_even_background_fill=PAINEL, table_odd_background_fill=GRAFITE, table_border_color=LINHA,
    table_row_focus=PAINEL2,
    button_primary_background_fill=ECO, button_primary_background_fill_hover=ECO_CLARO,
    button_primary_text_color=GRAFITE, button_primary_text_color_hover=GRAFITE,
    button_primary_border_color=ECO, button_primary_border_color_hover=ECO_CLARO,
    button_secondary_background_fill=PAINEL2, button_secondary_background_fill_hover=LINHA,
    button_secondary_text_color=PAPEL, button_secondary_border_color=LINHA,
    button_cancel_background_fill=PAINEL2, button_cancel_text_color=ERRO, button_cancel_border_color=LINHA,
    error_background_fill='#2A1512', error_border_color=ERRO, error_text_color=ERRO,
    shadow_drop='none', shadow_drop_lg='0 8px 30px rgba(0,0,0,.45)', shadow_spread='0 0 0 3px rgba(139,124,255,.25)',
)

TEMA = gr.themes.Base(
    primary_hue=_eco, secondary_hue=_eco, neutral_hue=_grafite,
    radius_size=gr.themes.sizes.radius_lg, spacing_size=gr.themes.sizes.spacing_md,
    text_size=gr.themes.sizes.text_md, font=_fonte, font_mono=_mono,
)
_aceitas = set(__import__('inspect').signature(TEMA.set).parameters)
_tudo = {**_v, **{k + '_dark': v for k, v in _v.items()}}
TEMA.set(**{k: v for k, v in _tudo.items() if k in _aceitas})  # ignora o que esta versão do Gradio não tiver

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@500;600;700&family=Manrope:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');
:root { --dub-grafite:#0B0B10; --dub-painel:#15151C; --dub-linha:#2A2A35; --dub-papel:#F2F1EC;
        --dub-apagado:#9C9AAB; --dub-eco:#8B7CFF; --dub-selo:#F5C518; --dub-ok:#5CC98A; --dub-erro:#F0705C; }
body, gradio-app, .gradio-container { background: var(--dub-grafite) !important; }
.gradio-container { max-width: 1180px !important; margin: 0 auto !important; }
/* títulos em Geist, apertados (Vercel / Linear) */
.gradio-container h1, .gradio-container h2, .gradio-container h3, .dub-titulo {
  font-family: 'Geist', 'Manrope', system-ui, sans-serif !important; letter-spacing: -0.02em; font-weight: 600; }
.gradio-container h1 { font-size: 2rem; }
/* abas: sublinhado Eco na aba ativa (Linear) */
button[role="tab"] { font-weight: 600; color: var(--dub-apagado) !important; }
button[role="tab"][aria-selected="true"] { color: var(--dub-papel) !important; border-color: var(--dub-eco) !important; }
/* botão principal em pílula, um só por tela (ElevenLabs) */
button.primary { border-radius: 999px !important; font-weight: 700 !important; padding-inline: 22px !important; }
button.primary:focus-visible, input:focus-visible, textarea:focus-visible { outline: 2px solid var(--dub-eco); outline-offset: 2px; }
/* cabeçalho */
.dub-topo { display:flex; align-items:center; gap:14px; padding:18px 4px 10px; border-bottom:1px solid var(--dub-linha); margin-bottom:8px; }
.dub-topo svg { height:34px; width:auto; }
.dub-topo .dub-sub { color: var(--dub-apagado); font-size: .9rem; margin-left:auto; }
/* selos de situação da biblioteca */
.dub-selo { display:inline-flex; align-items:center; gap:6px; padding:3px 10px; border-radius:999px;
  font: 600 .78rem/1.4 'Geist Mono', ui-monospace, monospace; letter-spacing:.04em; text-transform:uppercase; }
.dub-selo.liberado { background: rgba(92,201,138,.12); color: var(--dub-ok); }
.dub-selo.bloqueado { background: rgba(240,112,92,.12); color: var(--dub-erro); }
/* faixa de consentimento: amarelo da Central, o único lugar onde ele aparece */
.dub-consentimento { border:1px solid rgba(245,197,24,.35); background: rgba(245,197,24,.07);
  border-left: 3px solid var(--dub-selo); border-radius: 12px; padding: 12px 16px; }
.dub-consentimento strong { color: var(--dub-selo); }
/* barras de voz animadas enquanto gera (eco do símbolo) */
.dub-onda { display:inline-flex; gap:3px; align-items:center; height:18px; }
.dub-onda i { width:4px; border-radius:2px; background: var(--dub-eco); animation: dub-onda 1s ease-in-out infinite; }
.dub-onda i:nth-child(1){height:18px} .dub-onda i:nth-child(2){height:13px; animation-delay:.15s} .dub-onda i:nth-child(3){height:7px; animation-delay:.3s}
@keyframes dub-onda { 50% { transform: scaleY(.45); opacity:.6; } }
@media (prefers-reduced-motion: reduce) { .dub-onda i { animation: none; } }
/* tabela em Manrope (o Gradio usa a mono por padrão) */
.gradio-container .table-wrap, .gradio-container table { --font-mono: 'Manrope', system-ui, sans-serif; }
.gradio-container table, .gradio-container table * { font-family: 'Manrope', system-ui, sans-serif !important; }
footer { opacity: .5; }
"""

# Cabeçalho com o logotipo (SVG em linha, sem fonte externa)
CABECALHO = """
<div class="dub-topo">
<svg viewBox="0 0 330 80" role="img" aria-label="Dublê"><g transform="translate(-2 -4.8) scale(1.4)"><path d="M30 12 A20 20 0 0 0 30 52 Z" fill="#F2F1EC"/><g fill="#8B7CFF"><rect x="33" y="12" width="5" height="40" rx="2.5"/><rect x="41" y="17" width="5" height="30" rx="2.5"/><rect x="49" y="24" width="5" height="16" rx="2.5"/></g></g><g transform="translate(98 0)" fill="none" stroke="#F2F1EC" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><circle cx="20.5" cy="50" r="16"/><path d="M36.5 10 V70"/><path d="M57.5 30 V54 A16 16 0 0 0 89.5 54 M89.5 30 V70"/><path d="M110.5 10 V70"/><circle cx="126.5" cy="50" r="16"/><path d="M163.5 10 V70"/><path d="M184.5 50 H216.5 A16 16 0 1 0 211.8 61.3"/><path d="M191.5 22 L200.5 13 L209.5 22" stroke="#8B7CFF"/></g></svg>
<span class="dub-sub">Voz e rosto, só com autorização · uso interno</span>
</div>
"""

__all__ = ['TEMA', 'CSS', 'CABECALHO']
