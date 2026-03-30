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
    .block-container { max-width: 1200px; padding-top: 2rem; }
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        min-height: 150px;
    }
    .project-card h3 { margin-top: 0; font-size: 1.05rem; }
    .project-card p { font-size: 0.88rem; color: #495057; }
    .card-tag {
        display: inline-block;
        background: #e9ecef;
        border-radius: 4px;
        padding: 2px 8px;
        margin: 2px;
        font-size: 0.72rem;
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
These work samples demonstrate how APAC streaming competition, content
investment, and launch trajectory can be analyzed using only public, external data.
</p>
""", unsafe_allow_html=True)

st.markdown("")

# ── Start Here ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="start-box">
<strong>If you have 30 seconds:</strong> Open any project → Executive Summary tab.<br>
<strong>If you have 5 minutes:</strong> Read all three Executive Summaries, then Strategic Implications / JP vs KR tabs.<br>
<strong>Three questions answered:</strong><br>
&nbsp;&nbsp;A — What does APAC streaming competition actually look like beyond SVOD rivalry?<br>
&nbsp;&nbsp;B — How can content investment be discussed when precise internal data isn't available?<br>
&nbsp;&nbsp;C — Which public early signals distinguish front-loaded launches from durable performers?<br>
<strong>Method:</strong> Public market data, transparent assumptions, documented scoring rationale.<br>
<strong>Key caveat:</strong> External data only. All limitations are stated upfront.
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.divider()

# ── Project Cards ────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
<div class="project-card">
<h3>📊 APAC Streaming Competitive Intelligence</h3>
<p>Three-layer competitive framework for Japan & Korea — premium SVOD,
free/ad-supported, and YouTube/UGC attention competition.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
**Question:** What competitive pressures matter most in each market?

- **20 platforms** across three competition layers
- **Sub-signal decomposition** with documented rationale
- Source, date, confidence on every data point
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Korea</span>'
        '<span class="card-tag">Competitive Intelligence</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.link_button("🔗 Dashboard", "https://apac-streaming-c-8peixzfcwmsgthjnafktgn.streamlit.app/", use_container_width=True)
    st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/apac-streaming-ci", use_container_width=True)

with col2:
    st.markdown("""
<div class="project-card">
<h3>🎬 Japan Content Investment Efficiency</h3>
<p>Framework for comparing Japanese content types on viewing efficiency,
export value, and portfolio role using Netflix engagement data.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
**Question:** Which content types generate the most viewing per estimated cost?

- **21 titles** with defined inclusion criteria
- **Sensitivity analysis** across cost scenarios
- Export value **rule-based** on Global Top 10 weeks
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Content Strategy</span>'
        '<span class="card-tag">Investment Framework</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.link_button("🔗 Dashboard", "https://japan-content-efficiency-6hurjz8iuwotjxug83aqb3.streamlit.app/", use_container_width=True)
    st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/japan-content-efficiency", use_container_width=True)

with col3:
    st.markdown("""
<div class="project-card">
<h3>🚀 JP/KR Launch Health Scorecard</h3>
<p>Title-level diagnostics for early signal vs. staying power
in Japan and Korea Netflix scripted series.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
**Question:** Which early signals distinguish front-loaded launches from durable performers?

- **14 titles** (7 JP / 7 KR) with weekly trajectory
- **3 dimensions:** launch strength, staying power, off-platform
- **Rule-based archetypes** from within-market z-scores
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Korea</span>'
        '<span class="card-tag">Launch Diagnostics</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.link_button("🔗 Dashboard", "https://launch-health-scorecard-mn8yu4pnfclrl8eaujdnny.streamlit.app/", use_container_width=True)
    st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/launch-health-scorecard", use_container_width=True)

st.markdown("")
st.divider()

# ── How They Connect ─────────────────────────────────────────────────────────
st.markdown("### How These Projects Fit Together")

st.markdown("""
| | Project A | Project B | Project C |
|---|---|---|---|
| **Question** | What does the competitive environment look like? | How should content investment be discussed? | Which launch signals matter most? |
| **Scope** | JP + KR, 20 platforms | Japan, 21 titles | JP + KR, 14 titles |
| **Method** | Three-layer pressure framework | Viewing efficiency + export value | Launch strength + staying power + off-platform |
| **Key finding** | Free/UGC pressure underweighted in JP; premium rivalry dominates KR | Anime is the most capital-efficient export vehicle | Week-1 alone is misleading; KR launches bigger but decays faster |
| **Limitation** | Semi-quantitative scoring | Category-level cost proxies | 14-title sample, thresholded Top 10 data |
""")

st.info("Together: **market context → investment framework → launch health diagnostics**")

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
