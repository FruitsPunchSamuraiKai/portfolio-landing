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
    .block-container { max-width: 1200px; padding-top: 2rem; }
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        min-height: 160px;
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
    .placeholder-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        border: 2px dashed #dee2e6;
        min-height: 160px;
    }
    .placeholder-card h3 { margin-top: 0; font-size: 1.1rem; color: #adb5bd; }
    .placeholder-card p { font-size: 0.9rem; color: #adb5bd; }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("# Selected Work Samples")
st.markdown("##### Strategy & Analytics — APAC Content Markets")

st.markdown(
    "These work samples explore core content analytics questions: "
    "how APAC market structure shapes streaming competition, how content "
    "investment can be discussed under incomplete data, and how analytical "
    "frameworks bridge global assumptions with local market realities."
)

st.markdown("")

# ── Project Cards ────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
<div class="project-card">
<h3>📊 APAC Streaming Competitive Intelligence</h3>
<p>Three-layer competitive framework for Japan & Korea — premium SVOD, free/ad-supported streaming, and YouTube/UGC attention competition.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
- Mapped **20 platforms** across three competition layers
- Scored competitive pressure with **documented rationale**
- Surfaced APAC dynamics global frameworks underweight
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Korea</span>'
        '<span class="card-tag">Competitive Intelligence</span>'
        '<span class="card-tag">Market Structure</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.link_button("🔗 Live Dashboard", "https://apac-streaming-c-8peixzfcwmsgthjnafktgn.streamlit.app/", use_container_width=True)
    st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/apac-streaming-ci", use_container_width=True)

with col2:
    st.markdown("""
<div class="project-card">
<h3>🎬 Japan Content Investment Efficiency</h3>
<p>Framework for discussing content investment using public engagement data, transparent cost proxies, and metrics for efficiency, export value, and portfolio role.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
- Analyzed **27 Japanese titles** across anime, drama, film, reality
- Designed **three content metrics** with transparent assumptions
- Produced strategic implications for investment discussion
""")

    st.markdown(
        '<span class="card-tag">Japan</span>'
        '<span class="card-tag">Content Strategy</span>'
        '<span class="card-tag">Investment Framework</span>'
        '<span class="card-tag">Netflix Data</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.link_button("🔗 Live Dashboard", "https://japan-content-efficiency-6hurjz8iuwotjxug83aqb3.streamlit.app/", use_container_width=True)
    st.link_button("📦 GitHub", "https://github.com/FruitsPunchSamuraiKai/japan-content-efficiency", use_container_width=True)

with col3:
    st.markdown("""
<div class="placeholder-card">
<h3>🔧 Project C — Coming Soon</h3>
<p>A third analytical work sample is in development. Check back for updates.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<span style="color: #adb5bd;">

- TBD
- TBD
- TBD

</span>
""", unsafe_allow_html=True)

    st.markdown(
        '<span class="card-tag" style="opacity:0.4;">TBD</span>',
        unsafe_allow_html=True)

    st.markdown("")
    st.button("🔗 Coming Soon", disabled=True, use_container_width=True)
    st.button("📦 Coming Soon ", disabled=True, use_container_width=True)

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
