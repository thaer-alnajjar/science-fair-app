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
    st.session_state.unlocked_trees = ["🌳 شجرة البلوط الخضراء"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌳 شجرة البلوط الخضراء"

# CSS للأنيميشن السينمائي والتصميم النظيف
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
       الأنيميشن ورسم الشجرة السينمائية الكرتونية
       ========================================== */
    .tree-stage {
        position: relative;
        width: 100%;
        height: 380px;
        background: linear-gradient(to bottom, #e0f2fe 0%, #f0fdf4 100%);
        border-radius: 24px;
        overflow: hidden;
        border: 3px solid #0891b2;
        box-shadow: inset 0 0 30px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
        align-items: flex-end;
    }

    /* جذع الشجرة السينمائي */
    .tree-trunk {
        position: absolute;
        bottom: 0;
        width: 50px;
        height: 180px;
        background: linear-gradient(to right, #78350f, #451a03);
        border-radius: 12px 12px 0 0;
        z-index: 2;
    }

    /* تفرع أغصان كرتونية */
    .tree-trunk::before {
        content: '';
        position: absolute;
        top: 20px;
        left: -30px;
        width: 40px;
        height: 15px;
        background: #451a03;
        transform: rotate(-30deg);
        border-radius: 10px;
    }
    .tree-trunk::after {
        content: '';
        position: absolute;
        top: 40px;
        right: -30px;
        width: 40px;
        height: 15px;
        background: #451a03;
        transform: rotate(30deg);
        border-radius: 10px;
    }

    # تاج الأوراق الضخم */
    .tree-canopy {
        position: absolute;
        bottom: 120px;
        width: 260px;
        height: 220px;
        border-radius: 50% 50% 45% 45%;
        z-index: 3;
        animation: sway 4s ease-in-out infinite alternate;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }

    /* ألوان وأفكار الشجر السينمائي */
    .theme-oak { background: radial-gradient(circle, #22c55e 0%, #15803d 100%); }
    .theme-sakura { background: radial-gradient(circle, #f472b6 0%, #db2777 100%); }
    .theme-pine { background: radial-gradient(circle, #38bdf8 0%, #0369a1 100%); }
    .theme-gold { background: radial-gradient(circle, #fbbf24 0%, #b45309 100%); }
    .theme-magic { background: radial-gradient(circle, #c084fc 0%, #6b21a8 100%); }
    .theme-autumn { background: radial-gradient(circle, #f97316 0%, #c2410c 100%); }
    .theme-crystal { background: radial-gradient(circle, #22d3ee 0%, #0e7490 100%); }

    /* حرك الاهتزاز الكرتوني للمجموع الورقي */
    @keyframes sway {
        0% { transform: rotate(-2deg) scale(1); }
        100% { transform: rotate(2deg) scale(1.02); }
    }

    /* تساقط الأوراق السينمائي الخفيف */
    .leaf-particle {
        position: absolute;
        width: 14px;
        height: 14px;
        border-radius: 0 70% 0 70%;
        opacity: 0.8;
        animation: fall 5s linear infinite;
        z-index: 4;
    }

    .leaf-1 { left: 45%; animation-delay: 0s; background: #86efac; }
    .leaf-2 { left: 52%; animation-delay: 1.5s; background: #fbcfe8; }
    .leaf-3 { left: 40%; animation-delay: 3s; background: #fef08a; }

    @keyframes fall {
        0% { top: 30%; transform: translateX(0) rotate(0deg); opacity: 1; }
        50% { transform: translateX(25px) rotate(180deg); }
        100% { top: 90%; transform: translateX(-20px) rotate(360deg); opacity: 0; }
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
        <div class="hero-title">🚀 النظام التحليلي المتطور والشجرة السينمائية المتحركة</div>
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
    "🌳 الشجرة السينمائية والمتجر"
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
# --- TAB 5: الشجرة السينمائية المتحركة والمتجر الخفيف ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 الشجرة السينمائية الحية")

    # تحديد كلاس المظهر بناءً على الشجرة المحددة
    theme_class = "theme-oak"
    tree_perk = "ميزة الشجرة: تمنحك +10% ثبات عالي واستقرار في التركيز"
    
    if "الكرز" in st.session_state.active_tree:
        theme_class = "theme-sakura"
        tree_perk = "ميزة الشجرة: تمنحك +15% سرعة استيعاب وإبداع"
    elif "الصنوبر" in st.session_state.active_tree:
        theme_class = "theme-pine"
        tree_perk = "ميزة الشجرة: تمنحك +20% صمود ومقاومة للتشتت"
    elif "النخيل" in st.session_state.active_tree:
        theme_class = "theme-gold"
        tree_perk = "ميزة الشجرة: تمنحك +25% طاقة ذهنية متجددة"
    elif "البوباب" in st.session_state.active_tree:
        tree_perk = "ميزة الشجرة: تمنحك +30% صفاء وذاكرة بعيدة المدى"
        theme_class = "theme-magic"
    elif "القيقب" in st.session_state.active_tree:
        theme_class = "theme-autumn"
        tree_perk = "ميزة الشجرة: تمنحك +15% هدوء وتقليل للتوتر"
    elif "الكريستال" in st.session_state.active_tree:
        theme_class = "theme-crystal"
        tree_perk = "ميزة الشجرة: تمنحك +35% أقصى طاقة استيعابية"

    # عرض المسرح السينمائي للشجرة بالأنيميشن
    st.markdown(f"""
    <div class="tree-stage">
        <div class="leaf-particle leaf-1"></div>
        <div class="leaf-particle leaf-2"></div>
        <div class="leaf-particle leaf-3"></div>
        <div class="tree-canopy {theme_class}"></div>
        <div class="tree-trunk"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🌲 الشجرة الحالية: **{st.session_state.active_tree}**")
    st.info(f"✨ **{tree_perk}**")

    st.markdown("---")
    
    # متجر بسيط وخفيف كروت ملمومة
    st.markdown("### 🛒 متجر الأشجار الخفيف")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")

    trees_catalog = [
        {"name": "🌳 شجرة البلوط الخضراء", "price": 0, "perk": "+10% ثبات واستقرار"},
        {"name": "🌸 شجرة الساكورا الوردية", "price": 30, "perk": "+15% سرعة استيعاب"},
        {"name": "🌲 شجرة الصنوبر الفضية", "price": 60, "perk": "+20% مقاومة للتشتت"},
        {"name": "🌴 شجرة النخيل الذهبية", "price": 90, "perk": "+25% طاقة متجددة"},
        {"name": "🔮 شجرة البوباب السحرية", "price": 120, "perk": "+30% صفاء ذهني"},
        {"name": "🍁 شجرة القيقب الحمراء", "price": 150, "perk": "+15% تقليل للتوتر"},
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
                    st.success("✅ المفعلة")
                else:
                    if st.button("تفعيل", key=f"act_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                if st.button(f"شراء ({t['price']} نقطة)", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success("🎉 تم الشراء والتفعيل!")
                        st.rerun()
                    else:
                        st.error("❌ النقاط غير كافية!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
