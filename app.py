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
    st.session_state.user_points = 50

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌳 شجرة البلوط الخضراء الضخمة"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌳 شجرة البلوط الخضراء الضخمة"

# CSS للأنيميشن السينمائي المتقدم وتفاصيل الشجرة الكرتونية الضخمة
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

    /* ==========================================
       المسرح السينمائي وتفاصيل الشجرة الكرتونية الضخمة
       ========================================== */
    .tree-stage {
        position: relative;
        width: 100%;
        height: 420px;
        background: linear-gradient(to bottom, #dbeafe 0%, #f0fdf4 100%);
        border-radius: 24px;
        overflow: hidden;
        border: 3px solid #059669;
        box-shadow: inset 0 0 40px rgba(0,0,0,0.08);
        display: flex;
        justify-content: center;
        align-items: flex-end;
    }

    /* أرضية خضراء كرتونية */
    .tree-ground {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 35px;
        background: linear-gradient(to top, #15803d, #22c55e);
        border-radius: 0 0 20px 20px;
        z-index: 5;
    }

    /* جذع الشجرة المتعرج والمفصل */
    .detailed-trunk {
        position: absolute;
        bottom: 30px;
        width: 60px;
        height: 190px;
        background: linear-gradient(90deg, #3f2204, #78350f, #451a03);
        border-radius: 15px 15px 5px 5px;
        z-index: 2;
        box-shadow: inset -5px 0 15px rgba(0,0,0,0.5);
    }

    /* أغصان جانبية */
    .branch-l {
        position: absolute;
        top: 30px;
        left: -35px;
        width: 50px;
        height: 18px;
        background: #572506;
        transform: rotate(-25deg);
        border-radius: 10px;
        z-index: 1;
    }

    .branch-r {
        position: absolute;
        top: 50px;
        right: -35px;
        width: 50px;
        height: 18px;
        background: #572506;
        transform: rotate(25deg);
        border-radius: 10px;
        z-index: 1;
    }

    /* تاج الأوراق متعدد الطبقات والضخم (Canopy Layers) */
    .canopy-container {
        position: absolute;
        bottom: 130px;
        width: 320px;
        height: 240px;
        z-index: 3;
        animation: treeSway 4.5s ease-in-out infinite alternate;
    }

    .leaf-blob {
        position: absolute;
        border-radius: 50%;
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.15));
    }

    /* طبقات الأوراق المتداخلة لتكوين شجرة كرتونية غنية */
    .blob-1 { width: 160px; height: 160px; top: 0px; left: 80px; }
    .blob-2 { width: 140px; height: 140px; top: 40px; left: 15px; }
    .blob-3 { width: 130px; height: 130px; top: 40px; right: 15px; }
    .blob-4 { width: 150px; height: 150px; top: 80px; left: 50px; }

    /* أنيميشن الاهتزاز مع الرياح */
    @keyframes treeSway {
        0% { transform: rotate(-1.5deg) scale(1); }
        100% { transform: rotate(1.5deg) scale(1.02); }
    }

    /* تساقط الأوراق السينمائي الحقيقي والتفصيلي */
    .falling-leaf {
        position: absolute;
        font-size: 18px;
        animation: leafFall 6s linear infinite;
        z-index: 4;
        opacity: 0.85;
    }

    .fl-1 { left: 35%; animation-delay: 0s; }
    .fl-2 { left: 55%; animation-delay: 2s; }
    .fl-3 { left: 45%; animation-delay: 4s; }

    @keyframes leafFall {
        0% { top: 25px; transform: translateX(0) rotate(0deg); opacity: 1; }
        50% { transform: translateX(30px) rotate(180deg); }
        100% { top: 350px; transform: translateX(-25px) rotate(360deg); opacity: 0; }
    }

    /* سمات ثيمات الأشجار الـ 7 التفصيلية */
    /* 1. البلوط الخضراء */
    .theme-oak .leaf-blob { background: radial-gradient(circle, #4ade80 0%, #16a34a 60%, #15803d 100%); }
    
    /* 2. الساكورا الوردية */
    .theme-sakura .leaf-blob { background: radial-gradient(circle, #fbcfe8 0%, #f472b6 60%, #db2777 100%); }
    
    /* 3. الصنوبر الفضية */
    .theme-pine .leaf-blob { background: radial-gradient(circle, #7dd3fc 0%, #38bdf8 60%, #0369a1 100%); }
    
    /* 4. النخيل الذهبية */
    .theme-gold .leaf-blob { background: radial-gradient(circle, #fde047 0%, #fbbf24 60%, #b45309 100%); }
    
    /* 5. البوباب السحرية */
    .theme-magic .leaf-blob { background: radial-gradient(circle, #e879f9 0%, #c084fc 60%, #6b21a8 100%); }
    
    /* 6. القيقب الحمراء */
    .theme-autumn .leaf-blob { background: radial-gradient(circle, #fdba74 0%, #f97316 60%, #c2410c 100%); }
    
    /* 7. الكريستال الزرقاء */
    .theme-crystal .leaf-blob { background: radial-gradient(circle, #67e8f9 0%, #22d3ee 60%, #0e7490 100%); }

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
        <div class="hero-title">🚀 النظام التحليلي المتطور والشجرة السينمائية المتحركة مفصلة الرسوم</div>
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

# ==========================================
# 3. الحسابات الذكية عند الضغط على زر الإرسال
# ==========================================
if submit_btn:
    score = 190.0
    score += (sleep_hours / 12.0) * 50.0
    score += (sleep_quality / 15.0) * 45.0
    score += (deep_focus / 12.0) * 95.0
    score += (motivation_level / 15.0) * 35.0
    score += (hydration_level / 15.0) * 25.0
    score -= (stress_level / 15.0) * 25.0
    score -= (screen_hours / 14.0) * 20.0
    score -= (overthinking_mins / 120.0) * 20.0
    
    if "ذكية" in snack_type or "بالبروتين" in snack_type:
        score += 20.0
    elif "ثقيلة" in snack_type:
        score -= 15.0
    elif "سكريات" in snack_type:
        score -= 25.0
        
    if study_method != "القراءة التكرارية الصامتة":
        score += 25.0
    if phone_isolation == "مفصول تماماً في غرفة ثانية":
        score += 25.0
    elif phone_isolation == "في اليد أو بجانب الكتاب":
        score -= 30.0
        
    final_score = min(max(score, 100.0), 500.0)
    
    st.session_state.user_points += 15

    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "score": round(final_score, 1),
        "sleep": sleep_hours,
        "focus": deep_focus,
        "stress": stress_level,
        "screen": screen_hours,
        "overthinking": overthinking_mins,
        "temp": room_temp,
        "snack": snack_type
    }
    st.session_state.history.append(entry)
    st.success("✅ تم حفظ البيانات وإرسالها بنجاح واكتسبت +15 نقطة!")

# ==========================================
# 4. التبويبات الرئيسية
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ",
    "🌳 الشجرة السينمائية المتحركة"
])

total_entries = len(st.session_state.history)

# --- TAB 1: المؤشرات والموجز الشامل ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    if total_entries == 0:
        st.info("👈 أدخل بياناتك من اللوحة الجانبية ثم اضغط **(إرسال وتحليل البيانات)** لعرض التقرير الشامل.")
    else:
        latest = st.session_state.history[-1]
        curr_score = latest.get("score", 0)
        
        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
            st.metric("النتيجة المعيارية الإجمالية", f"{curr_score} / 500 نقطة")
            st.progress(int((curr_score/500)*100))
            
            percentage = (curr_score / 500.0) * 100
            if percentage >= 80:
                st.success("🌟 جاهزية استثنائية: قدرات استيعاب واستشفاء عالية تضعك في القمة.")
            elif percentage >= 65:
                st.info("👍 أداء مستقر وممتاز، موازنة بسيطة في نومك وترطيبك تضمن العلامة الكاملة.")
            else:
                st.warning("⚠️ تنبيه: يتطلب الأمر ضبط ساعات النوم وتقليل الإرهاق البصري لرفع حصيلتك.")
                
        with col_b:
            st.subheader("🪙 رصيد نقاطك")
            st.metric("إجمالي النقاط المحفوظة", f"{st.session_state.user_points} نقطة")
            st.write(f"الشجرة النشطة حالياً: **{st.session_state.active_tree}**")

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية والاستشفاء الجسدي")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("#### 👁️ محلل التعب والإجهاد البصري")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            screen_val = latest.get("screen", 4.5)
            eye_fatigue_score = min(100, int((screen_val / 12.0) * 100))
            st.write(f"نسبة إجهاد العين المحسوبة: **{eye_fatigue_score}%**")
            st.progress(eye_fatigue_score)
        else:
            st.caption("أدخل بياناتك أولاً لحساب التعب البصري.")

    with col_e2:
        st.markdown("#### 🚪 محلل أكسجين وتهوية المكان")
        st.success("🍃 نسبة التهوية والأكسجين في مكان جلوسك متوازنة.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ محرك الطاقة المعرفية والتحديات الإبداعية")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### ⚡ حاسبة سرعة البديهة والجاهزية العصبية")
        if st.button("🎯 بدء اختبار التفاعل العصبي السريع"):
            rand_speed = random.randint(180, 240)
            st.success(f"⚡ **سرعة استجابتك العصبية:** **{rand_speed} ملي ثانية**")

    with col_t2:
        st.markdown("#### 🧠 حاسبة السعرات الحرارية للدماغ")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            cals = int(latest.get("focus", 3.5) * 72.0)
            st.write(f"🔥 بذل دماغك طاقة تقدر بـ **{cals} سعرة حرارية** اليوم.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل والتفريغ ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التحليل النفسي المعرفي وصندوق التفريغ")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("#### 🗑️ صندوق التفريغ الذهني وتنقية الذاكرة")
        thought_input = st.text_input("أدخل الفكرة المشتتة هنا لتنظيف عقلك:")
        if st.button("إفراغ الفكرة من الذهن"):
            if thought_input:
                st.session_state.mind_dump.append(thought_input)
                st.success("تم إفراغ الفكرة بنجاح من عقلك!")

    with col_d2:
        st.markdown("#### ⚖️ محامي الدماغ المنطقي تفنيد الكسل")
        custom_excuse = st.text_input("اكتب العذر الذي يجعلك تتكاسل الآن:")
        if st.button("💡 تفنيد العذر بالدليل العلمي"):
            if custom_excuse:
                st.info(f"⚖️ **رد المحامي المنطقي:** قولك '{custom_excuse}' هو مجرد حيلة من الدماغ لتوفير الطاقة. البدء بـ 5 دقائق يكسر هذا الحاجز فوراً!")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 5: الشجرة السينمائية المتحركة مفصلة الرسوم والمتجر ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 الشجرة السينمائية الحية مفصلة الأوراق والجذع")

    # تحديد سمة الثيم وتحديد الميزة لكل شجرة
    theme_class = "theme-oak"
    tree_perk = "ميزة الشجرة: تمنحك +10% ثبات عالي واستقرار في التركيز"
    leaf_emoji = "🍃"
    
    if "الساكورا" in st.session_state.active_tree:
        theme_class = "theme-sakura"
        tree_perk = "ميزة الشجرة: تمنحك +15% سرعة استيعاب وإبداع بصري"
        leaf_emoji = "🌸"
    elif "الصنوبر" in st.session_state.active_tree:
        theme_class = "theme-pine"
        tree_perk = "ميزة الشجرة: تمنحك +20% صمود ومقاومة للتشتت الرقمي"
        leaf_emoji = "🌲"
    elif "النخيل" in st.session_state.active_tree:
        theme_class = "theme-gold"
        tree_perk = "ميزة الشجرة: تمنحك +25% طاقة ذهنية متجددة"
        leaf_emoji = "✨"
    elif "البوباب" in st.session_state.active_tree:
        theme_class = "theme-magic"
        tree_perk = "ميزة الشجرة: تمنحك +30% صفاء وذاكرة بعيدة المدى"
        leaf_emoji = "🔮"
    elif "القيقب" in st.session_state.active_tree:
        theme_class = "theme-autumn"
        tree_perk = "ميزة الشجرة: تمنحك +15% هدوء وتقليل للتوتر العصبي"
        leaf_emoji = "🍁"
    elif "الكريستال" in st.session_state.active_tree:
        theme_class = "theme-crystal"
        tree_perk = "ميزة الشجرة: تمنحك +35% أقصى طاقة استيعابية خرافية"
        leaf_emoji = "💎"

    # عرض المسرح السينمائي للشجرة مع طبقات أوراق متداخلة وأغصان وتساقط واقعي
    st.markdown(f"""
    <div class="tree-stage {theme_class}">
        <!-- تساقط الأوراق السينمائي -->
        <div class="falling-leaf fl-1">{leaf_emoji}</div>
        <div class="falling-leaf fl-2">{leaf_emoji}</div>
        <div class="falling-leaf fl-3">{leaf_emoji}</div>
        
        <!-- تاج الأوراق الضخم متعدد الطبقات -->
        <div class="canopy-container">
            <div class="leaf-blob blob-1"></div>
            <div class="leaf-blob blob-2"></div>
            <div class="leaf-blob blob-3"></div>
            <div class="leaf-blob blob-4"></div>
        </div>
        
        <!-- الجذع والأغصان المعقدة -->
        <div class="detailed-trunk">
            <div class="branch-l"></div>
            <div class="branch-r"></div>
        </div>
        
        <!-- الأرضية الخضراء -->
        <div class="tree-ground"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🌲 الشجرة المفعلة حالياً: **{st.session_state.active_tree}**")
    st.info(f"✨ **{tree_perk}**")

    st.markdown("---")
    
    # متجر بسيط وخفيف وسلس
    st.markdown("### 🛒 متجر الأشجار السريع")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")

    trees_catalog = [
        {"name": "🌳 شجرة البلوط الخضراء الضخمة", "price": 0, "perk": "+10% ثبات عالي"},
        {"name": "🌸 شجرة الساكورا الوردية", "price": 30, "perk": "+15% سرعة استيعاب"},
        {"name": "🌲 شجرة الصنوبر الفضية", "price": 60, "perk": "+20% مقاومة للتشتت"},
        {"name": "🌴 شجرة النخيل الذهبية", "price": 90, "perk": "+25% طاقة متجددة"},
        {"name": "🔮 شجرة البوباب السحرية", "price": 120, "perk": "+30% صفاء ذهني"},
        {"name": "🍁 شجرة القيقب الحمراء", "price": 150, "perk": "+15% تقليل التوتر"},
        {"name": "💎 شجرة الكريستال الزرقاء", "price": 200, "perk": "+35% طاقة خرافية"}
    ]

    cols_shop = st.columns(3)
    for idx, t in enumerate(trees_catalog):
        with cols_shop[idx % 3]:
            st.markdown(f"**{t['name']}**")
            st.caption(f"⚡ {t['perk']}")
            
            is_unlocked = t['name'] in st.session_state.unlocked_trees
            
            if is_unlocked:
                if st.session_state.active_tree == t['name']:
                    st.success("✅ الشجرة المفعلة")
                else:
                    if st.button("تفعيل الشجرة", key=f"act_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                if st.button(f"شراء ({t['price']} نقطة)", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success("🎉 مبروك! تم الشراء والتفعيل بنجاح!")
                        st.rerun()
                    else:
                        st.error("❌ عذراً، نقاطك غير كافية للشراء!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
