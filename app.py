import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

# ==========================================
# 1. إعدادات الصفحة والتصميم العصري
# ==========================================
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور v3",
    page_icon="🎓",
    layout="wide"
)

# تهيئة ذاكرة الجلسة
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

if "unlocked_badges" not in st.session_state:
    st.session_state.unlocked_badges = ["مبتدئ اليقظة العصبية"]

# CSS لتصميم نظيف واحترافي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #f1f5f9;
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

# الهيدر
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 منصة التحليل المعرفي والبيئي المتقدم للأداء الدراسي</div>
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
    
    snack_quality = st.selectbox("🍏 نوع الوجبة الخفيفة للدماغ", ["مكسرات وفواكه (ذكية)", "وجبة خفيفة عادية", "سكريات وسريعة", "بدون وجبة"])
    study_method = st.selectbox("📚 أسلوب المذاكرة", ["التسجيل النشط والخرائط", "حل المسائل والتطبيقات", "القراءة الصامتة"])
    phone_isolation = st.selectbox("📵 عزل الهاتف", ["مفصول تماماً في غرفة ثانية", "قريب بصامت", "في اليد وبجانب الكتاب"])

    submit_btn = st.form_submit_button(label="🚀 إرسال وتحليل البيانات")

# ==========================================
# 3. معالجة الحسابات عند الضغط على إرسال
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
    
    if study_method != "القراءة الصامتة":
        score += 25.0
    if phone_isolation == "مفصول تماماً في غرفة ثانية":
        score += 25.0
    elif phone_isolation == "في اليد وبجانب الكتاب":
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
        "temp": room_temp
    }
    st.session_state.history.append(entry)
    st.success("✅ تم حفظ البيانات وإرسالها بنجاح إلى سجل الأداء!")

# ==========================================
# 4. التبويبات الرئيسية (منظمة بذكاء بدون حشر)
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 لوحة المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء (1,2,3,6,13,14)", 
    "⚡ الطاقة والتحفيز (4,5,7,9,15)", 
    "🧠 التحليل والتفريغ (8,10,11,12,16)"
])

total_entries = len(st.session_state.history)

# --- TAB 1: المؤشرات والموجز الشامل ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    if total_entries == 0:
        st.info("👈 يرجى إدخال بياناتك من اللوحة الجانبية والضغط على زر **(إرسال وتحليل البيانات)** لعرض التقرير.")
    else:
        latest = st.session_state.history[-1]
        
        # تنبيهات فورية بناء على التقدم أو التأخر عن الجلسة السابقة
        if total_entries >= 2:
            prev_score = st.session_state.history[-2]["score"]
            diff = latest["score"] - prev_score
            if diff > 0:
                st.success(f"🎉 **تقدم ملحوظ!** ارتفع رصيدك اليوم بمقدار **+{diff:.1f} نقطة** عن الجلسة السابقة.")
            elif diff < 0:
                st.warning(f"⚠️ **تنبيه تراجع أداء:** انخفض رصيدك بمقدار **{diff:.1f} نقطة**. راجع التوصيات أدناه لتعويض النقص.")
            else:
                st.info("⚖️ أداؤك مستقر وثابت مقارنة بالإدخال السابق.")

        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.subheader("🎯 مؤشر التحصيل الأكاديمي الحالي")
            st.metric("النتيجة الإجمالية", f"{latest['score']} / 500 نقطة")
            st.progress(int((latest['score']/500)*100))
            
            percentage = (latest['score'] / 500.0) * 100
            if percentage >= 80:
                st.success("🌟 جاهزية عالية جداً للاستيعاب والتميز الأكاديمي.")
            elif percentage >= 65:
                st.info("👍 أداء جيد ومستقر، مع إمكانية تحسين بعض العادات الصغيرة.")
            else:
                st.warning("⚠️ يحتاج إلى إعادة ضبط لجدول النوم وتقليل المشتتات.")
                
        with col_b:
            st.subheader("📈 ملخص الجلسات")
            st.write(f"إعدد الإدخالات المحفوظة: **{total_entries}**")
            st.write(f"آخر تحديث: {latest['timestamp']}")

        # نظام الموجز التراكمي (كل 5 إدخالات)
        if total_entries % 5 == 0 and total_entries > 0:
            st.markdown("---")
            st.markdown(f"### 📋 الموجز التراكمي الذكي (تقرير الـ {total_entries} إدخالات)")
            
            last_5 = st.session_state.history[-5:]
            df_5 = pd.DataFrame(last_5)
            first_s = last_5[0]["score"]
            last_s = last_5[-1]["score"]
            chg = last_s - first_s
            
            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                st.metric("متوسط الـ 5 إدخالات", f"{df_5['score'].mean():.1f} / 500")
            with mc2:
                st.metric("معدل التطور العام", f"{chg:+.1f} نقطة")
            with mc3:
                summary_status = "📈 متطور للأفضل" if chg > 5 else ("📉 متراجع بحاجة لحذر" if chg < -5 else "⚖️ مستقر ومتوازن")
                st.subheader(f"الحالة: {summary_status}")
                
            st.markdown("#### 📊 خط التطور البياني للإدخالات الخمسة الأخيرة:")
            st.line_chart(df_5.set_index("timestamp")["score"])
            
            st.markdown("### 🛠️ خطة التطوير المقترحة للمرحلة القادمة:")
            if chg <= 0:
                st.error("• **التوجيه العلاجي:** لاحظنا ثباتاً أو تراجعاً طفيفاً؛ يُنصح بزيادة ساعات التركيز النقي وعزل الهاتف كلياً في غرفة أخرى.")
            else:
                st.success("• **التوجيه التعزيزي:** أداؤك في تصاعد مستمر! حافظ على روتين النوم الحالي واستمر في استخدام التميز النشط.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء (الأفكار 1, 2, 3, 6, 13, 14) ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 ركن البيئة العصبية والاستشفاء البدني")
    
    col_e1, col_e2 = st.columns(2)
    
    with col_e1:
        # فكرة 1: تتبع معدل التعب البصري
        st.markdown("#### 1️⃣ مقياس إجهاد التعب البصري")
        if total_entries > 0:
            latest = st.session_state.history[-1]
            eye_stress = min(100, int((latest['screen'] / 12.0) * 100))
            st.write(f"نسبة الإرهاق البصري المتوقع للشاشات: **{eye_stress}%**")
            st.progress(eye_stress)
            if eye_stress > 50:
                st.caption("💡 **قاعدة 20-20-20:** انظر إلى شيء يبعد 20 قدماً لمدة 20 ثانية لإرخاء عضلات العين.")
        else:
            st.caption("أدخل بياناتك أولاً لتفعيل المؤشر.")

        # فكرة 2: ربط المذاكرة بالمناخ
        st.markdown("---")
        st.markdown("#### 2️⃣ مستشعر مناخ الغرفة والتركيز")
        if total_entries > 0:
            temp = latest['temp']
            if 20 <= temp <= 24:
                st.success(f"🌡️ درجة حرارة الغرفة ({temp}°م) ممتازة لتحفيز الخلايا العصبية.")
            elif temp > 24:
                st.warning(f"🌡️ الجو دافئ ({temp}°م)، قد يسبب خمولاً خفيفاً. يفضل تعديل التكييف.")
            else:
                st.warning(f"🌡️ الجو بارد ({temp}°م)، قد يشتت الانتباه الجسدي.")

        # فكرة 3: منبه الإيقاع التكيفي
        st.markdown("---")
        st.markdown("#### 3️⃣ منبه الإيقاع التكيفي للاستيقاظ")
        if total_entries > 0:
            rec_wake = "06:15 صباحاً" if latest['sleep'] >= 7.0 else "07:30 صباحاً (لتعويض عجز النوم)"
            st.info(f"⏰ **الموعد المقترح لاستيقاظ الغد:** **{rec_wake}** بناءً على مقاييس نومك الحالية.")

    with col_e2:
        # فكرة 6: محلل تهوية الغرفة
        st.markdown("#### 6️⃣ محلل تهوية الغرفة الافتراضي")
        st.info("🚪 **تنبيه الأكسجين:** بعد جلوس متواصل لفترة طويلة، فتح النافذة لـ 3 دقائق يرفع نسبة التركيز بنسبة 15%.")

        # فكرة 13: سجل الوجبات الخفيفة الذكية
        st.markdown("---")
        st.markdown("#### 3️⃣1️⃣ تقييم الوجبة الخفيفة")
        if total_entries > 0:
            st.write(f"طبيعة الوجبة المختارة: **{snack_quality}**")
            if "ذكية" in snack_quality:
                st.success("✨ اختيار رائع! الأغذية الطبيعية تمنح طاقة مستقرة للدماغ.")
            else:
                st.warning("⚠️ الوجبات الثقيلة أو السكريات تسبب هبوطاً مفاجئاً للطاقة بعد ساعة.")

        # فكرة 14: تنبيه وضعية الجلوس
        st.markdown("---")
        st.markdown("#### 4️⃣1️⃣ تنبيه استقامة وضعية الجلوس")
        st.warning("🦴 **فحص استقامة الظهر:** اعد ضبط كتفيك وظهرك بشكل مستقيم الآن لحماية عمودك الفقري وإطالة مدة التحمل.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز (الأفكار 4, 5, 7, 9, 15) ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ منصة الطاقة المعرفية وتحديات الإنجاز")
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        # فكرة 4: شجرة الإنتاجية الافتراضية
        st.markdown("#### 4️⃣ شجرة الإنتاجية الرقمية")
        if total_entries > 0:
            f_hrs = latest['focus']
            if f_hrs >= 5:
                st.success("🌳 **شجرة عملاقة ومثمرة بالكامل!** (أداء تركيز عميق استثنائي)")
            elif f_hrs >= 2.5:
                st.info("🌿 **شجرة تنمو وتزهر بشكل جميل.** (أداء جيد ومثمر)")
            else:
                st.warning("🌱 **شجيرة في بداية نموها.** (تحتاج زيادة ساعات التركيز)")
        else:
            st.caption("أدخل البيانات لتفعيل الشجرة.")

        # فكرة 5: حاسبة سرعة البديهة والجاهزية العصبية
        st.markdown("---")
        st.markdown("#### 5️⃣ اختبار سرعة البديهة والصفاء")
        if st.button("⚡ قياس استجابة الرفكس العصبي الفوري"):
            st.success("🎯 **نتيجة الاختبار:** زمن الاستجابة العصبي لديك في أفضل حالاته (صفاء ذهن ممتاز).")

        # فكرة 7: تحدي الرفاق الآمن
        st.markdown("---")
        st.markdown("#### 7️⃣ تحدي الرفاق الآمن (الخصوصية التامة)")
        peer_benchmark = 350.0
        if total_entries > 0:
            curr_s = latest['score']
            st.write(f"رصيدك المعرفي: **{curr_s}** | متوسط الزملاء الإفتراضي الآمن: **{peer_benchmark}**")
            if curr_s >= peer_benchmark:
                st.success("🏆 أنت ضمن قائمة المتصدرين في مؤشر الأداء!")
            else:
                st.info("💪 تفصلك خطوات بسيطة لتجاوز المتوسط العام.")

    with col_t2:
        # فكرة 9: حاسبة استهلاك الطاقة الحرارية للدماغ
        st.markdown("#### 9️⃣ حاسبة سعرات وحرارة الدماغ")
        if total_entries > 0:
            brain_cals_val = int(latest['focus'] * 68.0)
            st.write(f"🔥 استهلك دماغك ما يقارب **{brain_cals_val} سعرة حرارية** أثناء عمليات التحليل والتفكير اليوم.")

        # فكرة 15: مكافأة الإنجاز الصامت
        st.markdown("---")
        st.markdown("#### 5️⃣1️⃣ وسام مكافأة الإنجاز الصامت")
        if total_entries > 0 and latest['focus'] >= 3.5:
            st.success("🎖️ **وسام المحارب المعرفي:** تم منحك هذا الوسام نظراً لاتمامك جلسة تركيز عميقة بامتياز.")
        else:
            st.caption("أتمم 3.5 ساعات تركيز نقي لفتح هذا الوسام التقديري.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل العميق والتفريغ (الأفكار 8, 10, 11, 12, 16) ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التحليل النفسي المعرفي وصندوق التفريغ")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        # فكرة 8: صندوق التفريغ الذهني
        st.markdown("#### 8️⃣ صندوق التفريغ الذهني المؤقت")
        st.caption("اكتب أي أفكار جانبية أو مشتتات تفكير لتفريغها فوراً من عقلك:")
        user_thought = st.text_input("أدخل فكرة مشتتة هنا:")
        if st.button("تفريغ الفكرة وحفظها بالخلفية"):
            if user_thought:
                st.session_state.mind_dump.append(user_thought)
                st.success("🗑️ تمت تنقية الذاكرة المؤقتة بنجاح! ركز في دراستك الآن.")
        
        if len(st.session_state.mind_dump) > 0:
            with st.expander("📂 عرض الأفكار المفرغة سابقاً"):
                for idx, t in enumerate(st.session_state.mind_dump, 1):
                    st.write(f"{idx}. {t}")

        # فكرة 10: الخريطة الحرارية لأوقات التشتت
        st.markdown("---")
        st.markdown("#### 🔟 خريطة أوقات التشتت الحرارية")
        st.error("⏰ **ساعات الذروة المشتتة المتوقعة:** بين الساعة 1:30 ظهراً و 3:30 عصراً (يفضل تجنب المواد الصعبة فيها).")

    with col_d2:
        # فكرة 11: محامي الدماغ المنطقي
        st.markdown("#### 1️⃣1️⃣ محامي الدماغ المنطقي المفند للأعذار")
        excuse_type = st.selectbox("اختر العذر الذي يراودك الآن:", [
            "أشعر بالكسل الشديد ولا أستطيع البدء",
            "المادة معقدة جداً ولن أستوعبها",
            "الوقت متأخر ولن ألحق بإنجاز شيء"
        ])
        if "كسل" in excuse_type:
            st.info("⚖️ **الرد العلمي:** الكسل شعور زائف يزول فور البدء في إنجاز أول خطوة مدتها دقيقة واحدة فقط!")
        elif "معقدة" in excuse_type:
            st.info("⚖️ **الرد العلمي:** التعقيد يزول بتقسيم المادة إلى أجزاء صغرى ميكروية.")
        else:
            st.info("⚖️ **الرد العلمي:** إنجاز قليل ومستمر خير من التسويف التام!")

        # فكرة 12: مولد القصص المعرفية
        st.markdown("---")
        st.markdown("#### 2️⃣1️⃣ مولد القصص المعرفية الذكية")
        if st.button("📖 توليد تشبيه قصصي فوري"):
            st.write("📖 **القصة التشبيهية:** تخيل المعلومات الجديدة كضيوف جدد، عليك إكرامهم بالتكرار لتستقر في غرف الذاكرة بعيدة المدى نهائياً!")

        # فكرة 16: حاسبة التفكير الزائد والقلق
        st.markdown("---")
        st.markdown("#### 6️⃣1️⃣ حاسبة استرداد دقائق القلق")
        if total_entries > 0:
            mins_over = latest['overthinking']
            st.write(f"دقائق القلق المسجلة اليوم: **{mins_over} دقيقة**.")
            st.info(f"💡 تحويل طاقة هذا القلق إلى فعل يمنحك سرعة إنجاز تقدر بـ **{int(mins_over * 1.4)} صفحة** إضافية!")
            
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور v3 — مصمم خصيصاً بمعايير احترافية لتطبيقات الويب على Streamlit.")
