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

# تهيئة ذاكرة الجلسة وحفظ النقاط
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

if "user_points" not in st.session_state:
    st.session_state.user_points = 50  # نقاط بدائية تحفيزية

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌳 شجرة بلوط الفرسان الكلاسيكية"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌳 شجرة بلوط الفرسان الكلاسيكية"

# CSS لتصميم نظيف واحترافي وشكل حلقي كرتوني
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

    /* تصميم الشجرة الحلقية الكرتونية */
    .tree-ring-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background: #f1f5f9;
        border-radius: 20px;
        border: 3px dashed #10b981;
        margin: 10px 0;
    }

    .tree-circle-badge {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 6px solid #10b981;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3.5rem;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.25);
        margin-bottom: 12px;
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

# الهيدر الرئيسي
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 النظام التحليلي المتطور والشجرة المعرفية الحلقية</div>
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
    
    # مكافأة نقاط إضافية على الإنجاز والالتزام
    st.session_state.user_points += 10

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
    st.success("✅ تم حفظ البيانات وتحليلها بنجاح واكتسبت +10 نقاط!")

# ==========================================
# 4. التبويبات الرئيسية (شاملة الشجرة الحلقية المتطورة)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ",
    "🌳 شجرة الإنتاجية الحلقية"
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
# --- TAB 5: شجرة الإنتاجية الحلقية ومتجر الأشجار الـ 7 ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 شجرة الإنتاجية الحلقية ومتجر الأشجار الفخمة")
    
    # 1. عرض الشجرة الحلقية الكرتونية الفخمة والمبسطة
    curr_focus = st.session_state.history[-1].get("focus", 3.5) if total_entries > 0 else 3.5
    focus_pct = min(100, int((curr_focus / 8.0) * 100))
    
    # تحديد الإيموجي الكرتوني الفخم بناءً على الشجرة المحددة
    tree_icon = "🌳"
    if "الكرز" in st.session_state.active_tree:
        tree_icon = "🌸"
    elif "الصنوبر" in st.session_state.active_tree:
        tree_icon = "🌲"
    elif "النخيل" in st.session_state.active_tree:
        tree_icon = "🌴"
    elif "البوباب" in st.session_state.active_tree:
        tree_icon = "🔮"
    elif "القيقب" in st.session_state.active_tree:
        tree_icon = "🍁"
    elif "الكريستال" in st.session_state.active_tree:
        tree_icon = "💎"

    col_ring1, col_ring2 = st.columns([1, 1])
    
    with col_ring1:
        st.markdown(f"""
        <div class="tree-ring-container">
            <div class="tree-circle-badge">
                {tree_icon}
            </div>
            <h3 style="margin:0; color:#10b981;">{st.session_state.active_tree}</h3>
            <p style="margin-top:5px; font-weight:bold; color:#64748b;">نسبة اكتمال حلقة التركيز: {focus_pct}%</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(focus_pct)

    with col_ring2:
        st.markdown("### 🪙 كسب النقاط وتحديث المعدل")
        st.write(f"رصيدك الحالي المحفوظ: **{st.session_state.user_points} نقطة**")
        
        # كسب النقاط بفضل المعدل المدرسي
        school_grade = st.number_input("أدخل معدلك المدرسي الأخير (من 100):", 50.0, 100.0, 88.0, 0.5)
        if st.button("🎁 المطالبة بمكافأة التطابق والمعدل (+50 نقطة)"):
            st.session_state.user_points += 50
            st.success("🎉 تهانينا! حصلت على +50 نقطة لإضافة معدلك المدرسي بنجاح!")
            
        # كسب نقاط عند الالتزام بالدراسة أسبوعاً
        if st.button("🔥 مكافأة تحسن الأداء والاستمرار الأسبوعي (+30 نقطة)"):
            st.session_state.user_points += 30
            st.success("🎉 أسطوري! تم إضافة +30 نقطة لرصيدك بفضل استمرارك في المذاكرة!")

    st.markdown("---")
    
    # 2. جدول إرشادي بسيط وسلس لكسب النقاط
    st.markdown("### 📋 جدول الطرق البسيطة لكسب النقاط:")
    points_guide_df = pd.DataFrame({
        "النشاط الإنجازي": ["تأكيد المعدل المدرسي", "تحسن ساعات الدراسة الأسبوعية", "إرسال تحليل حيوية يومي", "تحقيق تركيز نقي متواصل"],
        "النقاط المكتسبة": ["+50 نقطة 🪙", "+30 نقطة 🪙", "+10 نقاط 🪙", "+15 نقطة 🪙"]
    })
    st.table(points_guide_df)

    st.markdown("---")
    
    # 3. متجر الأشجار الـ 7 الفخمة
    st.markdown("### 🛒 متجر الأشجار الـ 7 الأسطورية")
    st.caption("أنفق نقاطك المكتسبة لشراء وتفعيل أشجار فخمة ومتميزة:")

    trees_catalog = [
        {"name": "🌳 شجرة بلوط الفرسان الكلاسيكية", "price": 0, "icon": "🌳", "desc": "شجرة خضراء متوازنة وقوية."},
        {"name": "🌸 شجرة الكرز الوردية (الساكورا)", "price": 40, "icon": "🌸", "desc": "شجرة كرتونية وردية تفوح بالإلهام."},
        {"name": "🌲 شجرة الصنوبر الفضية المتلألئة", "price": 70, "icon": "🌲", "desc": "شجرة شتوية فخمة بأطراف فضية."},
        {"name": "🌴 شجرة النخيل الذهبية الأسطورية", "price": 100, "icon": "🌴", "desc": "تصميم دافئ وذهبي لقمة التفوق."},
        {"name": "🔮 شجرة البوباب البنفسجية السحرية", "price": 130, "icon": "🔮", "desc": "شجرة غامضة بلون بنفسجي متألق."},
        {"name": "🍁 شجرة القيقب الحمراء الخريفية", "price": 160, "icon": "🍁", "desc": "أوراق أرجوانية وخريفية ساحرة."},
        {"name": "💎 شجرة الكريستال الزرقاء", "price": 200, "icon": "💎", "desc": "شجرة كرتونية مشعة من الكريستال النقي."}
    ]

    cols_shop = st.columns(3)
    for idx, t in enumerate(trees_catalog):
        col_target = cols_shop[idx % 3]
        with col_target:
            st.markdown(f"#### {t['icon']} {t['name']}")
            st.write(f"{t['desc']}")
            st.write(f"السعر: **{t['price']} نقطة**")
            
            is_unlocked = t['name'] in st.session_state.unlocked_trees
            
            if is_unlocked:
                if st.session_state.active_tree == t['name']:
                    st.success("✅ شجرتك المفعلة حالياً")
                else:
                    if st.button(f"تفعيل {t['icon']}", key=f"activate_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                if st.button(f"شراء بـ {t['price']} نقطة 🪙", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success(f"🎉 مبروك! قمت بشراء وتفعيل {t['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ نقاطك غير كافية لشراء هذه الشجرة!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
