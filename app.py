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

if "tree_customization" not in st.session_state:
    st.session_state.tree_customization = "شجرة بلوط خضراء 🌳"

if "user_points" not in st.session_state:
    st.session_state.user_points = 120  # رصيد نقاط افتراضي للتخصيص

# CSS لتصميم نظيف واحترافي
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
        padding: 28px;
        border-radius: 16px;
        border: 2px solid #6366f1;
        border-right: 6px solid #f97316;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);
    }

    .hero-verse {
        font-size: 1.35rem;
        font-weight: 700;
        color: #f97316;
        margin-bottom: 5px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.8rem;
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

# الهيدر الرئيسي
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 النظام التحليلي المتطور للأداء الدراسي والبيئة المعرفية</div>
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
    
    snack_type = st.selectbox("🍱 نوع الوجبة الرئيسية/الخفيفة قبل المذاكرة", [
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
    
    # زيادة رصيد النقاط تلقائياً عند الإرسال الناجح
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
    st.success("✅ تم حفظ البيانات وتحليلها بنجاح واكتسبت +15 نقطة إنجاز لشجرتك!")

# ==========================================
# 4. التبويبات الرئيسية (شاملة أيقونة الشجرة المستقلة)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ",
    "🌳 شجرة الإنتاجية الحية"
])

total_entries = len(st.session_state.history)

# --- TAB 1: المؤشرات والموجز الشامل ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    if total_entries == 0:
        st.info("👈 أدخل بياناتك من اللوحة الجانبية ثم اضغط **(إرسال وتحليل البيانات)** لعرض التقرير الشامل.")
    else:
        latest = st.session_state.history[-1]
        
        if total_entries >= 2:
            prev_score = st.session_state.history[-2].get("score", 0)
            curr_score = latest.get("score", 0)
            diff = curr_score - prev_score
            if diff > 0:
                st.success(f"🎉 **تقدم أسطوري!** ارتفع رصيدك المعرفي بمقدار **+{diff:.1f} نقطة** وشجرتك زادت إزهاراً.")
            elif diff < 0:
                st.warning(f"⚠️ **تنبيه انخفاض أداء:** تراجع أدائك بمقدار **{diff:.1f} نقطة** (تطايرت ورقة من شجرتك).")
            else:
                st.info("⚖️ أدائك مستقر تماماً ومماثل للجلسة السابقة.")

        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
            curr_score = latest.get("score", 0)
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
            st.subheader("📈 إحصائيات السجل")
            st.write(f"إجمالي الجلسات المسجلة: **{total_entries}**")
            st.write(f"رصيد نقاط إنجازك: **{st.session_state.user_points} نقطة** 🪙")

        if total_entries % 5 == 0 and total_entries > 0:
            st.markdown("---")
            st.markdown(f"### 📋 الموجز التراكمي الشامل (تقرير الـ {total_entries} إدخالات)")
            
            last_5 = st.session_state.history[-5:]
            df_5 = pd.DataFrame(last_5)
            first_s = last_5[0].get("score", 0)
            last_s = last_5[-1].get("score", 0)
            chg = last_s - first_s
            
            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                st.metric("متوسط النقاط في الموجز", f"{df_5['score'].mean():.1f} / 500")
            with mc2:
                st.metric("معدل التغير الإجمالي", f"{chg:+.1f} نقطة")
            with mc3:
                summary_status = "📈 تصاعد مستمر" if chg > 5 else ("📉 يتطلب تعديل المسار" if chg < -5 else "⚖️ أداء متوازن")
                st.subheader(f"الحالة: {summary_status}")
                
            st.markdown("#### 📊 منحنى التطور المعرفي عبر الإدخالات الخمسة الأخيرة:")
            st.line_chart(df_5.set_index("timestamp")["score"])

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية والاستشفاء الجسدي")
    
    col_e1, col_e2 = st.columns(2)
    
    with col_e1:
        st.markdown("#### 👁️ محلل التعب والإجهاد البصري")
        study_medium = st.radio("مصدر المذاكرة الرئيسي اليوم:", ["كتب وأوراق ورقية 📚", "جهاز لوحي / شاشة 🖥️", "خليط بينهما 📱📚"], horizontal=True)
        if total_entries > 0:
            latest = st.session_state.history[-1]
            screen_val = latest.get("screen", 4.5)
            multiplier = 1.2 if "شاشة" in study_medium else (0.8 if "ورقية" in study_medium else 1.0)
            eye_fatigue_score = min(100, int((screen_val / 12.0) * 100 * multiplier))
            
            st.write(f"نسبة إجهاد العين المحسوبة: **{eye_fatigue_score}%**")
            st.progress(eye_fatigue_score)
            if eye_fatigue_score > 60:
                st.error("🚨 إجهاد بصري مرتفع! استخدم قطرة مرطبة وطبق قاعدة 20-20-20 فوراً.")
            else:
                st.success("✨ مستوى إجهاد العين ضمن النطاق الآمن والمقبول.")
        else:
            st.caption("أدخل بياناتك أولاً لحساب التعب البصري.")

        st.markdown("---")
        st.markdown("#### 🌡️ مستشعر مناخ الغرفة ونقاء الهواء")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            temp = latest.get("temp", 23)
            if 20 <= temp <= 23:
                st.success(f"🌡️ حرارة الغرفة ({temp}°م) هي النطاق الذهبي لعمل خلايا الدماغ بكفاءة 100%.")
            else:
                st.warning(f"🌡️ حرارة الغرفة ({temp}°م) قد تؤثر على اليقظة.")

    with col_e2:
        st.markdown("#### 🚪 محلل أكسجين وتهوية المكان")
        st.success("🍃 نسبة التهوية والأكسجين في مكان جلوسك متوازنة.")

        st.markdown("---")
        st.markdown("#### 🍱 تحليل أثر الطعام على اليقظة والخمول")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            snack_val = latest.get("snack", "وجبة غير مسجلة")
            st.write(f"نوع الوجبة المسجلة: **{snack_val}**")
            if "ثقيلة" in snack_val:
                st.error("📉 **تنبيه الخمول الغذائي:** الكاربوهيدرات الثقيلة تسحب الدم للمعدة وتسبب النعاس.")
            elif "ذكية" in snack_val or "بالبروتين" in snack_val:
                st.success("⚡ **طاقة استثنائية:** اختيار ممتاز يمد الدماغ بنواقل عصبية مستقرة.")
            else:
                st.info("☕ حافظ على ترطيب جسمك بالماء باستمرار.")
        else:
            st.caption("أدخل بياناتك أولاً لتحليل الوجبة.")

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
            st.success(f"⚡ **سرعة استجابتك العصبية:** **{rand_speed} ملي ثانية** (جاهزية عالية ومستعدة للحل والتحليل!)")

        st.markdown("---")
        st.markdown("#### 🛡️ تحدي الرفاق التنافسي (المجهول)")
        peer_benchmark = 360.0
        if total_entries > 0:
            latest = st.session_state.history[-1]
            user_s = latest.get("score", 0)
            st.write(f"رصيدك الحالي: **{user_s} نقطة** | متوسط الزملاء الإفتراضي: **{peer_benchmark} نقطة**")
            if user_s >= peer_benchmark:
                st.success("🥇 أنت متقدم على 85% من الزملاء في رصيد نقاط هذا الأسبوع!")
            else:
                st.info("🥈 أداء جيد! تفصلك خطوات قليلة للصدارة.")

    with col_t2:
        st.markdown("#### 🧠 حاسبة السعرات الحرارية للدماغ")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            cals = int(latest.get("focus", 3.5) * 72.0)
            st.write(f"🔥 بذل دماغك طاقة تقدر بـ **{cals} سعرة حرارية** أثناء حل المسائل والتفكير المعقد اليوم.")
        else:
            st.caption("أدخل بياناتك لحساب السعرات.")

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
        
        if len(st.session_state.mind_dump) > 0:
            with st.expander("📂 الأفكار المفرغة والمحفوظة بالخلفية"):
                for idx, item in enumerate(st.session_state.mind_dump, 1):
                    st.write(f"{idx}. {item}")

    with col_d2:
        st.markdown("#### ⚖️ محامي الدماغ المنطقي تفنيد الكسل")
        custom_excuse = st.text_input("اكتب العذر الذي يجعلك تتكاسل الآن:")
        if st.button("💡 تفنيد العذر بالدليل العلمي"):
            if custom_excuse:
                st.info(f"⚖️ **رد المحامي المنطقي:** قولك '{custom_excuse}' هو مجرد حيلة من الدماغ لتوفير الطاقة. البدء بـ 5 دقائق يكسر هذا الحاجز فوراً!")
            else:
                st.warning("يرجى كتابة العذر أولاً لتفنيده.")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 5: شجرة الإنتاجية الحية (أيقونة رئيسية مستقلة) ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 شجرة الإنتاجية الحية والازهار المعرفي")
    st.write("هذه شجرتك التفاعلية الفريدة التي تنمو وتتغير أوراقها وفصولها بناءً على أدائك وتركيزك المستمر!")

    # حساب حالة الشجرة بناءً على إجمالي النقاط أو التركيز
    avg_focus = st.session_state.history[-1].get("focus", 3.0) if total_entries > 0 else 3.0
    
    # تحديد الفصل والشكل بناءً على الأداء
    if avg_focus >= 5.0:
        season_name = "🌸 فصل الربيع المزدهر (قمة الإنتاجية)"
        tree_visual = """
             🌸  🌿  🌸  🌿
          🌿   🌳🌳🌳   🌸
        🌸    🌳🌳🌳🌳🌳    🌿
             📁📁|  |📁📁
             📁📁|  |📁📁
        """
        leaf_messages = [
            "🍃 لأنك درست بجد واجتهاد دون تشتت.",
            "🌟 لأنك نمت جيداً وحققت استشفاءً كاملاً.",
            "💧 لأنك حافظت على ترطيب جسمك وعقلك.",
            "📵 لأنك عزلت هاتفك تماماً أثناء الجلسة العميقة."
        ]
    elif avg_focus >= 3.0:
        season_name = "☀️ فصل الصيف الأخضر المستقر"
        tree_visual = """
               🟢  🍃  🟢
            🍃  🟢🟢🟢  🍃
              🟢🟢🟢🟢🟢
                 trunk| |
                 trunk| |
        """
        leaf_messages = [
            "👍 لأن أداءك مستقر وثابت اليوم.",
            "📚 لأنك استخدمت استراتيجيات المذاكرة النشطة.",
            "🌡️ لأن مناخ غرفتك كان مثالياً للتركيز."
        ]
    else:
        season_name = "🍂 فصل الخريف المتساقط (يحتاج إنقاذ)"
        tree_visual = """
               🍂      🍃
            🍃     🪵🪵     🍂
                 🪵🪵🪵🪵
                 trunk| |
                 trunk| |
        """
        leaf_messages = [
            "⚠️ تطايِرت ورقة بسبب نقص ساعات التركيز النقي.",
            "⚠️ تطايِرت ورقة بسبب زيادة ساعات الشاشة والإرهاق البصري.",
            "💡 ابدأ جلسة تركيز جديدة الآن لإعادة إنبات الأوراق!"
        ]

    c_t1, c_t2 = st.columns([1, 1])
    
    with c_t1:
        st.markdown(f"### الموسم الحالي: {season_name}")
        st.code(tree_visual, language="text")
        st.metric("رصيد نقاط التخصيص المتاحة", f"{st.session_state.user_points} نقطة 🪙")
        
    with c_t2:
        st.markdown("### 🍃 أوراق الشجرة الناطقة (رسائل التحفيز):")
        st.write("كل ورقة على شجرتك تمثل سبباً لنجاحك العلمي اليوم:")
        for msg in leaf_messages:
            st.success(msg)
            
    st.markdown("---")
    st.markdown("### 🎨 متجر وكاتب مظهر الشجرة (تخصيص بالنقاط):")
    st.write("استخدم نقاط إنجازك لترقية مظهر شجرتك في المعرض العلمي:")
    
    selected_theme = st.selectbox("اختر شكل الشجرة المعرفية:", [
        "شجرة البلوط المعرفية الكلاسيكية 🌳 (تتطلب 0 نقطة)",
        "شجرة الكرز المزهرة اليابانية 🌸 (تتطلب 50 نقطة)",
        "شجرة السنديان الذهبية المتألقة ✨ (تتطلب 100 نقطة)"
    ])
    
    if st.button("✨ تطبيق مظهر الشجرة الجديد"):
        st.session_state.tree_customization = selected_theme
        st.success(f"🎉 تم تحديث مظهر شجرتك بنجاح إلى: **{selected_theme}**!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
