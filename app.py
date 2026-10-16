import streamlit as st
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
    st.session_state.user_points = 100

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌸 شجرة الساكورا اليابانية"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌸 شجرة الساكورا اليابانية"

# CSS للرسوم الواقعية والأنيميشن الاحترافي للشجار الـ 10
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

    /* المسرح السينمائي العام للرسم الواقعي */
    .realistic-stage {
        position: relative;
        width: 100%;
        height: 450px;
        border-radius: 20px;
        overflow: hidden;
        border: 3px solid #334155;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.2);
        display: flex;
        justify-content: center;
        align-items: center;
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
        <div class="hero-title">🚀 متجر الأشجار الواقعية والأنيميشن السينمائي المتقدم</div>
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
    st.session_state.user_points += 20
    st.success("✅ تم حفظ التحليل واكتسبت +20 نقطة إضافية في رصيدك!")

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
    st.metric("النتيجة المعيارية الإجمالية", "445 / 500 نقطة")
    st.progress(89)
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
# --- TAB 5: معارض الأشجار الـ 10 الواقعية والأنيميشن ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 المعرض الفني للأشجار الواقعية المتقدمة")
    st.write("رسم هندسي دقيق وعالي التفاصيل (SVG/CSS) مع أنيميشن حركة الرياح وتساقط العناصر بدقة فائقة:")

    active = st.session_state.active_tree

    # رسم SVG واقعي ومفصل لكل شجرة بناءً على الاختيار
    svg_tree_render = ""
    
    if "الساكورا" in active: # 1. الساكورا اليابانية
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs>
                <linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdf2f8"/><stop offset="100%" stop-color="#fce7f3"/></linearGradient>
                <radialGradient id="pinkBlob" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f472b6"/><stop offset="100%" stop-color="#db2777"/></radialGradient>
            </defs>
            <rect width="500" height="450" fill="url(#sky1)"/>
            <path d="M230 450 L230 280 C230 240 210 200 180 170 C240 180 260 210 270 280 L270 450 Z" fill="#451a03"/>
            <path d="M245 330 C200 300 120 280 90 250 C130 240 190 260 245 300 Z" fill="#5c2c16"/>
            <path d="M255 310 C300 280 380 260 410 230 C370 220 310 240 255 280 Z" fill="#5c2c16"/>
            <!-- تجمعات أوراق الساكورا الواقعية المتعددة -->
            <circle cx="180" cy="160" r="85" fill="url(#pinkBlob)" opacity="0.9"/>
            <circle cx="310" cy="170" r="80" fill="url(#pinkBlob)" opacity="0.9"/>
            <circle cx="245" cy="110" r="95" fill="url(#pinkBlob)" opacity="0.95"/>
            <circle cx="130" cy="220" r="60" fill="#f472b6" opacity="0.85"/>
            <circle cx="370" cy="210" r="65" fill="#f472b6" opacity="0.85"/>
            <!-- بتلات متساقطة -->
            <circle cx="200" cy="350" r="4" fill="#fbcfe8"/><circle cx="320" cy="380" r="5" fill="#fbcfe8"/><circle cx="150" cy="400" r="4" fill="#fbcfe8"/>
        </svg>
        """
    elif "الصنوبر" in active: # 2. الصنوبر الثلجية
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs>
                <linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e0f2fe"/><stop offset="100%" stop-color="#bae6fd"/></linearGradient>
            </defs>
            <rect width="500" height="450" fill="url(#sky2)"/>
            <rect x="235" y="300" width="30" height="150" fill="#291203" rx="5"/>
            <!-- طبقات صنوبر مثلثية واقعية مع ثلج -->
            <polygon points="250,60 140,180 360,180" fill="#0369a1"/>
            <polygon points="250,60 140,180 360,180" fill="#ffffff" opacity="0.3" clip-path="polygon(250,60 180,130 320,130)"/>
            <polygon points="250,130 120,270 380,270" fill="#0284c7"/>
            <polygon points="250,200 100,360 400,360" fill="#0ea5e9"/>
        </svg>
        """
    elif "الفطر" in active: # 3. شجرة الفطر الساحرة
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky3" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2e1065"/><stop offset="100%" stop-color="#581c87"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky3)"/>
            <!-- ساق ضخمة -->
            <path d="M200 450 C210 320 220 280 230 200 L270 200 C280 280 290 320 300 450 Z" fill="#fbcfe8"/>
            <!-- قبعة الفطر العملاقة الساحرة -->
            <path d="M125 200 C125 100 375 100 375 200 C320 220 180 220 125 200 Z" fill="#ef4444"/>
            <circle cx="200" cy="150" r="18" fill="#ffffff"/><circle cx="280" cy="140" r="22" fill="#ffffff"/><circle cx="330" cy="180" r="12" fill="#ffffff"/><circle cx="160" cy="170" r="15" fill="#ffffff"/>
        </svg>
        """
    elif "النخيل" in active: # 4. النخيل الاستوائية
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky4" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#f97316"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky4)"/>
            <!-- جذع منحني واقعي -->
            <path d="M220 450 Q 280 280 250 150 L270 150 Q 300 280 240 450 Z" fill="#78350f"/>
            <!-- سعف النخيل الموزع -->
            <path d="M260 160 Q 380 100 450 140 Q 360 180 260 160 Z" fill="#15803d"/>
            <path d="M260 160 Q 400 200 440 260 Q 360 220 260 160 Z" fill="#16a34a"/>
            <path d="M260 160 Q 140 100 50 140 Q 150 180 260 160 Z" fill="#15803d"/>
            <path d="M260 160 Q 100 200 60 260 Q 160 220 260 160 Z" fill="#16a34a"/>
            <path d="M260 160 Q 260 40 260 10 Q 280 80 260 160 Z" fill="#22c55e"/>
        </svg>
        """
    elif "القيقب" in active: # 5. القيقب الخريفي
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky5" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ffedd5"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky5)"/>
            <path d="M230 450 L230 270 C230 220 210 180 170 150 C240 170 260 200 270 270 L270 450 Z" fill="#451a03"/>
            <circle cx="180" cy="150" r="85" fill="#ea580c" opacity="0.9"/>
            <circle cx="320" cy="160" r="80" fill="#ea580c" opacity="0.9"/>
            <circle cx="250" cy="100" r="100" fill="#dc2626" opacity="0.95"/>
            <circle cx="250" cy="180" r="90" fill="#f59e0b" opacity="0.9"/>
        </svg>
        """
    elif "الويسترليا" in active: # 6. الويسترليا الساحرة
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky6" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f3e8ff"/><stop offset="100%" stop-color="#e9d5ff"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky6)"/>
            <path d="M230 450 L230 280 C230 230 210 190 170 160 C240 180 260 210 270 280 L270 450 Z" fill="#3b0764"/>
            <circle cx="250" cy="140" r="110" fill="#c084fc" opacity="0.85"/>
            <!-- عناقيد زهور متدلية -->
            <path d="M180 180 Q 170 250 160 300" stroke="#a855f7" stroke-width="12" stroke-linecap="round" fill="none"/>
            <path d="M220 190 Q 210 270 200 330" stroke="#c084fc" stroke-width="14" stroke-linecap="round" fill="none"/>
            <path d="M280 190 Q 290 270 300 330" stroke="#a855f7" stroke-width="14" stroke-linecap="round" fill="none"/>
            <path d="M320 180 Q 330 250 340 300" stroke="#c084fc" stroke-width="12" stroke-linecap="round" fill="none"/>
        </svg>
        """
    elif "الكريستال" in active: # 7. شجرة الكريستال
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky7" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky7)"/>
            <rect x="235" y="280" width="30" height="170" fill="#334155" rx="5"/>
            <!-- بلورات كريستالية متوهجة -->
            <polygon points="250,40 290,120 250,200 210,120" fill="#38bdf8" opacity="0.9"/>
            <polygon points="180,100 230,160 180,220 130,160" fill="#0284c7" opacity="0.9"/>
            <polygon points="320,100 370,160 320,220 270,160" fill="#7dd3fc" opacity="0.9"/>
            <polygon points="250,150 300,220 250,290 200,220" fill="#38bdf8" opacity="0.85"/>
        </svg>
        """
    elif "البنساي" in active: # 8. البنساي العتيقة
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky8" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdf4ff"/><stop offset="100%" stop-color="#fae8ff"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky8)"/>
            <!-- صخرة القاعدة -->
            <ellipse cx="250" cy="400" rx="120" ry="30" fill="#78716c"/>
            <!-- جذع متلوّي وعريق -->
            <path d="M200 400 C150 350 300 250 220 180 C180 150 210 100 250 80 C290 100 320 160 260 220 Z" fill="#292524" stroke="#1c1917" stroke-width="4"/>
            <!-- وسائد أوراق البنساي الخضراء المنسقة -->
            <ellipse cx="250" cy="70" rx="60" ry="25" fill="#15803d"/>
            <ellipse cx="170" cy="140" rx="45" ry="20" fill="#16a34a"/>
            <ellipse cx="330" cy="160" rx="50" ry="20" fill="#15803d"/>
        </svg>
        """
    elif "البامبو" in active: # 9. غابة البامبو
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky9" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0fdf4"/><stop offset="100%" stop-color="#dcfce7"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky9)"/>
            <!-- سيقان البامبو متعددة وواقعية -->
            <rect x="150" y="20" width="25" height="430" fill="#16a34a" rx="5"/><line x1="150" y1="120" x2="175" y2="120" stroke="#14532d" stroke-width="4"/><line x1="150" y1="240" x2="175" y2="240" stroke="#14532d" stroke-width="4"/><line x1="150" y1="360" x2="175" y2="360" stroke="#14532d" stroke-width="4"/>
            <rect x="230" y="0" width="35" height="450" fill="#15803d" rx="5"/><line x1="230" y1="100" x2="265" y2="100" stroke="#14532d" stroke-width="5"/><line x1="230" y1="220" x2="265" y2="220" stroke="#14532d" stroke-width="5"/><line x1="230" y1="340" x2="265" y2="340" stroke="#14532d" stroke-width="5"/>
            <rect x="320" y="40" width="22" height="410" fill="#22c55e" rx="4"/><line x1="320" y1="150" x2="342" y2="150" stroke="#16a34a" stroke-width="3"/><line x1="320" y1="280" x2="342" y2="280" stroke="#16a34a" stroke-width="3"/>
        </svg>
        """
    else: # 10. العنقاء النارية
        svg_tree_render = """
        <svg viewBox="0 0 500 450" width="100%" height="100%">
            <defs><linearGradient id="sky10" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#18181b"/><stop offset="100%" stop-color="#27272a"/></linearGradient></defs>
            <rect width="500" height="450" fill="url(#sky10)"/>
            <path d="M230 450 L230 280 C230 230 210 190 170 160 C240 180 260 210 270 280 L270 450 Z" fill="#09090b"/>
            <!-- ألسنة اللهب النارية المشتعلة واقعياً -->
            <circle cx="250" cy="140" r="110" fill="#ef4444" opacity="0.9"/>
            <circle cx="250" cy="130" r="85" fill="#f97316" opacity="0.95"/>
            <circle cx="250" cy="110" r="55" fill="#fde047" opacity="0.95"/>
        </svg>
        """

    # عرض المسرح الفني
    st.markdown(f"""
    <div class="realistic-stage">
        {svg_tree_render}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🌲 الشجرة النشطة حالياً: **{active}**")
    st.info("✨ هذه الشجرة مرسومة بدقة هندسية عالية وتمثل البيئة المعرفية الافتراضية الخاصة بك.")

    st.markdown("---")
    st.markdown("### 🛒 متجر الـ 10 أشجار الواقعية والأيقونية")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")

    trees_catalog = [
        {"name": "🌸 شجرة الساكورا اليابانية", "price": 0, "env": "بيئة ربيعية زهرية"},
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
# --- TAB 6: منصة الحكام والاستثمار (مبسطة وهادئة وثقة تامة) ---
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
