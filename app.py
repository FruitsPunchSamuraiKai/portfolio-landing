"""
Xinran Li — APAC Content Analytics Portfolio
"""

import streamlit as st

st.set_page_config(
    page_title="Xinran Li — APAC Content Analytics Portfolio",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
    .block-container { max-width: 1100px; padding-top: 2rem; }
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        min-height: 150px;
    }
    .project-card h3 { margin-top: 0; font-size: 1.1rem; }
    .project-card p { font-size: 0.9rem; color: #495057; }
    .card-tag {
        display: inline-block;
        background: #e9ecef;
        border-radius: 4px;
        padding: 2px 8px;
        margin: 2px;
        font-size: 0.75rem;
        color: #495057;
    }
    .hero-subtitle { font-size: 1.05rem; color: #495057; line-height: 1.7; }
    .start-box { background: #f0f4ff; border-radius: 10px; padding: 1.2rem; border: 1px solid #d0daf0; }
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("# Xinran Li")
st.markdown("##### APAC Content Analytics — Public-Data Work Samples")

st.markdown("""
<p class="hero-subtitle">
Strategy and analytics professional with experience at Apple and Accenture.
These work samples demonstrate how APAC streaming competition and content
investment can be analyzed using only public, external data — and where
internal data would improve the analysis.
</p>
""", unsafe_allow_html=True)

st.markdown("")

# ── Start Here ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="start-box">
<strong>If you have 30 seconds:</strong> Open Project A → Executive Summary tab.<br>
<strong>If you have 5 minutes:</strong> Read both Executive Summaries, then the Strategic Implications tabs.<br>
<strong>What these projects answer:</strong><br>
&nbsp;&nbsp;A — What does APAC streaming competition actually look like beyond SVOD rivalry?<br>
&nbsp;&nbsp;B — How can content investment be discussed when precise internal data isn't available?<br>
<strong>Method:</strong> Public market data, transparent assumptions, documented scoring rationale.<br>
<strong>Key caveat:</strong> External data only. All limitations are stated upfront.
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.divider()

# ── Project Cards ────────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
<div class="project-card">
<h3>📊 APAC Streaming Competitive Intelligence</h3>
<p>Three-layer competitive framework for Japan & Korea comparing premium SVOD,
free/ad-supported streaming, and YouTube/UGC attention competition.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
**Business question:** What competitive pressures matter most in each market,
and where do global streaming frameworks underweight APAC-specific dynamics?

- Mapped **20 platforms** across three competition layers in two markets
- Scored competitive pressure on three dimensions with **sub-signal decomposition** and documented rationale
- Every data point tagged with **source, date, and confidence tier**
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Korea</span>'
        '<span class="card-tag">Competitive Intelligence</span>'
        '<span class="card-tag">Market Structure</span>',
        unsafe_allow_html=True)

    st.markdown("")
    c1a, c1b = st.columns(2)
    with c1a:
        st.link_button("🔗 Live Dashboard", "https://apac-streaming-c-8peixzfcwmsgthjnafktgn.streamlit.app/", use_container_width=True)
    with c1b:
        st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/apac-streaming-ci", use_container_width=True)

with col2:
    st.markdown("""
<div class="project-card">
<h3>🎬 Japan Content Investment Efficiency</h3>
<p>Framework for comparing Japanese content types on viewing efficiency,
export value, and portfolio role using Netflix public engagement data.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
**Business question:** Which Japanese content types generate the most
viewing per estimated cost, and which travel beyond Japan?

- Analyzed **21 Japanese titles** with defined inclusion criteria (Japan-produced, Japanese-language)
- Designed **three metrics** (Viewing Efficiency, Export Value, Portfolio Role) with **sensitivity analysis**
- Export value scored **rule-based** on Global Top 10 weeks, not manual judgment
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Content Strategy</span>'
        '<span class="card-tag">Investment Framework</span>'
        '<span class="card-tag">Netflix Data</span>',
        unsafe_allow_html=True)

    st.markdown("")
    c2a, c2b = st.columns(2)
    with c2a:
        st.link_button("🔗 Live Dashboard", "https://japan-content-efficiency-6hurjz8iuwotjxug83aqb3.streamlit.app/", use_container_width=True)
    with c2b:
        st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/japan-content-efficiency", use_container_width=True)

st.markdown("")
st.divider()

# ── How They Connect ─────────────────────────────────────────────────────────
st.markdown("### How These Projects Fit Together")

st.markdown("""
| | Project A | Project B |
|---|---|---|
| **Question** | What does the competitive environment look like? | How should content investment be discussed? |
| **Scope** | Japan + Korea, 20 platforms | Japan, 21 titles across 4 content types |
| **Method** | Three-layer pressure framework with sub-signals | Viewing efficiency + export value + portfolio role |
| **Key finding** | Free/UGC pressure is underweighted in Japan; premium rivalry dominates Korea | Anime is the most capital-efficient export vehicle; drama is a local anchor |
| **Limitation** | Semi-quantitative scoring on public data | Category-level cost proxies, not title-level budgets |
""")

st.info("Together: **competitive landscape → content investment framework → strategic implications**")

st.divider()

# ── Links ────────────────────────────────────────────────────────────────────
st.markdown("### Links")

lk1, lk2, lk3 = st.columns(3)
with lk1:
    st.markdown("**GitHub**")
    st.markdown("[github.com/FruitsPunchSamuraiKai](https://github.com/FruitsPunchSamuraiKai)")
with lk2:
    st.markdown("**LinkedIn**")
    st.markdown("[linkedin.com/in/xinran-li](https://www.linkedin.com/in/xinran-li-090306205/)")
with lk3:
    st.markdown("**Contact**")
    st.markdown("li1000v2@gmail.com")

st.markdown("")
st.caption(
    "All projects use public, external data only. Assumptions and limitations are documented. "
    "These are analytical frameworks for strategy discussion, not production forecasting systems."
)
