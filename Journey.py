from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Journey P｜角色狀態", page_icon="🧭", layout="wide")


def image_data(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


traveler = image_data(APP_DIR / "static" / "traveler.png")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700;900&display=swap');
    :root { --gold:#c89a4b; --pale:#ead9b5; --ink:#0a0b0c; --panel:#171713; }
    * { box-sizing:border-box; }
    html, body, [class*="css"] { font-family:'Noto Serif TC','Microsoft JhengHei',serif; }
    .stApp {
      color:var(--pale); min-height:100vh;
      background:
        radial-gradient(circle at 16% 45%, rgba(37,67,68,.42), transparent 30%),
        radial-gradient(circle at 88% 30%, rgba(34,55,92,.5), transparent 32%),
        linear-gradient(180deg,#07101e 0%,#101815 57%,#080a09 100%);
    }
    .stApp:before { content:""; position:fixed; inset:0; pointer-events:none; opacity:.13;
      background-image:linear-gradient(rgba(255,255,255,.15) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.1) 1px,transparent 1px); background-size:4px 4px; }
    .wood-menu{position:fixed;z-index:3;left:max(12px,calc(50vw - 595px));top:50%;transform:translateY(-50%);width:116px;padding:20px 8px 10px;display:flex;flex-direction:column;gap:9px;border:3px solid #3a210e;outline:2px solid #9b642b;border-radius:5px;background:repeating-linear-gradient(88deg,#6e3f1d 0,#7f4b23 7px,#5c3217 13px,#76431f 20px);box-shadow:inset 0 0 0 3px #b27738,inset 0 0 18px #241106,0 8px 22px #000}.wood-slot{position:relative;width:94px;height:42px;border:2px solid #38200e;border-radius:3px;background:radial-gradient(circle at 45% 42%,#392313,#1b120c 72%);box-shadow:inset 0 0 0 2px #8b592b,inset 0 0 10px #000,0 2px 3px #2b1509}.wood-slot:after{content:"";position:absolute;left:50%;top:50%;width:18px;height:18px;border:1px solid #8d6537;transform:translate(-50%,-50%) rotate(45deg);opacity:.45}
    header[data-testid="stHeader"], #MainMenu, footer { display:none; }
    .block-container { max-width:890px; width:74vw; padding:.45rem .7rem .3rem; position:relative; z-index:1; }
    .jp-shell { border:4px solid #6f4b21; outline:2px solid #1a1108; padding:10px; border-radius:7px;
      box-shadow:0 0 0 2px #d3a34e,0 0 0 7px #25180b,0 22px 65px #000; background:#0b0c0bd9; }
    .jp-inner { border:2px solid #76552e; padding:11px; background:linear-gradient(135deg,#191814f4,#0e100ff7); }
    .title-wrap { position:relative; z-index:5; display:flex; justify-content:center; margin:0 0 9px; }
    .title { min-width:420px; text-align:center; font-size:2.35rem; font-weight:900; letter-spacing:.22em; padding:10px 32px 14px;
      color:#f1e0b8; text-shadow:2px 3px #090704; border:3px solid #9d7131; outline:3px solid #15100a;
      background:linear-gradient(#243d6d,#16284b); box-shadow:inset 0 0 0 2px #cf9d42,0 7px 12px #000b; }
    .profile { display:flex; gap:18px; align-items:center; padding-bottom:15px; border-bottom:2px dotted #5a492e; }
    .portrait { width:70px;height:70px;border:3px solid #c8943d;box-shadow:0 0 0 4px #18130d;background:#243149;display:grid;place-items:center;font-size:34px; }
    .name { font-size:2rem;font-weight:900;color:#f0dfbd;line-height:1.2; }
    .mood { color:#c7b389;font-size:1.05rem;margin-top:6px; }
    .character-stage { position:relative; margin-top:9px; height:clamp(250px,calc(100vh - 405px),355px); overflow:hidden; border:1px solid #443821;
      background:radial-gradient(circle at 50% 58%,#17241d 0,#090d0e 66%,#050708 100%); box-shadow:inset 0 0 32px #000; padding:4px; }
    .character-stage img { display:block;width:100%;height:100%;object-fit:contain;object-position:center;image-rendering:pixelated;opacity:.96; }
    .slot { position:absolute;width:66px;height:66px;display:grid;place-items:center;font-size:32px;background:#11120fe8;border:2px solid #746246;box-shadow:inset 0 0 0 3px #080907,0 3px 8px #000; }
    .s1{left:14px;top:18px}.s2{left:14px;top:100px}.s3{left:14px;top:182px}.s4{right:14px;top:18px}.s5{right:14px;top:100px}.s6{right:14px;top:182px}
    .xp-card { display:grid;grid-template-columns:105px 1fr;margin-top:16px;border:2px solid #76552e;background:#11120f; }
    .level { padding:13px;text-align:center;background:linear-gradient(#17305a,#101b34);border-right:2px solid #ba8437;font-weight:900;color:#f3ce6b; }
    .level small{display:block}.level strong{font-size:2.2rem}.xp{padding:12px 16px}.xp-row{display:flex;justify-content:space-between;color:#ded0b3}.bar{height:14px;background:#090a09;border:2px solid #71634d;margin:7px 0 10px;box-shadow:inset 0 0 5px #000}.fill{height:100%;background:linear-gradient(#8fd45d,#397f32);}
    .title-tag { border:1px solid #52442e;padding:7px 12px;color:#e8d4a6;font-size:1.05rem; }
    .section-title { display:flex;align-items:center;gap:13px;color:#d8bf8b;font-size:1.2rem;letter-spacing:.15em;margin:5px 0 14px; }
    .section-title:before,.section-title:after{content:"";height:2px;flex:1;background:linear-gradient(90deg,transparent,#705d3a,transparent)}
    .vital { margin-bottom:9px;padding:9px 14px;border:2px solid #7b572e;background:#10100ef2;box-shadow:inset 0 0 0 2px #22170c; }
    .vital-top { display:flex;align-items:center;gap:12px;font-size:1.45rem;font-weight:900; }.vital-top .num{margin-left:auto;font-variant-numeric:tabular-nums}.icon{font-size:1.5rem}.red{color:#ff6d76}.blue{color:#5da8ff}.yellow{color:#f9d44f}
    .meter { height:18px;margin-top:10px;background:#070909;border:2px solid #9a7138;border-radius:3px;padding:2px; }.meter span{display:block;height:100%}.hp{background:linear-gradient(#fa5262,#b31d35)}.mp{background:linear-gradient(#3a9eff,#1764c4)}.sp{background:linear-gradient(#ffe86a,#c29b23)}
    .stats { display:grid;grid-template-columns:1fr 1fr;border:2px solid #4f432f;background:#11120f; }.stat{display:flex;justify-content:space-between;padding:10px 14px;border-bottom:1px dotted #50452f}.stat:nth-child(odd){border-right:1px solid #50452f}.stat b{color:#f0e2c5}.stat span:last-child{color:#d7c8aa;font-weight:700}
    .quest { margin-top:16px;border:2px solid #74552f;padding:15px;background:linear-gradient(90deg,#1b1710,#11130f); }.quest-head{display:flex;justify-content:space-between;color:#f0d18e;font-weight:900}.quest p{margin:8px 0 0;color:#bcae92}.quest-progress{height:8px;background:#080908;margin-top:10px}.quest-progress span{display:block;width:62%;height:100%;background:#cf9e45}
    .footer-note{text-align:center;color:#8f8066;margin:7px 0 0;font-size:.75rem;letter-spacing:.08em}
    div[data-testid="stButton"] button { border:2px solid #8e6935;background:linear-gradient(#252017,#11120f);color:#ead8b2;border-radius:2px;font-family:inherit;font-weight:700;box-shadow:inset 0 0 0 2px #0a0907; }
    div[data-testid="stButton"] button:hover{border-color:#ddb465;color:#fff1c9}
    div[data-testid="column"]{min-width:0}.section-title{font-size:.94rem;margin:1px 0 5px}.vital{margin-bottom:5px;padding:6px 10px}.vital-top{gap:7px;font-size:1.02rem}.meter{height:12px;margin-top:5px}.stat{padding:5px 9px;font-size:.87rem}.quest{margin-top:6px;padding:7px 9px;font-size:.85rem}.quest p{margin-top:2px}.quest-progress{margin-top:4px;height:5px}.footer-note{position:fixed;left:0;right:0;bottom:9px;margin:0;z-index:2;pointer-events:none}div[data-testid="stButton"] button{padding:6px;font-size:.85rem}
    @media(max-width:820px){.title{min-width:0;width:82%;font-size:1.55rem}.character-stage{height:420px}.stats{grid-template-columns:1fr}.stat:nth-child(odd){border-right:0}.jp-inner{padding:12px}.block-container{padding-top:2rem}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<aside class="wood-menu" aria-label="主要選單"><div class="wood-slot"></div><div class="wood-slot"></div><div class="wood-slot"></div><div class="wood-slot"></div><div class="wood-slot"></div></aside><div class="jp-shell"><div class="jp-inner"><div class="title-wrap"><div class="title">角色狀態</div></div>', unsafe_allow_html=True)

left, right = st.columns([1, 0.95], gap="large")
with left:
    st.markdown(
        f"""
        <div class="profile"><div class="portrait">🧑🏻‍🦱</div><div><div class="name">亞 倫</div><div class="mood">有點累，但還是會繼續冒險。</div></div></div>
        <div class="character-stage">
          <img src="data:image/png;base64,{traveler}" alt="披著深藍斗篷、手持長劍的像素風旅人">
          <div class="slot s1" title="武器">🗡️</div><div class="slot s2" title="守護">🛡️</div><div class="slot s3" title="專注披風">🧥</div>
          <div class="slot s4" title="信念護符">🔮</div><div class="slot s5" title="習慣指環">💍</div><div class="slot s6" title="旅者靴">🥾</div>
        </div>
        <div class="xp-card"><div class="level"><small>旅程等級</small><strong>18</strong></div><div class="xp"><div class="xp-row"><b>本週成長</b><span>2,360 / 4,500</span></div><div class="bar"><div class="fill" style="width:52%"></div></div><div class="title-tag">★ 見習冒險者 · 穩定前進中</div></div></div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="section-title">✦ 今日能量 ✦</div>
        <div class="vital"><div class="vital-top"><span class="icon">❤️</span><span>體力</span><span class="num red">72 / 120</span></div><div class="meter"><span class="hp" style="width:60%"></span></div></div>
        <div class="vital"><div class="vital-top"><span class="icon">💧</span><span>專注</span><span class="num blue">56 / 100</span></div><div class="meter"><span class="mp" style="width:56%"></span></div></div>
        <div class="vital"><div class="vital-top"><span class="icon">⚡</span><span>心力</span><span class="num yellow">38 / 100</span></div><div class="meter"><span class="sp" style="width:38%"></span></div></div>
        <div class="section-title">✦ 成長屬性 ✦</div>
        <div class="stats">
          <div class="stat"><b>⚔️ 行動力</b><span>56</span></div><div class="stat"><b>🥾 自律</b><span>34</span></div>
          <div class="stat"><b>🛡️ 韌性</b><span>42</span></div><div class="stat"><b>❤️ 健康</b><span>52</span></div>
          <div class="stat"><b>🎯 專注</b><span>92%</span></div><div class="stat"><b>💧 知識</b><span>28</span></div>
          <div class="stat"><b>✨ 創造力</b><span>18</span></div><div class="stat"><b>🍀 幸運</b><span>15</span></div>
        </div>
        <div class="quest"><div class="quest-head"><span>主線任務｜打造 Journey P</span><span>62%</span></div><p>下一步：完成角色介面，定義成長屬性。</p><div class="quest-progress"><span></span></div></div>
        """,
        unsafe_allow_html=True,
    )
    a, b = st.columns(2)
    with a:
        st.button("📜 查看今日任務", use_container_width=True)
    with b:
        st.button("🧭 繼續旅程", use_container_width=True, type="primary")

st.markdown('<div class="footer-note">JOURNEY P · EVERY DAY IS PART OF THE ADVENTURE</div></div></div>', unsafe_allow_html=True)
