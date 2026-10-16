import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

# ==========================================
# 1. إعدادات الصفحة والتصميم العرفي
# ==========================================
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور v2",
    page_icon="🎓",
    layout="wide"
)

# تهيئة ذاكرة الجلسة لحفظ السجلات
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

# CSS لتجميل الواجهة
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
        padding: 30px;
        border-radius: 18px;
        border: 2px solid #4f46e5;
        border-right: 6px solid #ea580c;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.15);
    }

    .hero-verse {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ea580c;
        margin-bottom: 5px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.85rem;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .clean-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-top: 3px solid #1e293b;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
    }

    .stButton>button {
        background: #ea580c;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
        border: none;
    }
    
    .stButton>button:hover {
        background: #c2410c;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 النظام التحليلي الذكي للأداء الدراسي والتتبع الخماسي ⚡</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. اللوحة الجانبية: نموذج إدخال البيانات (Form)
# ==========================================
with st.sidebar.form(key="biometric_form"):
    st.markdown("### 🎛️ لوحة الإدخال والقياس الحيوية")
    st.caption("أدخل بياناتك ثم اضغط زر الإرسال للحفظ والتحليل")
    
    sleep_hours = st.slider("🌙 ساعات النوم اليومية", 3.0, 12.0, 7.5, 0.5)
    sleep_quality = st.slider("✨ جودة الاستشفاء النومى (1-15)", 1, 15, 11)
    sleep_consistency = st.slider("📅 انتظام أوقات النوم (1-15)", 1, 15, 12)
    
    screen_hours = st.slider("📱/🖥️ ساعات استخدام الشاشات اليومية", 1.0, 14.0, 5.0, 0.5) # فكرة 1: التعب البصري
    total_study = st.slider("⏱️ إجمالي ساعات الدراسة", 1.0, 12.0, 4.0, 0.5)
    deep_focus = st.slider("🎯 التركيز النقي (ساعات)", 0.5, 12.0, 3.5, 0.5)
    
    room_temp = st.slider("🌡️ درجة حرارة الغرفة (مئوية)", 16, 35, 23) # فكرة 3: المناخ
    overthinking_mins = st.slider("🌀 دقائق التفكير الزائد والقلق اليومي", 0, 120, 25, 5) # فكرة 16: التفكير الزائد
    
    stress_level = st.slider("⚠️ مستوى التوتر (1-15)", 1, 15, 5)
    motivation_level = st.slider("🔥 الدافعية والحماس (1-15)", 1, 15, 11)
    hydration_level = st.slider("💧 مستوى الترطيب والماء (1-15)", 1, 15, 10)
    
    snack_type = st.selectbox("🍏 نوع الوجبة الخفيفة قبل المذاكرة", ["فواكه/مكسرات (خفيفة)", "وجبة ثقيلة/سكريات", "صائم/بدون وجبة"]) # فكرة 13: وجبات ذكية
    study_method = st.selectbox("📚 أسلوب الدراسة", ["التسجيل النشط والخرائط الذهنية", "حل التطبيقات والمسائل", "القراءة التكرارية الصامتة"])
    chronotype = st.selectbox("🌅 ذروة النشاط", ["الصباح المبكر", "المساء والليل", "مرن ومتوازن"])
    phone_isolation = st.selectbox("📵 مكان الهاتف", ["مفصول تماماً في غرفة ثانية", "قريب بصامت", "في اليد وبجانب الكتاب"])

    submit_button = st.form_submit_button(label="🚀 إرسال وتحليل البيانات")

# ==========================================
# 3. معالجة البيانات والحسابات عند الإرسال
# ==========================================
if submit_button:
    # خوارزمية حساب النتيجة من 500
    score = 180.0
    score += (sleep_hours / 12.0) * 50.0
    score += (sleep_quality / 15.0) * 50.0
    score += (deep_focus / 12.0) * 90.0
    score += (motivation_level / 15.0) * 40.0
    score += (hydration_level / 15.0) * 25.0
    score -= (stress_level / 15.0) * 30.0
    score -= (screen_hours / 14.0) * 20.0 # خصم التعب البصري
    score -= (overthinking_mins / 120.0) * 25.0 # خصم التفكير الزائد
    
    if study_method != "القراءة التكرارية الصامتة":
        score += 30.0
    if phone_isolation == "مفصول تماماً في غرفة ثانية":
        score += 25.0
    elif phone_isolation == "في اليد وبجانب الكتاب":
        score -= 30.0
        
    final_score = min(max(score, 100.0), 500.0)
    
    # حفظ الإدخال في القائمة
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
    st.success("✅ تم حفظ البيانات وتحليلها بنجاح!")

# ==========================================
# 4. التنبيهات الرئيسية وتغطية الموجز الخماسي
# ==========================================
total_entries = len(st.session_state.history)

if total_entries > 0:
    latest = st.session_state.history[-1]
    
    # تنبيهات الصفحة الرئيسية بناءً على التقدم والضعف
    if total_entries >= 2:
        prev_score = st.session_state.history[-2]["score"]
        diff = latest["score"] - prev_score
        if diff > 0:
            st.balloons()
            st.success(f"🎉 **إنجاز متصاعد!** ارتفاع في أدائك اليوم بمقدار **+{diff:.1f} نقطة** مقارنة بالإدخال السابق.")
        elif diff < 0:
            st.warning(f"⚠️ **تنبيه انخفاض أداء:** تراجع أدائك بمقدار **{diff:.1f} نقطة**. يرجى مراجعة التوصيات والنوم بالقدر الكافي.")
        else:
            st.info("⚖️ **أداء مستقر:** مستوى أدائك اليوم يطابق الإدخال السابق تماماً.")

    # نظام الموجز التراكمي الشامل (كل 5 إدخالات)
    if total_entries % 5 == 0 and total_entries > 0:
        st.markdown("---")
        st.markdown(f"## 📋 الموجز التراكمي الشامل (تقرير الـ {total_entries} إدخالات)")
        
        last_5 = st.session_state.history[-5:]
        df_5 = pd.DataFrame(last_5)
        
        # تحليل التقدم خلال الـ 5 أيام
        first_5_score = last_5[0]["score"]
        last_5_score = last_5[-1]["score"]
        overall_change = last_5_score - first_5_score
        
        c_m1, c_m2, c_m3 = st.columns(3)
        with c_m1:
            st.metric("متوسط النقاط في الموجز", f"{df_5['score'].mean():.1f} / 500")
        with c_m2:
            st.metric("معدل التغير عبر الـ 5 جلسات", f"{overall_change:+.1f} نقطة")
        with c_m3:
            status = "📈 تقدم ممتاز" if overall_change > 10 else ("📉 تراجع يتطلب التدخل" if overall_change < -10 else "⚖️ استقرار")
            st.subheader(f"الحالة: {status}")
            
        # رسم بياني بسيط جداً
        st.markdown("#### 📊 منحنى التطور خلال الجلسات الخمس الأخيرة:")
        st.line_chart(df_5.set_index("timestamp")["score"])
        
        # وضع خطة التطوير
        st.markdown("### 🛠️ خطة التطوير التكيفية للمرحلة القادمة:")
        avg_screen = df_5["screen"].mean()
        avg_sleep = df_5["sleep"].mean()
        
        dev_plan = []
        if avg_screen > 6:
            dev_plan.append("• **تقليل ساعات الشاشة:** متوسط استخدامك للشاشات مرتفع، خفضه بمعدل ساعة يومياً لحماية البصر.")
        if avg_sleep < 7:
            dev_plan.append("• **تثبيت وقت النوم:** ارفع معدل نومك ليكون 7.5 ساعات على الأقل لتحسين الاسترجاع الذهني.")
        if overall_change <= 0:
            dev_plan.append("• **تغيير أسلوب المذاكرة:** جرب الاعتماد على حل المسائل والتسجيل النشط بدلاً من القراءة الصامتة.")
        else:
            dev_plan.append("• **الاستمرار على النمط الجيد:** حافظ على ساعات التركيز النقي الحالية مع زيادة فترات الاستراحة.")
            
        for plan in dev_plan:
            st.info(plan)
        st.markdown("---")

# ==========================================
# 5. التبويبات الرئيسية (تطبيق الأفكار 1-16)
# ==========================================
tab_dash, tab_ideas1_8, tab_ideas9_16 = st.tabs([
    "📊 لوحة التحليل الحالية", 
    "🧠 الأدوات التفاعلية (الأفكار 1-8)", 
    "⚡ الأدوات التفاعلية (الأفكار 9-16)"
])

# --- تبويب لوحة التحليل ---
with tab_dash:
    if total_entries == 0:
        st.info("👈 يرجى إدخال البيانات من اللوحة الجانبية والضغط على زر 'إرسال وتحليل البيانات'.")
    else:
        st.markdown('<div class="clean-card">', unsafe_allow_html=True)
        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.subheader("🎯 مؤشر التحصيل الأكاديمي الحركي")
            st.metric("النتيجة الحالية", f"{latest['score']} / 500 نقطة")
            st.progress(int((latest['score']/500)*100))
            
            # فكرة 3: منبه الإيقاع التكيفي
            suggested_wake = "06:30 صباحاً" if latest['sleep'] >= 7 else "08:00 صباحاً (لتعويض النوم)"
            st.info(f"⏰ **منبه الإيقاع التكيفي المقترح:** ينصح بالاستيقاظ غداً الساعة **{suggested_wake}** بناءً على ساعات نومك اليوم.")
            
        with col_b:
            # فكرة 4: شجرة الإنتاجية الافتراضية
            st.subheader("🌳 شجرة الإنتاجية")
            focus_hrs = latest['focus']
            if focus_hrs >= 6:
                st.success("🌳 شجرة مثمرة وافرة الأوراق! (إنجاز أسطوري)")
            elif focus_hrs >= 3:
                st.warning("🌿 شجرة متوسطة النمو (أداء جيد)")
            else:
                st.error("🌱 شجيرة صغيرة (تحتاج المزيد من سقي التركيز)")
        st.markdown('</div>', unsafe_allow_html=True)

# --- تبويب الأفكار من 1 إلى 8 ---
with tab_ideas1_8:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("💡 تطبيقات الأفكار الذكية (1 - 8)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # فكرة 1: تتبع معدل التعب البصري
        st.markdown("#### 1️⃣ مقياس التعب البصري")
        if total_entries > 0:
            eye_fatigue = min(100, int((latest['screen'] / 12.0) * 100))
            st.write(f"مستوى إجهاد العين المتوقع: **{eye_fatigue}%**")
            st.progress(eye_fatigue)
            if eye_fatigue > 60:
                st.caption("⚠️ ينصح بطبيق قاعدة 20-20-20 لإراحة العين فوراً.")
        else:
            st.write("أدخل البيانات أولاً لتفعيل المقياس.")

        # فكرة 2: ربط المذاكرة بالمناخ
        st.markdown("---")
        st.markdown("#### 2️⃣ مؤشر المذاكرة والمناخ")
        if total_entries > 0:
            temp = latest['temp']
            if 20 <= temp <= 24:
                st.success(f"🌡️ حرارة الغرفة ({temp}°م) مثالية جداً للاستيعاب والتركيز.")
            else:
                st.warning(f"🌡️ حرارة الغرفة ({temp}°م) قد تسبب الخمول أو المشتتات، يفضل تعديل التكييف.")
                
        # فكرة 6: محلل تهوية الغرفة
        st.markdown("---")
        st.markdown("#### 6️⃣ محلل تهوية الغرفة الافتراضي")
        if total_entries > 0 and latest['focus'] > 2:
            st.info("🚪 **تنبيه الأكسجين:** قمت بجلسة تركيز طويلة، فتح النافذة لمدة 5 دقائق يجدد نشاط الدماغ.")

    with col2:
        # فكرة 5: حاسبة سرعة البديهة
        st.markdown("#### 5️⃣ اختبار سرعة البديهة والجاهزية")
        if st.button("⚡ اضغط هنا لقياس الجاهزية العصبية"):
            st.success("🎯 استجابة ممتازة! عقلك جاهز لاستقبال المعلومات المعقدة.")
            
        # فكرة 7: تحدي الرفاق الآمن
        st.markdown("---")
        st.markdown("#### 7️⃣ تحدي الرفاق الآمن (دون كشف الخصوصية)")
        peer_avg = 340.0
        if total_entries > 0:
            user_s = latest['score']
            st.write(f"رصيدك الحالي: **{user_s}** | متوسط الزملاء الإفتراضي: **{peer_avg}**")
            if user_s >= peer_avg:
                st.success("🏆 أداؤك أعلى من المتوسط هذا الأسبوع!")
            else:
                st.info("💪 تفصلك نقاط قليلة للوصول للصدارة.")

        # فكرة 8: صندوق التفريغ الذهني
        st.markdown("---")
        st.markdown("#### 8️⃣ صندوق التفريغ الذهني")
        thought = st.text_input("اكتب الفكرة المشتتة لتنظيف الذاكرة المؤقتة:")
        if st.button("حفظ الفكرة وإفراغ الذهن"):
            if thought:
                st.session_state.mind_dump.append(thought)
                st.success("تم إفراغ الفكرة بنجاح من عقلك! ركز في دراستك الآن.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- تبويب الأفكار من 9 إلى 16 ---
with tab_ideas9_16:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ تطبيقات الأفكار الذكية (9 - 16)")
    
    col3, col4 = st.columns(2)
    
    with col3:
        # فكرة 9: حاسبة استهلاك الطاقة الحرارية
        st.markdown("#### 9️⃣ حاسبة السعرات الحرارية للدماغ")
        if total_entries > 0:
            brain_cals = int(latest['focus'] * 65.0)
            st.write(f"🔥 استهلك دماغك ما يقارب **{brain_cals} سعرة حرارية** أثناء التركيز اليوم.")
            
        # فكرة 10: الخريطة الحرارية لأوقات التشتت
        st.markdown("---")
        st.markdown("#### 🔟 خريطة أوقات التشتت المتوقعة")
        st.caption("أوقات يفضل تجنب المذاكرة المكثفة فيها:")
        st.error("⏰ الفترة من 2:00 ظهراً إلى 4:00 عصراً (انخفاض طبيعي بالطاقة)")

        # فكرة 11: محامي الدماغ المنطقي
        st.markdown("---")
        st.markdown("#### 1️⃣1️⃣ محامي الدماغ المنطقي")
        lazy_excuse = st.selectbox("اختر عذر الكسل المتكرر:", ["أشعر بالنعاس", "المادة صعبة جداً", "لا يوجد وقت كافٍ"])
        if lazy_excuse == "أشعر بالنعاس":
            st.info("⚖️ **الرد العلمي:** شرب كوب ماء والحركة لمدة دقيقتين يزيل النعاس الكاذب فوراً!")
        elif lazy_excuse == "المادة صعبة جداً":
            st.info("⚖️ **الرد العلمي:** قسم المادة لمقاطع صغيرة مدتها 5 دقائق وسيزول التعقيد.")
        else:
            st.info("⚖️ **الرد العلمي:** 15 دقيقة من التركيز النقي تعادل ساعتين من المذاكرة المشتتة.")

        # فكرة 12: مولد القصص المعرفية
        st.markdown("---")
        st.markdown("#### 2️⃣1️⃣ مولد القصص المعرفية")
        if st.button("📖 تحويل مفهوم معقد إلى قصة"):
            st.write("📖 **قصة الموصلات:** تخيل الإلكترونات كسيارات سريعة في طريق سريع بدون إشارات مرور!")

    with col4:
        # فكرة 13: سجل الوجبات الذكية
        st.markdown("#### 3️⃣1️⃣ أثر الوجبة الخفيفة")
        if total_entries > 0:
            st.write("تقييم الوجبة الخفيفة المحددة ودورها في اليقظة.")

        # فكرة 14: تنبيه وضعية الجلوس
        st.markdown("---")
        st.markdown("#### 4️⃣1️⃣ تنبيه وضعية الجلوس")
        st.warning("🦴 **تذكير:** اعد ضبط استقامة ظهرك وكتفيك الآن لحماية عمودك الفقري.")

        # فكرة 15: مكافأة الإنجاز الصامت
        st.markdown("---")
        st.markdown("#### 5️⃣1️⃣ وسام الإنجاز الصامت")
        if total_entries > 0 and latest['focus'] >= 4:
            st.success("🎖️ **وسام المحارب الصامت:** أتممت جلسة تركيز استثنائية!")
        else:
            st.caption("أنجز 4 ساعات تركيز للحصول على الوسام.")

        # فكرة 16: حاسبة التفكير الزائد
        st.markdown("---")
        st.markdown("#### 6️⃣1️⃣ حاسبة الوقت المسترد من التفكير الزائد")
        if total_entries > 0:
            lost_mins = latest['overthinking']
            st.write(f"دقائق قلق اليوم: **{lost_mins} دقيقة**.")
            st.info(f"💡 تحويل هذه الدقائق إلى أفعال يمنحك قراءة **{int(lost_mins*1.5)} صفحة** إضافية!")
            
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور v2 — جاهز كلياً لرفعه على GitHub ومنافسة المعارض العلمية.")
