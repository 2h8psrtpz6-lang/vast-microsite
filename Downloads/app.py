import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="VAST + Mistral · AI Data Infrastructure",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0f;
    color: #e8e8f0;
}
.main { background-color: #0a0a0f; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
header { display: none !important; }
footer { display: none !important; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #2a2a3f; border-radius: 3px; }

.nav-bar {
    position: sticky; top: 0; z-index: 999;
    background: rgba(10,10,15,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid #1e1e2e;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 48px; height: 64px;
}
.nav-logos { display: flex; align-items: center; gap: 12px; }
.nav-brand {
    font-size: 18px; font-weight: 800; letter-spacing: -0.5px;
    background: linear-gradient(90deg, #ffffff, #a78bfa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.nav-divider { color: #3a3a5a; font-size: 20px; }
.nav-partner { font-size: 15px; font-weight: 600; color: #f97316; }
.nav-links { display: flex; gap: 32px; }
.nav-links a {
    color: #9090b0; text-decoration: none; font-size: 13px;
    font-weight: 500; letter-spacing: 0.3px; transition: color 0.2s;
}
.nav-links a:hover { color: #e8e8f0; }
.nav-cta {
    background: linear-gradient(135deg, #6d28d9, #4f46e5);
    color: white !important; border: none; padding: 9px 20px;
    border-radius: 6px; font-size: 13px; font-weight: 600;
    cursor: pointer; text-decoration: none !important;
    transition: opacity 0.2s; display: inline-block;
}
.nav-cta:hover { opacity: 0.85; }

.hero {
    min-height: 90vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
    padding: 80px 48px 60px;
    position: relative; overflow: hidden;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(109,40,217,0.18) 0%, transparent 70%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(249,115,22,0.08) 0%, transparent 60%),
                #0a0a0f;
}
.hero-mesh {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(rgba(109,40,217,0.12) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black, transparent);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(109,40,217,0.15); border: 1px solid rgba(109,40,217,0.4);
    border-radius: 100px; padding: 6px 16px; margin-bottom: 32px;
    font-size: 12px; font-weight: 600; letter-spacing: 1px;
    color: #a78bfa; text-transform: uppercase;
}
.hero-badge-dot {
    width: 6px; height: 6px; border-radius: 50%; background: #a78bfa;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.4); }
}
.hero h1 {
    font-size: clamp(40px, 6vw, 76px);
    font-weight: 900; line-height: 1.05;
    letter-spacing: -2px; margin: 0 0 24px;
    background: linear-gradient(135deg, #ffffff 40%, #c4b5fd 75%, #a78bfa 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    max-width: 900px;
}
.hero-sub {
    font-size: clamp(16px, 2vw, 20px);
    color: #7070a0; max-width: 640px;
    line-height: 1.7; margin: 0 0 48px; font-weight: 400;
}
.hero-ctas { display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
.btn-primary {
    background: linear-gradient(135deg, #6d28d9, #4f46e5);
    color: white !important; padding: 14px 32px; border-radius: 8px;
    font-size: 15px; font-weight: 700; text-decoration: none !important;
    display: inline-block; transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 24px rgba(109,40,217,0.4);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(109,40,217,0.5); }
.btn-secondary {
    background: transparent; color: #e8e8f0 !important;
    padding: 14px 32px; border-radius: 8px;
    border: 1px solid #2a2a4a; font-size: 15px; font-weight: 600;
    text-decoration: none !important; display: inline-block;
    transition: border-color 0.2s, background 0.2s;
}
.btn-secondary:hover { border-color: #6d28d9; background: rgba(109,40,217,0.08); }

.section { padding: 96px 48px; }
.section-alt { background: #0d0d18; }
.section-label {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    color: #6d28d9; text-transform: uppercase; margin-bottom: 12px;
}
.section-title {
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 800; letter-spacing: -1.5px; line-height: 1.1;
    margin: 0 0 16px;
}
.section-sub {
    font-size: 17px; color: #6060a0; max-width: 560px;
    line-height: 1.7; margin: 0 0 56px;
}

.stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 2px; background: #1a1a2e; border-radius: 16px;
    overflow: hidden; border: 1px solid #1e1e32;
}
.stat-cell {
    background: #0d0d18; padding: 40px 32px; text-align: center;
}
.stat-number {
    font-size: clamp(36px, 4vw, 56px);
    font-weight: 900; letter-spacing: -2px; line-height: 1;
    background: linear-gradient(135deg, #ffffff, #a78bfa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}
.stat-label { font-size: 13px; color: #5050a0; font-weight: 500; line-height: 1.5; }

.ba-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 16px; }
.ba-card { border-radius: 16px; padding: 32px; }
.ba-before { background: #0d0d14; border: 1px solid #2a1a1a; }
.ba-after  { background: #0d0d14; border: 1px solid #1a2a1a; }
.ba-header {
    font-size: 15px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 24px;
}
.ba-before .ba-header { color: #ef4444; }
.ba-after  .ba-header { color: #10b981; }
.ba-row {
    display: flex; justify-content: space-between; align-items: flex-start;
    padding: 14px 0; border-bottom: 1px solid #1e1e2e;
}
.ba-row:last-child { border-bottom: none; }
.ba-row-label { font-size: 17px; color: #6060a0; flex: 1; }
.ba-row-val { font-size: 17px; font-weight: 700; text-align: right; max-width: 55%; }
.ba-before .ba-row-val { color: #ef4444; }
.ba-after  .ba-row-val { color: #10b981; }

.zigzag-item {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 64px; align-items: center;
    padding: 64px 0; border-bottom: 1px solid #1a1a2e;
}
.zigzag-item:last-child { border-bottom: none; }
.zigzag-item.reverse { direction: rtl; }
.zigzag-item.reverse > * { direction: ltr; }
.zigzag-text h3 {
    font-size: clamp(22px, 3vw, 32px); font-weight: 800;
    letter-spacing: -1px; margin: 0 0 16px; line-height: 1.2;
}
.zigzag-text p { font-size: 15px; color: #6060a0; line-height: 1.8; margin: 0; }
.zigzag-visual {
    background: #111120; border: 1px solid #1e1e32;
    border-radius: 16px; padding: 32px;
    display: flex; flex-direction: column; gap: 12px;
}
.pill {
    background: #0d0d1e; border: 1px solid #2a2a4a;
    border-radius: 8px; padding: 12px 16px;
    font-size: 13px; color: #8080b0;
    display: flex; align-items: center; gap: 10px;
}
.pill-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.pill-purple .pill-dot { background: #6d28d9; }
.pill-orange .pill-dot { background: #f97316; }
.pill-green  .pill-dot  { background: #10b981; }
.pill-blue   .pill-dot  { background: #3b82f6; }

.entry-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 24px; margin-top: 16px;
}
.entry-card {
    background: #111120; border: 1px solid #1e1e32;
    border-radius: 16px; padding: 32px;
    display: flex; flex-direction: column;
    transition: border-color 0.3s, transform 0.3s;
}
.entry-card:hover { border-color: #6d28d9; transform: translateY(-4px); }
.entry-card.featured {
    border-color: #6d28d9;
    background: linear-gradient(160deg, #13132a, #111120);
    box-shadow: 0 0 40px rgba(109,40,217,0.15);
}
.entry-phase {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: #a78bfa; margin-bottom: 12px;
}
.entry-card h3 { font-size: 20px; font-weight: 800; letter-spacing: -0.5px; margin: 0 0 12px; }
.entry-card p { font-size: 14px; color: #6060a0; line-height: 1.65; margin: 0 0 24px; flex: 1; }
.entry-features { list-style: none; padding: 0; margin: 0 0 28px; }
.entry-features li {
    font-size: 13px; color: #8080b0; padding: 6px 0;
    display: flex; align-items: center; gap: 8px;
}
.entry-features li::before { content: '✓'; color: #6d28d9; font-weight: 700; flex-shrink: 0; }
.entry-btn {
    display: block; text-align: center; padding: 12px;
    border-radius: 8px; font-size: 14px; font-weight: 700;
    text-decoration: none !important; transition: all 0.2s; margin-top: auto;
}
.entry-btn-primary {
    background: linear-gradient(135deg, #6d28d9, #4f46e5);
    color: white !important; box-shadow: 0 4px 16px rgba(109,40,217,0.35);
}
.entry-btn-secondary {
    background: transparent; color: #e8e8f0 !important;
    border: 1px solid #2a2a4a;
}
.entry-btn:hover { opacity: 0.85; transform: translateY(-1px); }

.uc-tag {
    display: inline-block; font-size: 14px; font-weight: 600;
    letter-spacing: 0.5px; padding: 3px 10px; border-radius: 100px;
    margin-bottom: 8px; margin-right: 6px;
}
.tag-mistral { background: rgba(249,115,22,0.12); color: #f97316; }
.tag-vast    { background: rgba(109,40,217,0.12); color: #a78bfa; }

.footer {
    border-top: 1px solid #1a1a2e; padding: 40px 48px;
    display: flex; align-items: center; justify-content: space-between;
}
.footer-brand {
    font-size: 15px; font-weight: 800;
    background: linear-gradient(90deg, #ffffff, #a78bfa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

div[data-testid="stTabs"] button { color: #6060a0 !important; font-size: 13px !important; }
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #a78bfa !important; border-bottom-color: #6d28d9 !important;
}
</style>
""", unsafe_allow_html=True)

# ── NAV ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
  <div class="nav-logos">
    <span class="nav-brand">VAST</span>
    <span class="nav-divider">×</span>
    <span class="nav-partner">Mistral AI</span>
  </div>
  <div class="nav-links">
    <a href="#solutions">Solutions</a>
    <a href="#results">Results</a>
    <a href="#savings">Cost &amp; Time</a>
    <a href="#why">Why Now</a>
    <a href="#entry">Get Started</a>
  </div>
  <a href="#entry" class="nav-cta">Choose Your Entry Point →</a>
</div>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-mesh"></div>
  <div class="hero-badge">
    <span class="hero-badge-dot"></span>
    VAST + Mistral AI · Unified AI Data Infrastructure
  </div>
  <h1>An End-to-End AI Stack<br>Powered by VAST &amp; NVIDIA</h1>
  <p class="hero-sub">
    From video intelligence to enterprise RAG to real-time data security —
    VAST and Mistral deliver unified AI infrastructure that eliminates silos,
    cuts latency by 20×, and deploys complex pipelines in an hour or less.
  </p>
  <div class="hero-ctas">
    <a href="#solutions" class="btn-primary">Explore Solutions</a>
    <a href="#entry" class="btn-secondary">Choose Your Entry Point</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1: SOLUTIONS ──────────────────────────────────────────────────────
st.markdown('<div id="solutions"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Solutions &amp; Use Cases</div>
  <div class="section-title">Agentic Pipeline Blueprints.<br>One Simple Platform.</div>
  <div class="section-sub">
    Mistral's VLMs and LLMs run natively on VAST —
    from ingestion to inference, no data movement required.
  </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🎥  Video Search Summarization",
    "📄  Document RAG",
    "🔐  Data Classification & Security",
])

with tab1:
    st.markdown("""
    <div style="padding:32px 0;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;">
        <div>
          <span class="uc-tag tag-mistral">Mistral VLMs</span>
          <span class="uc-tag tag-vast">VAST Event Broker</span>
          <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 16px;">Video Search Summarization</h3>
          <p style="font-size:19px;color:#6060a0;line-height:1.8;margin:0 0 20px;">
            Transform massive video archives into searchable, actionable intelligence.
            The VAST VSS blueprint is a fully operationalized, production-ready implementation
            of NVIDIA's reference architecture — deployable in <strong style="color:#e8e8f0;">under a single working day</strong>.
          </p>
          <p style="font-size:19px;color:#6060a0;line-height:1.8;margin:0 0 20px;">
            When video lands in a VAST S3 bucket, a built-in Kafka-compatible event broker triggers
            an AI pipeline processing up to <strong style="color:#e8e8f0;">1 million events per second</strong>.
            <strong style="color:#f97316;">Mistral Vision-Language Models</strong> analyze chunked video with
            dynamically customized prompts, generating rich semantic scene descriptions stored as vector
            embeddings directly in the VAST DataBase.
          </p>
          <p style="font-size:19px;color:#6060a0;line-height:1.8;margin:0 0 28px;">
            Operators query across <strong style="color:#e8e8f0;">trillions of vectors from one namespace</strong> in natural language —
            simultaneously running semantic similarity search while filtering by metadata like timestamp, location, or camera ID.
          </p>
          <div style="background:#0d0d1e;border:1px solid #2a1a3a;border-radius:12px;padding:20px 24px;margin-bottom:20px;">
            <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#6d28d9;text-transform:uppercase;margin-bottom:16px;">Challenges VAST Solves</div>
            <div style="display:flex;flex-direction:column;gap:16px;">
              <div>
                <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚡ Metadata Hotspots at 500K Cameras</div>
                <div style="font-size:17px;color:#6060a0;line-height:1.7;">Legacy systems break down at scale. VAST's Disaggregated Shared-Everything (DASE) architecture provides a global, lockless metadata pool — eliminating hotspots and delivering the NVMe bandwidth needed for 500K simultaneous streams.</div>
              </div>
              <div>
                <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🧬 Vector Scale: 259 Billion+ Vectors</div>
                <div style="font-size:17px;color:#6060a0;line-height:1.7;">500K cameras × 10s chunks × 30 days = ~259B vectors minimum. VAST's built-in Vector DB supports trillions of vectors with hybrid semantic + metadata search in one unified system — no fragmented clusters.</div>
              </div>
              <div>
                <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔁 Re-process Historical Video Instantly</div>
                <div style="font-size:17px;color:#6060a0;line-height:1.7;">New investigation, new AI agent? VAST's all-flash platform eliminates cold storage delays — agents instantly re-scan archived video at NVMe speeds and query enriched metadata to pinpoint only the relevant segments.</div>
              </div>
              <div>
                <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔓 No Vendor Lock-in, Future-Proof Models</div>
                <div style="font-size:17px;color:#6060a0;line-height:1.7;">Swap or upgrade models — Qwen to Cosmos Reason 2 — without architectural overhauls. Scale-to-Zero automatically minimizes resource consumption during idle periods.</div>
              </div>
            </div>
          </div>
        </div>
        <div style="display:flex;flex-direction:column;gap:14px;">
          <div class="zigzag-visual">
            <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#a78bfa;text-transform:uppercase;margin-bottom:12px;">VSS Blueprint Pipeline</div>
            <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#c4b5fd;font-size:17px;">Stage 1 · Ingest</strong><br><span style="font-size:16px;">CCTV / VMS stream → VAST S3 object bucket</span></div></div>
            <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
            <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;font-size:17px;">Stage 2 · Trigger</strong><br><span style="font-size:16px;">Built-in Kafka event broker fires (1M/sec) — no external broker needed</span></div></div>
            <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
            <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;font-size:17px;">Stage 3 · Inference</strong><br><span style="font-size:16px;">NVIDIA microservices chunk video → Mistral VLM analyzes with custom prompts</span></div></div>
            <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
            <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#c4b5fd;font-size:17px;">Stage 4 · Store</strong><br><span style="font-size:16px;">Scene descriptions embedded → vectors + metadata stored in VAST DB</span></div></div>
            <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
            <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;font-size:17px;">Stage 5 · Search</strong><br><span style="font-size:16px;">Hybrid semantic + metadata NL search across trillions of vectors</span></div></div>
            <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
            <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;font-size:17px;">Stage 6 · Act</strong><br><span style="font-size:16px;">Agentic workflows: ServiceNow log, incident report, first responder dispatch</span></div></div>
          </div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:10px;padding:18px 20px;">
            <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#5050a0;text-transform:uppercase;margin-bottom:14px;">Key Capabilities</div>
            <ul style="margin:0;padding-left:18px;font-size:17px;color:#7070a0;line-height:2.3;">
              <li>500,000+ camera feeds — zero metadata hotspots</li>
              <li>Trillions of vectors in one unified namespace</li>
              <li>Intelligent frame selection — GPU only on high-priority data</li>
              <li>Re-process historical video instantly at NVMe speeds</li>
              <li>Open-source blueprint — fork, extend, swap models freely</li>
              <li>Full source on <a href="https://github.com/vast-data/cosmos-labs" target="_blank" style="color:#a78bfa;">Cosmos Labs GitHub</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-mistral">Mistral LLMs</span>
      <span class="uc-tag tag-vast">VAST Sync Engine</span>
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Document RAG</h3>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown("""
        <div style="background:#0d0d1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#6d28d9;text-transform:uppercase;margin-bottom:18px;">Why VAST vs. AWS / Open Source</div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔀 Swap to Custom Mistral Models — No Redesign</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">The entire pipeline is open-source and modular. Redirect the inference endpoint to your own fine-tuned or open-weight Mistral releases — no infrastructure redesign required.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚡ Zero-ETL Sync Engine Triggers Mistral Embeddings</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">No complex Airflow pipelines. VAST's native Sync Engine pulls from Confluence, Google Drive, or SharePoint directly into S3 — the moment a doc lands, it triggers your custom Mistral embedding function automatically.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">📦 Serverless Scale-to-Zero vs. Managing EKS Node Groups</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">VAST's DataEngine runs containerized functions natively on the storage cluster. Backlogs auto-scale up linearly; idle pipelines scale to zero — consuming zero compute when no documents need processing.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🧬 Unified Vector + Metadata Store vs. RDS + Milvus/Pinecone</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">No stitching together separate datastores. Vectors live as a column in VastDB alongside metadata — your Mistral RAG agent runs hybrid semantic + metadata searches in a single native query.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔐 Automatic ACL Enforcement — No Engineering Overhead</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">ACLs from Confluence or SharePoint are fetched and stored in VastDB at ingest. When your Mistral agent answers a prompt, it queries by Azure AD identity — users only see chunks they're authorized to view, automatically.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div style="background:#111120;border:1px solid #1e1e32;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#a78bfa;text-transform:uppercase;margin-bottom:16px;">Document RAG Pipeline Flow</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#bfdbfe;font-size:16px;">Stage 1 · Sync</strong><br><span style="font-size:15px;color:#8080b0;">VAST Sync Engine pulls docs from Google Drive / SharePoint / Confluence into VAST S3</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:16px;">Stage 2 · Trigger</strong><br><span style="font-size:15px;color:#8080b0;">Doc landing triggers built-in event broker — ACLs fetched and stored alongside</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#6d28d9;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#c4b5fd;font-size:16px;">Stage 3 · DataEngine</strong><br><span style="font-size:15px;color:#8080b0;">Serverless functions chunk text and prepare it for your Mistral embedding model</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:16px;">Stage 4 · Mistral Embedding</strong><br><span style="font-size:15px;color:#8080b0;">Custom or default Mistral model generates embeddings — swap endpoints without redesign</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#6d28d9;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#c4b5fd;font-size:16px;">Stage 5 · Store</strong><br><span style="font-size:15px;color:#8080b0;">Vectors, metadata and ACLs written as columns in VastDB — no separate vector store</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:16px;">Stage 6 · RAG Agent</strong><br><span style="font-size:15px;color:#8080b0;">Mistral agent queries by Azure AD identity — hybrid semantic + metadata search, ACL-enforced</span></div>
          </div>
        </div>
        <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:10px;padding:18px 20px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#5050a0;text-transform:uppercase;margin-bottom:14px;">Key Capabilities</div>
          <div style="font-size:16px;color:#7070a0;line-height:2.3;">
            ✓ &nbsp;Swap Mistral model endpoints without redesign<br>
            ✓ &nbsp;Zero-ETL sync from Confluence, Drive, SharePoint<br>
            ✓ &nbsp;Scale-to-zero serverless compute on storage cluster<br>
            ✓ &nbsp;Unified vector + metadata in a single VastDB query<br>
            ✓ &nbsp;Automatic ACL enforcement via Azure AD identity<br>
            ✓ &nbsp;Open-source blueprint — fully forkable
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-mistral">Mistral LLMs</span>
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Data Classification &amp; Security</h3>
    </div>
    """, unsafe_allow_html=True)

    col_c, col_d = st.columns(2, gap="large")

    with col_c:
        st.markdown("""
        <div style="background:#0d0d1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#6d28d9;text-transform:uppercase;margin-bottom:18px;">Why VAST vs. Legacy / Open Source</div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚡ Classification on Write vs. Batch Processing</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">Legacy regex tools run in slow batches covering only 10–25% of data during off-hours. VAST inspects data in real-time the moment it is written — ensuring all data is classified before it can become a Shadow AI risk.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔁 Built-in Event Broker vs. External Kafka</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">Open source requires standing up and maintaining external Kafka brokers. VAST natively integrates a Kafka-compatible broker directly into the storage layer — processing 1M events/sec with zero external infrastructure to manage.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🧱 Unified AIOS vs. Fragmented Silos</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">Open-source stacks bolt together MinIO, Milvus, Spark, and separate metadata DBs. VAST collapses everything into one exabyte-scale AI Operating System — eliminating security sprawl entirely.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚙️ Zero-ETL Agentic Workflows vs. Brittle Pipelines</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">Disjointed open-source components require heavy ETL to move data between the object store, vector DB, and inference endpoints. VAST's DataEngine eliminates ETL entirely — agentic services trigger directly on real-time ingestion.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">📊 Total Exabyte Coverage vs. Uncovered Data Lakes</div>
            <div style="font-size:16px;color:#6060a0;line-height:1.7;">Legacy systems leave enterprise data lakes nearly uncovered because traditional enumeration kills system controls. VAST's DASE architecture eliminates metadata hotspots — scaling linearly at exabyte scale without impacting production workloads.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_d:
        st.markdown("""
        <div style="background:#111120;border:1px solid #1e1e32;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#a78bfa;text-transform:uppercase;margin-bottom:16px;">Classification Pipeline Flow</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#bfdbfe;font-size:16px;">Stage 1 · Ingest</strong><br><span style="font-size:15px;color:#8080b0;">User writes file via S3/NFS/SMB or VAST Sync Engine pulls from Google Drive / SharePoint</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:16px;">Stage 2 · Trigger</strong><br><span style="font-size:15px;color:#8080b0;">Built-in Kafka-compatible event broker fires instantly — no external routing needed</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#6d28d9;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#c4b5fd;font-size:16px;">Stage 3 · Pre-process</strong><br><span style="font-size:15px;color:#8080b0;">DataEngine serverless functions chunk the file and prepare text for inference</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:16px;">Stage 4 · Mistral Inference</strong><br><span style="font-size:15px;color:#8080b0;">Mistral LLM returns structured JSON: classification level, confidence scores, content summary</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;font-size:18px;">↓</div>
          <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:16px;">Stage 5 · Store &amp; Act</strong><br><span style="font-size:15px;color:#8080b0;">Tags, vectors and ACLs written to VAST DB — sovereignty rules enforced or downstream alert triggered</span></div>
          </div>
        </div>
        <div style="background:#0d0d1e;border:1px solid #2a2a4a;border-radius:10px;padding:18px 20px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#5050a0;text-transform:uppercase;margin-bottom:14px;">Key Capabilities</div>
          <div style="font-size:16px;color:#7070a0;line-height:2.3;">
            ✓ &nbsp;Real-time classification on write — zero batch lag<br>
            ✓ &nbsp;1M events/sec native Kafka-compatible broker<br>
            ✓ &nbsp;FIPS 140-3 validated encryption<br>
            ✓ &nbsp;Data Passport: sovereignty rules travel with data<br>
            ✓ &nbsp;Zero-ETL — agentic triggers on raw ingest<br>
            ✓ &nbsp;Exabyte-scale coverage via DASE architecture
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── SECTION 2: RESULTS
# ── SECTION 2: RESULTS ────────────────────────────────────────────────────────
st.markdown('<div id="results"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-alt">
  <div class="section-label">Results</div>
  <div class="section-title">Numbers That Change<br>What's Possible.</div>
  <div class="section-sub">Real-world performance delivered by the VAST + Mistral stack.</div>
  <div class="stats-grid">
    <div class="stat-cell">
      <div class="stat-number">20×</div>
      <div class="stat-label">Faster latency<br><span style="font-size:12px;color:#4040a0;">TTFT: 63s → 3s via KV cache offload</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">99.999%</div>
      <div class="stat-label">Uptime<br><span style="font-size:12px;color:#4040a0;">AI training job failure rate −90%</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">3GB/s</div>
      <div class="stat-label">Per Vera Rubin GPU (NCP)<br><span style="font-size:12px;color:#4040a0;">Exceeding GPU bandwidth at scale</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">2.12×</div>
      <div class="stat-label">Data reduction<br><span style="font-size:12px;color:#4040a0;">Avg across global fleets</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3: COST & TIME SAVINGS ───────────────────────────────────────────
st.markdown('<div id="savings"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Time &amp; Cost Savings</div>
  <div class="section-title">Legacy Infrastructure<br>vs. VAST.</div>
  <div class="section-sub">The economics of AI infrastructure have changed. Here's what you leave behind.</div>
  <div class="ba-grid">
    <div class="ba-card ba-before">
      <div class="ba-header">❌ &nbsp;Legacy Approach</div>
      <div class="ba-row"><span class="ba-row-label">Observability storage cost</span><span class="ba-row-val">$1–$4 / GB ingestion</span></div>
      <div class="ba-row"><span class="ba-row-label">Inference latency (TTFT)</span><span class="ba-row-val">63 seconds</span></div>
      <div class="ba-row"><span class="ba-row-label">Edge deployment footprint</span><span class="ba-row-val">+12 hardware racks</span></div>
      <div class="ba-row"><span class="ba-row-label">Pipeline deployment time</span><span class="ba-row-val">Weeks</span></div>
      <div class="ba-row"><span class="ba-row-label">GPU memory efficiency</span><span class="ba-row-val">Low — KV cache on GPU</span></div>
      <div class="ba-row"><span class="ba-row-label">Data classification</span><span class="ba-row-val">Slow batch processing</span></div>
    </div>
    <div class="ba-card ba-after">
      <div class="ba-header">✅ &nbsp;VAST + Mistral</div>
      <div class="ba-row"><span class="ba-row-label">Observability storage cost</span><span class="ba-row-val">Cents / GB · infinite retention</span></div>
      <div class="ba-row"><span class="ba-row-label">Inference latency (TTFT)</span><span class="ba-row-val">3 seconds (20× faster)</span></div>
      <div class="ba-row"><span class="ba-row-label">Edge deployment footprint</span><span class="ba-row-val">75% less power · 12 racks removed</span></div>
      <div class="ba-row"><span class="ba-row-label">Pipeline deployment time</span><span class="ba-row-val">Under 1 working day</span></div>
      <div class="ba-row"><span class="ba-row-label">GPU memory efficiency</span><span class="ba-row-val">Up to 90% better · KV on NVMe</span></div>
      <div class="ba-row"><span class="ba-row-label">Data classification</span><span class="ba-row-val">Real-time via Mistral DataEngine</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4: WHY VAST NOW ───────────────────────────────────────────────────
st.markdown('<div id="why"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-alt">
  <div class="section-label">Why VAST</div>
  <div class="section-title">A New Architecture.<br>A New Art of the Possible.</div>
  <div class="section-sub">The fundamental shifts that make VAST the platform for what comes next.</div>

  <div class="zigzag-item">
    <div class="zigzag-text">
      <div class="section-label">Shift 01</div>
      <h3>The Rise of Physical &amp; Agentic AI</h3>
      <p>Imagine architecting the ultimate Smart City — scaling to 200,000 cameras with live robotics and autonomous drones. On AWS, latency and ETL overhead of moving video to S3, syncing metadata to RDS, and triggering SageMaker would bottleneck every physical AI use case.</p>
      <p style="margin-top:16px;">On VAST, you build a fully open pipeline using your own Mistral models:</p>
      <ul style="margin:12px 0 0;padding-left:20px;color:#6060a0;font-size:15px;line-height:2.0;">
        <li><strong style="color:#e8e8f0;">Massive Scale:</strong> 1,500 GPUs for robotics + hundreds for real-time inference, adjacent to storage</li>
        <li><strong style="color:#e8e8f0;">Synthetic Data:</strong> CARLA simulator generates photorealistic corner-case training video</li>
        <li><strong style="color:#e8e8f0;">Custom Mistral VLM:</strong> Deploy Pixtral Large natively on the VAST DataEngine — swap out proprietary endpoints entirely</li>
        <li><strong style="color:#e8e8f0;">Unified Agentic Action:</strong> mistral-embed vectors stored in VastDB; Mistral Large agent triggers ServiceNow, incident reports, and first responder dispatch at 1M events/sec</li>
      </ul>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">200K cameras</strong><br><span style="font-size:14px;">Municipal surveillance + robotics network</span></div></div>
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#c4b5fd;">Pixtral Large on DataEngine</strong><br><span style="font-size:14px;">Custom Mistral VLM — no proprietary lock-in</span></div></div>
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">mistral-embed → VastDB</strong><br><span style="font-size:14px;">Vectors + metadata in one unified store</span></div></div>
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">1M events/sec</strong><br><span style="font-size:14px;">Mistral Large agent triggers real-world agentic actions</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">CARLA Synthetic Data</strong><br><span style="font-size:14px;">Train on rare corner cases impossible to find in real footage</span></div></div>
    </div>
  </div>

  <div class="zigzag-item reverse">
    <div class="zigzag-text">
      <div class="section-label">Shift 02</div>
      <h3>Deep Mistral Integration</h3>
      <p>VAST is built to empower Mistral's advanced models, bringing deliberate, multi-modal reasoning directly into your video analytics and data classification workflows.</p>
      <p style="margin-top:16px;">Because the VAST DataEngine processes events in real-time, Mistral VLMs and LLMs run natively on the platform — no external inference endpoints, no complex data movement, no latency tax. Swap model versions, redirect endpoints, and upgrade without architectural overhaul.</p>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">Mistral VLMs natively on DataEngine</strong><br><span style="font-size:14px;">Multi-modal reasoning at ingest — zero data movement</span></div></div>
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#c4b5fd;">Swap endpoints without redesign</strong><br><span style="font-size:14px;">Point to any Mistral model — fine-tuned or open-weight</span></div></div>
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">Real-time event processing</strong><br><span style="font-size:14px;">Classification and inference trigger on raw ingest</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">No latency tax</strong><br><span style="font-size:14px;">No ETL, no external endpoints, no data movement</span></div></div>
    </div>
  </div>

  <div class="zigzag-item">
    <div class="zigzag-text">
      <div class="section-label">Shift 03</div>
      <h3>Sovereignty as a Service</h3>
      <p>Enterprises demand zero-trust, hard multi-tenancy. VAST delivers FIPS 140-3 validated encryption, strict isolation, and a "Data Passport" — sovereignty rules that travel dynamically with the data. Compliance isn't a layer you add. It's built into the architecture.</p>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-green"><span class="pill-dot"></span>🛂 Data Passport — sovereignty travels with data</div>
      <div class="pill pill-purple"><span class="pill-dot"></span>🔐 FIPS 140-3 validated encryption</div>
      <div class="pill pill-orange"><span class="pill-dot"></span>🧱 Hard multi-tenancy — strict isolation</div>
      <div class="pill pill-blue"><span class="pill-dot"></span>🌍 Cross-border compliance built in</div>
    </div>
  </div>

  <div class="zigzag-item reverse">
    <div class="zigzag-text">
      <div class="section-label">Shift 04</div>
      <h3>Eliminate Every Silo</h3>
      <p>VAST provides a unified AI Operating System (AIOS) that collapses file storage, object storage, transactional databases, vector databases, streaming, and serverless compute into one exabyte-scale platform. One system. One API surface. Zero silos.</p>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-purple"><span class="pill-dot"></span>📁 File + Object + Block storage unified</div>
      <div class="pill pill-orange"><span class="pill-dot"></span>🧬 Vector DB + Transactional DB combined</div>
      <div class="pill pill-green"><span class="pill-dot"></span>⚡ Serverless compute — built in</div>
      <div class="pill pill-blue"><span class="pill-dot"></span>📊 Observability + Data Lakehouse native</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5: ENTRY POINTS ───────────────────────────────────────────────────
st.markdown('<div id="entry"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="padding:96px 48px 24px; background:#0a0a0f;">
  <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#6d28d9;text-transform:uppercase;margin-bottom:12px;">Choose Your Entry Point</div>
  <div style="font-size:48px;font-weight:800;letter-spacing:-1.5px;line-height:1.1;margin:0 0 16px;color:#e8e8f0;">Start Where<br>You Are.</div>
  <div style="font-size:17px;color:#6060a0;max-width:560px;line-height:1.7;margin:0 0 40px;">Three paths to production AI infrastructure — from foundational storage to full AIOS deployment.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div style="background:#111120;border:1px solid #1e1e32;border-radius:16px;padding:32px;height:100%;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#a78bfa;margin-bottom:12px;">Phase 1</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Deploy Storage Services</div>
      <div style="font-size:14px;color:#6060a0;line-height:1.65;margin-bottom:24px;">Start with the highest-performance storage foundation — NFS, SMB, S3 Object, and NVMe/TCP Block — with global namespaces, snapshots, and wire encryption built in.</div>
      <div style="font-size:14px;color:#8080b0;line-height:2.2;">
        <div>✓ &nbsp;NFS / SMB / S3 Object / NVMe-TCP Block</div>
        <div>✓ &nbsp;Global namespaces &amp; instant snapshots</div>
        <div>✓ &nbsp;Wire encryption &amp; FIPS 140-3</div>
        <div>✓ &nbsp;10TB/s read bandwidth — GPU zero-starvation</div>
        <div>✓ &nbsp;Kubernetes install in 15 minutes</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Start with Infrastructure →", "#", use_container_width=True)

with col2:
    st.markdown("""
    <div style="background:linear-gradient(160deg,#13132a,#111120);border:2px solid #6d28d9;border-radius:16px;padding:32px;height:100%;box-shadow:0 0 40px rgba(109,40,217,0.2);">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#a78bfa;margin-bottom:12px;">Phase 2 — Most Popular</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Add Advanced Data Services</div>
      <div style="font-size:14px;color:#6060a0;line-height:1.65;margin-bottom:24px;">Layer on the full VAST AIOS: Data Lakehouse, streaming Event Broker, Vector Database, InsightEngine, and Observability — all on the same platform.</div>
      <div style="font-size:14px;color:#8080b0;line-height:2.2;">
        <div>✓ &nbsp;Vector DB + Transactional DB unified</div>
        <div>✓ &nbsp;Event Broker — 1M events/sec</div>
        <div>✓ &nbsp;Data Lakehouse with flat storage economics</div>
        <div>✓ &nbsp;Native Mistral LLM / VLM hosting</div>
        <div>✓ &nbsp;InsightEngine + Observability included</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Explore Full Platform →", "#", use_container_width=True, type="primary")

with col3:
    st.markdown("""
    <div style="background:#111120;border:1px solid #1e1e32;border-radius:16px;padding:32px;height:100%;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#a78bfa;margin-bottom:12px;">Blueprints</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Deploy a Ready-to-Use Blueprint</div>
      <div style="font-size:14px;color:#6060a0;line-height:1.65;margin-bottom:24px;">Fast-track with open-source Cosmos Labs blueprints. Go from zero to a production-grade VSS or Document RAG pipeline in under a single working day.</div>
      <div style="font-size:14px;color:#8080b0;line-height:2.2;">
        <div>✓ &nbsp;VSS Blueprint — Video Search Summarization</div>
        <div>✓ &nbsp;Document RAG Assistant Blueprint</div>
        <div>✓ &nbsp;Mistral models pre-integrated</div>
        <div>✓ &nbsp;NVIDIA Cosmos Reason 2 compatible</div>
        <div>✓ &nbsp;Open source — fork and extend freely</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Browse Blueprints →", "https://github.com/vast-data/cosmos-labs", use_container_width=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-brand">VAST × Mistral AI</div>
    <div style="font-size:12px;color:#3030a0;margin-top:4px;">The AI Operating System for the Enterprise</div>
  </div>
  <div style="font-size:12px;color:#3030a0;">© 2025 VAST Data. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)
