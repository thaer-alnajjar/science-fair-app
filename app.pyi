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
        border-top: 4px solid #3b82f6;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }

    .stButton>button {
        background: #f97316;
        color: white;
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #ea580c;
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
    
    # خيارات الوجبات والأطعمة الموسعة والمفصلة
    snack_type = st.selectbox("🍱 نوع الوجبة الرئيسية/الخفيفة قبل المذاكرة", [
        "🍏 وجبة ذكية خفيفة (مكسرات، فواكه، زبادي)",
        "🥩 وجبة غنية بالبروتين (بيض، دجاج، أسمك)",
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
    
    # تأثير نوع الوجبة على النتيجة والأداء
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
    st.success("✅ تم حفظ البيانات وتحليلها بنجاح!")

# ==========================================
# 4. التبويبات الرئيسية (بدون أرقام علوية)
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ"
])

total_entries = len(st.session_state.history)

# --- TAB 1: المؤشرات والموجز الشامل ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    if total_entries == 0:
        st.info("👈 أدخل بياناتك من اللوحة الجانبية ثم اضغط **(إرسال وتحليل البيانات)** لعرض التقرير الشامل.")
    else:
        latest = st.session_state.history[-1]
        
        # تنبيهات التطور أو الانخفاض مقارنة بالإدخال السابق
        if total_entries >= 2:
            prev_score = st.session_state.history[-2]["score"]
            diff = latest["score"] - prev_score
            if diff > 0:
                st.success(f"🎉 **تقدم أسطوري!** ارتفع رصيدك المعرفي بمقدار **+{diff:.1f} نقطة** مقارنة بالمرة السابقة.")
            elif diff < 0:
                st.warning(f"⚠️ **تنبيه انخفاض أداء:** تراجع أدائك بمقدار **{diff:.1f} نقطة**. تحقق من نصائح الاستشفاء والوجبات.")
            else:
                st.info("⚖️ أدائك مستقر تماماً ومماثل للجلسة السابقة.")

        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
            st.metric("النتيجة المعيارية الإجمالية", f"{latest['score']} / 500 نقطة")
            st.progress(int((latest['score']/500)*100))
            
            percentage = (latest['score'] / 500.0) * 100
            if percentage >= 80:
                st.success("🌟 جاهزية استثنائية: قدرات استيعاب واستشفاء عالية تضعك في القمة.")
            elif percentage >= 65:
                st.info("👍 أداء مستقر وممتاز، موازنة بسيطة في نومك وترطيبك تضمن العلامة الكاملة.")
            else:
                st.warning("⚠️ تنبيه: يتطلب الأمر ضبط ساعات النوم وتقليل الإرهاق البصري لرفع حصيلتك.")
                
        with col_b:
            st.subheader("📈 إحصائيات السجل")
            st.write(f"إجمالي الجلسات المسجلة: **{total_entries}**")
            st.write(f"تاريخ آخر تحليل: **{latest['timestamp']}**")

        # نظام الموجز التراكمي الذكي (كل 5 إدخالات)
        if total_entries % 5 == 0 and total_entries > 0:
            st.markdown("---")
            st.markdown(f"### 📋 الموجز التراكمي الشامل (تقرير الـ {total_entries} إدخالات)")
            
            last_5 = st.session_state.history[-5:]
            df_5 = pd.DataFrame(last_5)
            first_s = last_5[0]["score"]
            last_s = last_5[-1]["score"]
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
            
            st.markdown("### 🛠️ خطة التطوير والمكافأة المقترحة:")
            if chg <= 0:
                st.error("• **خطة تعديل المسار:** لوحظ تراجع في نقاطك الأخيرة. ابدأ بتغيير نظام وجبتك قبل المذاكرة، وافصل الهاتف تماماً في غرفة ثانية.")
            else:
                st.success("• **خطة تعزيز التفوق:** أداؤك متصاعد بامتياز! استمر على طريقة التسجيل النشط وقم بزيادة فترات الاستراحة القصيرة.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية والاستشفاء الجسدي")
    
    col_e1, col_e2 = st.columns(2)
    
    with col_e1:
        # فكرة 1: تتبع معدل التعب البصري المتطور
        st.markdown("#### 👁️ محلل التعب والإجهاد البصري")
        study_medium = st.radio("مصدر المذاكرة الرئيسي اليوم:", ["كتب وأوراق ورقية 📚", "جهاز لوحي / شاشة 🖥️", "خليط بينهما 📱📚"], horizontal=True)
        if total_entries > 0:
            latest = st.session_state.history[-1]
            multiplier = 1.2 if "شاشة" in study_medium else (0.8 if "ورقية" in study_medium else 1.0)
            eye_fatigue_score = min(100, int((latest['screen'] / 12.0) * 100 * multiplier))
            
            st.write(f"نسبة إجهاد العين المحسوبة: **{eye_fatigue_score}%**")
            st.progress(eye_fatigue_score)
            if eye_fatigue_score > 60:
                st.error("🚨 إجهاد بصري مرتفع! استخدم قطرة مرطبة وطبق قاعدة 20-20-20 فوراً.")
            else:
                st.success("✨ مستوى إجهاد العين ضمن النطاق الآمن والمقبول.")
        else:
            st.caption("أدخل بياناتك أولاً لحساب التعب البصري.")

        # فكرة 2: ربط المذاكرة بالمناخ والطقس
        st.markdown("---")
        st.markdown("#### 🌡️ مستشعر مناخ الغرفة ونقاء الهواء")
        if total_entries > 0:
            temp = latest['temp']
            if 20 <= temp <= 23:
                st.success(f"🌡️ حرارة الغرفة ({temp}°م) هي النطاق الذهبي لعمل خلايا الدماغ بكفاءة 100%.")
            elif temp > 23:
                st.warning(f"🌡️ حرارة الغرفة ({temp}°م) مرتفعة نسبياً وقد تزيد تدفق الدم للجلد بدلاً من الدماغ مما يسبب النعاس.")
            else:
                st.info(f"🌡️ حرارة الغرفة ({temp}°م) منخفضة، تأكد من ارتداء ملابس دافئة لمنع التشتت الجسدي.")

        # فكرة 3: منبه الإيقاع التكيفي لشبكة النوم
        st.markdown("---")
        st.markdown("#### ⏰ منبه دورات النوم التكيفي (Sleep Cycles)")
        if total_entries > 0:
            latest_sleep = latest['sleep']
            st.write(f"بناءً على نومك البارحة (**{latest_sleep} ساعة**)، الدورة العصبية المثالية للاستيقاظ غداً هي:")
            st.info("💡 **الموعد الأول (خفيف):** بعد 6 ساعات (4 دورات نوم كاملة)\n\n💡 **الموعد الثاني (عميق):** بعد 7.5 ساعات (5 دورات نوم كاملة)")

    with col_e2:
        # فكرة 6: محلل التهوية والأكسجين
        st.markdown("#### 🚪 محلل أكسجين وتهوية المكان")
        if total_entries > 0 and latest['focus'] >= 3:
            st.warning("⚠️ **تنبيه نقص الأكسجين المتوقع:** استمرار الجلوس لـ 3 ساعات يقلل أكسجين الغرفة المغلقة. افتح النافذة لمدة 4 دقائق لتجديد نشاطك.")
        else:
            st.success("🍃 نسبة التهوية والأكسجين في مكان جلوسك متوازنة.")

        # فكرة 13: سجل الوجبات الخفيفة والأطعمة الموسع
        st.markdown("---")
        st.markdown("#### 🍱 تحليل أثر الطعام على اليقظة والخمول")
        if total_entries > 0:
st.write(f"نوع الوجبة المسجلة: **{latest.get('snack', 'وجبة غير مسجلة')}**")
            if "ثقيلة" in latest['snack']:
                st.error("📉 **تنبيه الخمول الغذائي (Food Coma):** الكاربوهيدرات الثقيلة تسحب الدم للمعدة. ينصح بانتظار 45 دقيقة قبل بدء التفكير المعقد.")
            elif "سكريات" in latest['snack']:
                st.warning("⚠️ **تنبيه هبوط السكر المفاجئ:** السكريات تمنحك طاقة سريعة لمدة 20 دقيقة يعقبها هبوط حاد بالتركيز.")
            elif "ذكية" in latest['snack'] or "بالبروتين" in latest['snack']:
                st.success("⚡ **طاقة استثنائية:** اختيار ممتاز يمد الدماغ بنواقل عصبية مستقرة طوال جلسة الدراسة.")
            else:
                st.info("☕ **ملاحظة:** الاعتماد على القهوة أو الصيام يحتاج ترطيباً مضاعفاً بالماء لتجنب الصداع.")

        # فكرة 14: تنبيه وضعية الجلوس والدورة الدموية
        st.markdown("---")
        st.markdown("#### 🦴 فحص استقامة الظهر والوضعية")
        st.info("💡 **تمرين سريع (10 ثوانٍ):** ارفع كتفيك للأعلى ثم ارجعهما للخلف واشفط بطنك للداخل لتعديل استقامة فقرات ظهرك الآن.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ محرك الطاقة المعرفية والتحديات الإبداعية")
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        # فكرة 4: شجرة الإنتاجية التفاعلية
        st.markdown("#### 🌳 شجرة الإنتاجية الافتراضية")
        if total_entries > 0:
            focus_val = latest['focus']
            if focus_val >= 6:
                st.success("🌳 **شجرة بلا any غابة مثمرة بامتياز!** (أنجزت ساعات تركيز خرافية اليوم)")
            elif focus_val >= 3.5:
                st.info("🌿 **شجرة خضراء تنمو وتزهر بسعادة.** (مستوى تركيز رائع ومستقر)")
            else:
                st.warning("🌱 **نبتة صغيرة تحتاج إلى السقي.** (قم بريّه بساعات تركيز إضافية غداً)")
        else:
            st.caption("أدخل البيانات لتفعيل الشجرة.")

        # فكرة 5: حاسبة سرعة البديهة والصفاء الذهني
        st.markdown("---")
        st.markdown("#### ⚡ حاسبة سرعة البديهة والجاهزية العصبية")
        st.caption("اختبر صفاء ذهنك قبل بدء الدراسة:")
        if st.button("🎯 بدء اختبار التفاعل العصبي السريع"):
            rand_speed = random.randint(180, 240)
            st.success(f"⚡ **سرعة استجابتك العصبية:** **{rand_speed} ملي ثانية** (جاهزية عالية ومستعدة للحل والتحليل!)")

        # فكرة 7: تحدي الرفاق الآمن مع حفظ الخصوصية
        st.markdown("---")
        st.markdown("#### 🛡️ تحدي الرفاق التنافسي (المجهول)")
        peer_benchmark = 360.0
        if total_entries > 0:
            user_s = latest['score']
            st.write(f"رصيدك الحالي: **{user_s} نقطة** | متوسط الزملاء الإفتراضي: **{peer_benchmark} نقطة**")
            if user_s >= peer_benchmark:
                st.success("🥇 أنت متقدم على 85% من الزملاء في رصيد نقاط هذا الأسبوع!")
            else:
                st.info("🥈 أداء جيد! تحتاج إلى 15 نقطة إضافية للوصول للمركز الأول.")

    with col_t2:
        # فكرة 9: حاسبة استهلاك الطاقة الحرارية للدماغ
        st.markdown("#### 🧠 حاسبة السعرات الحرارية للدماغ")
        if total_entries > 0:
            cals = int(latest['focus'] * 72.0)
            st.write(f"🔥 بذل دماغك طاقة تقدر بـ **{cals} سعرة حرارية** أثناء حل المسائل والتفكير المعقد اليوم.")

        # فكرة 15: مكافأة الإنجاز الصامت والأوسمة
        st.markdown("---")
        st.markdown("#### 🏆 صندوق أوسمة الإنجاز الصامت")
        if total_entries > 0:
            if latest['focus'] >= 4.0 and latest['screen'] <= 3.0:
                st.success("🎖️ **وسام العبقري الهادئ:** عزل كامل للتشتت مع تركيز عميق أسطوري!")
            elif latest['focus'] >= 3.0:
                st.info("🏅 **وسام المثابر:** إنجاز جلسة دراسية ممتازة وثابتة.")
            else:
                st.caption("أكمل 3 ساعات تركيز نقي مع خفض ساعات الشاشة لفتح الأوسمة المغلقة.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل والتفريغ ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التحليل النفسي المعرفي وصندوق التفريغ")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        # فكرة 8: صندوق التفريغ الذهني التفاعلي
        st.markdown("#### 🗑️ صندوق التفريغ الذهني وتنقية الذاكرة")
        st.caption("اكتب أي فكرة جانبية أو مقلقة لتفريغها فوراً من عقلك:")
        thought_input = st.text_input("أدخل الفكرة المشتتة هنا:")
        if st.button("إفراغ الفكرة من الذهن"):
            if thought_input:
                st.session_state.mind_dump.append(thought_input)
                st.success("تم إفراغ الفكرة بنجاح من عقلك! أصبحت ذاكرتك الآن نظيفة ومستعدة.")
        
        if len(st.session_state.mind_dump) > 0:
            with st.expander("📂 الأفكار المفرغة والمحفوظة بالخلفية"):
                for idx, item in enumerate(st.session_state.mind_dump, 1):
                    st.write(f"{idx}. {item}")

        # فكرة 10: الخريطة الحرارية لأوقات التشتت
        st.markdown("---")
        st.markdown("#### 🗺️ الخريطة الحرارية لساعات السرحان")
        st.error("⏰ **ساعات التشتت العالية:** من 2:00 ظهراً إلى 4:00 عصراً (تجنب المذاكرة المعقدة فيها).")
        st.success("✨ **ساعات الصفاء الذهني:** من 6:00 صباحاً إلى 9:00 صباحاً (استغلها للمواد الصعبة).")

    with col_d2:
        # فكرة 11: محامي الدماغ المنطقي المفند للأعذار
        st.markdown("#### ⚖️ محامي الدماغ المنطقي تفنيد الكسل")
        custom_excuse = st.text_input("اكتب العذر الذي يجعلك تتكاسل الآن:")
        if st.button("💡 تفنيد العذر بالدليل العلمي"):
            if custom_excuse:
                st.info(f"⚖️ **رد المحامي المنطقي:** إن قولك '{custom_excuse}' هو مجرد حيلة من الدماغ للحفاظ على الطاقة! أثبتت الدراسات أن البدء بـ 5 دقائق فقط يكسر هذا الحاجز النفسي تماماً.")
            else:
                st.warning("يرجى كتابة العذر أولاً لتفنيده.")

        # فكرة 12: مولد القصص المعرفية والتلاخيص
        st.markdown("---")
        st.markdown("#### 📖 مولد التشبيهات والقصص المعرفية")
        subject_type = st.selectbox("اختر المادة لتوليد تشبيه قصصي لها:", ["العلوم والأحياء", "الرياضيات والفيزياء", "التاريخ واللغات"])
        if st.button("🔮 توليد قصة تثبيت المعلومة"):
            if "العلوم" in subject_type:
                st.write("📖 **القصة:** تخيل الخلية كمدينة متكاملة، والميتوكندريا هي محطة توليد الكهرباء التي تغذي الجميع بالأنوار!")
            elif "الرياضيات" in subject_type:
                st.write("📖 **القصة:** تخيل المعادلة ككفتي ميزان لا بد أن تبقيها متوازنة، كل شيء تفعله في اليمين كرر مثله في اليسار!")
            else:
                st.write("📖 **القصة:** تخيل الكلمات الجديدة كأصدقاء جدد تتعرف عليهم، كلما ناديتهم بأسمائهم أصبحوا أقرب لقلبك وذاكرتك!")

        # فكرة 16: حاسبة التفكير الزائد
        st.markdown("---")
        st.markdown("#### 🌀 حاسبة استرداد وقت القلق والتسويف")
        if total_entries > 0:
            over_mins = latest['overthinking']
            st.write(f"دقائق القلق المسجلة: **{over_mins} دقيقة**.")
            st.success(f"💡 تحويل وقت القلق إلى إنجاز يمنحك حل **{int(over_mins * 0.8)} مسألة إضافية** اليوم!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
