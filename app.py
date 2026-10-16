import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import random
import datetime

# ==========================================
# 1. إعدادات الصفحة والتصميم العصري
# ==========================================
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تهيئة ذاكرة الجلسة
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

if "user_points" not in st.session_state:
    st.session_state.user_points = 150

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌸 شجرة الساكورا اليابانية الساحرة"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌸 شجرة الساكورا اليابانية الساحرة"

# CSS العام للتصميم النظيف
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #6366f1;
        border-right: 6px solid #f97316;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);
    }

    .hero-verse {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f97316;
        margin-bottom: 5px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.75rem;
        color: #ffffff;
    }

    .clean-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #10b981;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }

    .stButton>button {
        background: #10b981;
        color: white;
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #059669;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 متجر الأشجار الواقعية الفخمة والأنيميشن السينمائي المتقدم</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. اللوحة الجانبية: نموذج الإدخال (Form)
# ==========================================
with st.sidebar.form(key="main_form"):
    st.markdown("### 🎛️ لوحة القياسات الحيوية")
    st.caption("أدخل بياناتك ثم اضغط (إرسال وتحليل) للحفظ والتقييم")
    
    sleep_hours = st.slider("🌙 ساعات النوم اليومية", 3.0, 12.0, 7.5, 0.5)
    sleep_quality = st.slider("✨ جودة النوم الاستشفائي (1-15)", 1, 15, 12)
    screen_hours = st.slider("📱/🖥️ ساعات الشاشة (الإجهاد البصري)", 1.0, 14.0, 4.5, 0.5)
    
    total_study = st.slider("⏱️ إجمالي ساعات التواجد الدراسي", 1.0, 12.0, 4.0, 0.5)
    deep_focus = st.slider("🎯 ساعات التركيز النقي الصافي", 0.5, 12.0, 3.5, 0.5)
    
    room_temp = st.slider("🌡️ حرارة الغرفة (مئوية)", 16, 32, 23)
    overthinking_mins = st.slider("🌀 دقائق التفكير الزائد والقلق", 0, 120, 20, 5)
    
    stress_level = st.slider("⚠️ مستوى التوتر العصبي (1-15)", 1, 15, 5)
    motivation_level = st.slider("🔥 الدافعية والحماس (1-15)", 1, 15, 12)
    hydration_level = st.slider("💧 مستوى ترطيب الجسم (1-15)", 1, 15, 11)
    
    snack_type = st.selectbox("🍱 نوع الوجبة الخفيفة قبل المذاكرة", [
        "🍏 وجبة ذكية خفيفة (مكسرات، فواكه، زبادي)",
        "🥩 وجبة غنية بالبروتين (بيض، دجاج، أسماك)",
        "🍝 وجبة غداء ثقيلة/كاربوهيدرات (رز، معكرونة، وجبات سريعة)",
        "🍩 سكريات ومشروبات طاقة (حلويات، عصائر مصنعة)",
        "☕ معتمدة على الكافيين فقط (قهوة/شاي بدون طعام)",
        "🌙 صائم / لم أتناول وجبة"
    ])
    
    study_method = st.selectbox("📚 أسلوب المذاكرة الأساسي", [
        "التسجيل النشط والخرائط الذهنية",
        "حل المسائل والتطبيقات العملية",
        "القراءة التكرارية الصامتة"
    ])
    
    phone_isolation = st.selectbox("📵 عزل الهاتف الخلوي", [
        "مفصول تماماً في غرفة ثانية",
        "قريب بصامت ومقلوب",
        "في اليد أو بجانب الكتاب"
    ])

    submit_btn = st.form_submit_button(label="🚀 إرسال وتحليل البيانات")

if submit_btn:
    st.session_state.user_points += 25
    st.success("✅ تم حفظ التحليل واكتسبت +25 نقطة إضافية في رصيدك!")

# ==========================================
# 3. التبويبات الرئيسية
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ",
    "🌳 معارض الأشجار الواقعية",
    "🏛️ منصة الحكام والاستثمار"
])

# --- TAB 1: المؤشرات والموجز ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
    st.metric("النتيجة المعيارية الإجمالية", "460 / 500 نقطة")
    st.progress(92)
    st.success("🌟 أداء استثنائي وتوازن مثالي في القدرات العصبية.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية")
    st.success("🍃 ظروف الإضاءة والحرارة والتهوية مثالية للتركيز.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ محرك الطاقة المعرفية")
    st.info("⚡ سرعة الاستجابة العصبية في أعلى مستوياتها.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل والتفريغ ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التفريغ الذهني")
    st.success("🗑️ الذاكرة المؤقتة منقية وصافية تماماً.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 5: معارض الأشجار الـ 10 الواقعية عبر st.components مع SVG عالي التفصيل والأنيميشن ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 المعرض الفني للأشجار الواقعية المتقدمة والأنيميشن")
    st.write("تصاميم فنية عضوية متكاملة ومتحركة (تتضمن تدرجات لونية، لحاء أشجار مفصل، وتساقط بتلات وأوراق حية):")

    active = st.session_state.active_tree
    svg_tree_render = ""

    # تعريف ستايل الأنيميشن المشترك للريح والتساقط
    animation_styles = """
    <style>
        @keyframes sway {
            0% { transform: rotate(0deg); transform-origin: bottom center; }
            50% { transform: rotate(1.2deg); transform-origin: bottom center; }
            100% { transform: rotate(0deg); transform-origin: bottom center; }
        }
        @keyframes fall {
            0% { transform: translateY(0px) translateX(0px) rotate(0deg); opacity: 1; }
            100% { transform: translateY(380px) translateX(40px) rotate(360deg); opacity: 0; }
        }
        .animated-canopy { animation: sway 5s ease-in-out infinite; }
        .petal-1 { animation: fall 6s linear infinite; }
        .petal-2 { animation: fall 7.5s linear infinite; animation-delay: 2s; }
        .petal-3 { animation: fall 5.5s linear infinite; animation-delay: 3.5s; }
    </style>
    """

    if "الساكورا" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_sakura" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff1f2"/><stop offset="100%" stop-color="#ffe4e6"/></linearGradient>
                <linearGradient id="trunk_grad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#3b1d0e"/><stop offset="50%" stop-color="#5c2c16"/><stop offset="100%" stop-color="#2a1205"/></linearGradient>
                <radialGradient id="sakura_petal" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f472b6"/><stop offset="70%" stop-color="#db2777"/><stop offset="100%" stop-color="#be185d"/></radialGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_sakura)"/>
            <!-- أرضية طبيعية -->
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#d1fae5"/>
            <!-- جذع وأغصان عضوية واقعية -->
            <path d="M280 500 C280 400 290 330 270 260 C250 190 210 160 170 130 C220 150 250 180 270 220 C300 170 340 130 390 110 C340 140 310 180 300 240 C310 320 320 400 320 500 Z" fill="url(#trunk_grad)"/>
            <!-- تاج الأوراق الساكورا المتداخل والمتحرك -->
            <g class="animated-canopy">
                <circle cx="170" cy="140" r="85" fill="url(#sakura_petal)" opacity="0.9"/>
                <circle cx="390" cy="120" r="80" fill="url(#sakura_petal)" opacity="0.9"/>
                <circle cx="280" cy="90" r="110" fill="url(#sakura_petal)" opacity="0.95"/>
                <circle cx="230" cy="160" r="75" fill="#f472b6" opacity="0.85"/>
                <circle cx="330" cy="170" r="75" fill="#f472b6" opacity="0.85"/>
                <circle cx="280" cy="180" r="65" fill="#fb7185" opacity="0.9"/>
            </g>
            <!-- بتلات زهرية تتساقط بسينمائية -->
            <circle class="petal-1" cx="200" cy="150" r="6" fill="#fbcfe8"/>
            <circle class="petal-2" cx="350" cy="130" r="7" fill="#f472b6"/>
            <circle class="petal-3" cx="280" cy="100" r="5" fill="#fff1f2"/>
        </svg>
        """
    elif "الصنوبر" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_pine" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0f9ff"/><stop offset="100%" stop-color="#e0f2fe"/></linearGradient>
                <linearGradient id="pine_green" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_pine)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#f1f5f9"/>
            <rect x="280" y="320" width="40" height="160" fill="#1e293b" rx="8"/>
            <!-- طبقات صنوبر متدرجة ومفصلة مع ثلج -->
            <g class="animated-canopy">
                <polygon points="300,60 160,220 440,220" fill="url(#pine_green)"/>
                <polygon points="300,60 210,160 390,160" fill="#ffffff" opacity="0.35"/>
                <polygon points="300,160 130,320 470,320" fill="#0369a1"/>
                <polygon points="300,160 180,260 420,260" fill="#ffffff" opacity="0.3"/>
                <polygon points="300,260 100,420 500,420" fill="#075985"/>
            </g>
        </svg>
        """
    elif "الفطر" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_shroom" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#312e81"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_shroom)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#3730a3"/>
            <!-- ساق الفطر -->
            <path d="M240 480 C240 340 250 280 260 220 L340 220 C350 280 360 340 360 480 Z" fill="#e0e7ff"/>
            <!-- قبعة الفطر الساحرة مع توهج -->
            <g class="animated-canopy">
                <path d="M130 220 C130 80 470 80 470 220 C400 250 200 250 130 220 Z" fill="#dc2626"/>
                <circle cx="210" cy="150" r="22" fill="#ffffff" opacity="0.9"/>
                <circle cx="360" cy="140" r="28" fill="#ffffff" opacity="0.9"/>
                <circle cx="300" cy="190" r="16" fill="#ffffff" opacity="0.9"/>
                <circle cx="170" cy="190" r="18" fill="#ffffff" opacity="0.9"/>
            </g>
        </svg>
        """
    elif "النخيل" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_palm" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#fb923c"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_palm)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#fde047"/>
            <!-- جذع نخيل مائل وعضوي مفصل بخطوط -->
            <path d="M250 480 Q 320 280 290 140 L310 140 Q 350 280 270 480 Z" fill="#78350f"/>
            <!-- سعف النخيل الموزع باحترافية -->
            <g class="animated-canopy">
                <path d="M300 150 Q 450 80 540 140 Q 430 180 300 150 Z" fill="#15803d"/>
                <path d="M300 150 Q 480 180 540 260 Q 420 230 300 150 Z" fill="#16a34a"/>
                <path d="M300 150 Q 150 80 60 140 Q 170 180 300 150 Z" fill="#15803d"/>
                <path d="M300 150 Q 120 180 60 260 Q 180 230 300 150 Z" fill="#16a34a"/>
                <path d="M300 150 Q 300 40 310 10 Q 320 70 300 150 Z" fill="#22c55e"/>
            </g>
        </svg>
        """
    elif "القيقب" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_maple" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ffedd5"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_maple)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#ffedd5"/>
            <path d="M280 480 L280 280 C280 230 260 180 210 140 C280 160 300 200 310 280 L310 480 Z" fill="#451a03"/>
            <g class="animated-canopy">
                <circle cx="200" cy="160" r="95" fill="#ea580c" opacity="0.95"/>
                <circle cx="400" cy="170" r="90" fill="#ea580c" opacity="0.95"/>
                <circle cx="300" cy="100" r="120" fill="#dc2626" opacity="0.95"/>
                <circle cx="300" cy="190" r="100" fill="#f59e0b" opacity="0.9"/>
            </g>
            <circle class="petal-1" cx="220" cy="200" r="7" fill="#f97316"/>
            <circle class="petal-2" cx="380" cy="220" r="8" fill="#dc2626"/>
        </svg>
        """
    elif "الويسترليا" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_wist" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f3e8ff"/><stop offset="100%" stop-color="#e9d5ff"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_wist)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#e9d5ff"/>
            <path d="M280 480 L280 280 C280 220 260 180 210 140 C280 160 300 200 310 280 L310 480 Z" fill="#3b0764"/>
            <g class="animated-canopy">
                <circle cx="300" cy="130" r="130" fill="#c084fc" opacity="0.9"/>
                <!-- عناقيد زهور متدلية ساحرة -->
                <path d="M200 180 Q 180 260 170 350" stroke="#a855f7" stroke-width="14" stroke-linecap="round" fill="none"/>
                <path d="M250 200 Q 230 290 220 380" stroke="#c084fc" stroke-width="16" stroke-linecap="round" fill="none"/>
                <path d="M350 200 Q 370 290 380 380" stroke="#c084fc" stroke-width="16" stroke-linecap="round" fill="none"/>
                <path d="M400 180 Q 420 260 430 350" stroke="#a855f7" stroke-width="14" stroke-linecap="round" fill="none"/>
            </g>
        </svg>
        """
    elif "الكريستال" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_cryst" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_cryst)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#334155"/>
            <rect x="270" y="280" width="60" height="200" fill="#0f172a" rx="10"/>
            <g class="animated-canopy">
                <polygon points="300,30 360,130 300,230 240,130" fill="#38bdf8" opacity="0.95"/>
                <polygon points="200,100 260,170 200,240 140,170" fill="#0284c7" opacity="0.95"/>
                <polygon points="400,100 460,170 400,240 340,170" fill="#7dd3fc" opacity="0.95"/>
            </g>
        </svg>
        """
    elif "البنساي" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_bonsai" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdf4ff"/><stop offset="100%" stop-color="#fae8ff"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_bonsai)"/>
            <!-- حوض نبات عتيق -->
            <path d="M180 430 L420 430 L400 480 L200 480 Z" fill="#78716c"/>
            <!-- جذع عتيق متلوّي بدقة يابانية -->
            <path d="M280 430 C200 380 380 250 260 170 C220 140 250 90 300 70 C350 90 380 160 300 220 Z" fill="#292524" stroke="#1c1917" stroke-width="5"/>
            <!-- وسائد أوراق البنساي المنسقة -->
            <g class="animated-canopy">
                <ellipse cx="300" cy="65" rx="70" ry="28" fill="#15803d"/>
                <ellipse cx="200" cy="140" rx="55" ry="22" fill="#16a34a"/>
                <ellipse cx="400" cy="160" rx="60" ry="22" fill="#15803d"/>
            </g>
        </svg>
        """
    elif "البامبو" in active:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_bamboo" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0fdf4"/><stop offset="100%" stop-color="#dcfce7"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_bamboo)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#bbf7d0"/>
            <!-- سيقان البامبو المتعددة -->
            <rect x="180" y="20" width="30" height="460" fill="#16a34a" rx="6"/><line x1="180" y1="130" x2="210" y2="130" stroke="#14532d" stroke-width="5"/><line x1="180" y1="260" x2="210" y2="260" stroke="#14532d" stroke-width="5"/><line x1="180" y1="390" x2="210" y2="390" stroke="#14532d" stroke-width="5"/>
            <rect x="280" y="0" width="40" height="480" fill="#15803d" rx="8"/><line x1="280" y1="110" x2="320" y2="110" stroke="#14532d" stroke-width="6"/><line x1="280" y1="230" x2="320" y2="230" stroke="#14532d" stroke-width="6"/><line x1="280" y1="350" x2="320" y2="350" stroke="#14532d" stroke-width="6"/>
            <rect x="380" y="50" width="25" height="430" fill="#22c55e" rx="5"/><line x1="380" y1="160" x2="405" y2="160" stroke="#16a34a" stroke-width="4"/><line x1="380" y1="300" x2="405" y2="300" stroke="#16a34a" stroke-width="4"/>
        </svg>
        """
    else:
        svg_tree_render = animation_styles + """
        <svg viewBox="0 0 600 500" width="100%" height="100%">
            <defs>
                <linearGradient id="sky_phoenix" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#18181b"/><stop offset="100%" stop-color="#27272a"/></linearGradient>
            </defs>
            <rect width="600" height="500" fill="url(#sky_phoenix)"/>
            <ellipse cx="300" cy="480" rx="280" ry="30" fill="#27272a"/>
            <path d="M270 480 L270 300 C270 240 250 190 200 160 C270 180 290 220 300 300 L300 480 Z" fill="#09090b"/>
            <g class="animated-canopy">
                <circle cx="300" cy="140" r="120" fill="#ef4444" opacity="0.95"/>
                <circle cx="300" cy="130" r="95" fill="#f97316" opacity="0.95"/>
                <circle cx="300" cy="110" r="65" fill="#fde047" opacity="0.95"/>
            </g>
        </svg>
        """

    # عرض الرسوم عبر مكونات HTML معزولة لضمان عمل الرسوم بدقة مذهلة
    components.html(f"""
    <div style="width: 100%; height: 480px; border-radius: 20px; overflow: hidden; border: 3px solid #334155; box-shadow: 0 15px 30px rgba(0,0,0,0.2); background: #fff;">
        {svg_tree_render}
    </div>
    """, height=490)

    st.markdown(f"### 🌲 الشجرة النشطة حالياً: **{active}**")
    st.info("✨ هذه الشجرة مصممة برسم هندسي عضوي وأنيميشن سينمائي عالي الجودة.")

    st.markdown("---")
    st.markdown("### 🛒 متجر الـ 10 أشجار الواقعية والأيقونية")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")

    trees_catalog = [
        {"name": "🌸 شجرة الساكورا اليابانية الساحرة", "price": 0, "env": "بيئة ربيعية زهرية"},
        {"name": "🌲 شجرة الصنوبر الثلجية", "price": 40, "env": "بيئة جبلية شتوية"},
        {"name": "🍄 شجرة الفطر الساحرة", "price": 70, "env": "بيئة غامضة مضيئة"},
        {"name": "🌴 شجرة النخيل الاستوائية", "price": 100, "env": "بيئة واحة مشمسة"},
        {"name": "🍁 شجرة القيقب الخريفية", "price": 130, "env": "بيئة خريفية دافئة"},
        {"name": "🔮 شجرة الويسترليا البنفسجية", "price": 160, "env": "بيئة أرجوانية ساحرة"},
        {"name": "💎 شجرة الكريستال البلورية", "price": 200, "env": "بيئة جليدية مشعة"},
        {"name": "🌿 شجرة البنساي العتيقة", "price": 240, "env": "بيئة صخرية يابانية"},
        {"name": "🎋 غابة البامبو الآسيوية", "price": 280, "env": "بيئة غابة هادئة"},
        {"name": "🔥 شجرة العنقاء النارية", "price": 350, "env": "بيئة طاقة أسطورية"}
    ]

    cols_shop = st.columns(3)
    for idx, t in enumerate(trees_catalog):
        with cols_shop[idx % 3]:
            st.markdown(f"**{t['name']}**")
            st.caption(f"🌍 {t['env']}")
            
            is_unlocked = t['name'] in st.session_state.unlocked_trees
            if is_unlocked:
                if active == t['name']:
                    st.success("✅ المفعلة حالياً")
                else:
                    if st.button("تفعيل", key=f"act_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                if st.button(f"شراء ({t['price']} ن)", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success("🎉 مبروك! تم التفعيل بنجاح!")
                        st.rerun()
                    else:
                        st.error("❌ النقاط غير كافية!")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 6: منصة الحكام والاستثمار ---
# ==========================================
with tab6:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🏛️ منطقة الحكام والاستثمار")
    
    st.markdown("""
    ### 📌 نبذة سريعة عن المشروع:
    نظام ذكي متكامل لقياس وتحليل الأنماط المعرفية والبيئية للطلاب، يدمج بين علم النفس العصبي والتفاعل البصري المتقدم لتعزيز التحصيل الدراسي.

    ---
    ### 💡 رؤية التطوير والاستثمار (لماذا هذا المشروع واعد؟):
    * **قابلية التخصيص الكامل:** المنصة مصممة بهندسة مرنة تتيح لكل مستخدم أو مؤسسة تخصيص بيئتها وتجربتها بالكامل.
    * **مرتكز للمطورين (Extensibility):** البنية البرمجية قابلة للدمج والتطوير المستمر بسهولة تامة.
    * **الفرصة الاستثمارية:** يمثل المنتج حلاً حقيقياً لأسواق التعليم الرقمي (EdTech) والصحة العقلية، بطلب استهلاكي مرتفع وقابلية توسع تجاري ضخمة (SaaS).
    """)
    st.success("✨ مشروع يعكس رؤية تقنية واستثمارية مستقبلية مستدامة.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
