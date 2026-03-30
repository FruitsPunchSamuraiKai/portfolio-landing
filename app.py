"""
Selected Work Samples — APAC Content Analytics
"""

import streamlit as st

st.set_page_config(
    page_title="Xinran Li — Selected Work Samples",
    page_icon="📊",
    layout="wide",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .block-container { max-width: 1100px; padding-top: 2rem; }
    div[data-testid="stHorizontalBlock"] > div { padding: 0 0.5rem; }
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.8rem;
        height: 100%;
        border: 1px solid #e9ecef;
    }
    .project-card h3 { margin-top: 0; }
    .card-tag {
        display: inline-block;
        background: #e9ecef;
        border-radius: 4px;
        padding: 2px 8px;
        margin: 2px;
        font-size: 0.8rem;
        color: #495057;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("# Selected Work Samples")
st.markdown("##### Strategy & Analytics — APAC Content Markets")

st.markdown(
    "These work samples explore core content analytics questions: "
    "how APAC market structure shapes streaming competition, and how content "
    "investment can be discussed systematically under incomplete external data."
)

st.markdown("")

# ── Project Cards ────────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
<div class="project-card">
<h3>📊 APAC Streaming Competitive Intelligence</h3>
<p>Three-layer competitive framework for Japan & Korea — premium SVOD, free/ad-supported streaming, and YouTube/UGC attention competition.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
- Mapped **20 platforms** across three competition layers
- Scored competitive pressure with **documented rationale**
- Surfaced APAC dynamics that global frameworks underweight
""")

    st.markdown('<span class="card-tag">Japan</span>'
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
<p>Framework for discussing content investment using public engagement data, transparent cost proxies, and metrics for viewing efficiency, export value, and portfolio role.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
- Analyzed **27 Japanese titles** across anime, drama, film, reality
- Designed **three content metrics** with transparent assumptions
- Produced strategic implications for investment discussion
""")

    st.markdown('<span class="card-tag">Japan</span>'
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

c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
**Project A** → *What does the competitive environment look like?*

Maps the streaming landscape — not just paid rivals, but free ecosystems
and UGC attention competition that global frameworks often miss.
""")
with c_right:
    st.markdown("""
**Project B** → *How should content investment be discussed?*

Provides a structured way to compare content types on efficiency, export
value, and strategic role for slate planning.
""")

st.info("Together: **competitive landscape → investment framework → strategic implications**")

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
    "All projects use public, external data only with documented assumptions. "
    "These are analytical frameworks designed for strategy discussion."
)
