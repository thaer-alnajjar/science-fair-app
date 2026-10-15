import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي",
    page_icon="🎓",
    layout="wide"
)

# تصميم واجهة مستخدم بسيطة وفخمة بألوان الكحلي والبرتقالي (Navy & Orange Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #0b132b;
        color: #e0f2fe;
    }

    /* العنوان الرئيسي الفخم في المنتصف */
    .hero-container {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 100%);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ff6b35;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.2);
    }

    .hero-title {
        font-weight: 900;
        font-size: 2rem;
        color: #ffffff;
        margin-bottom: 8px;
    }

    .hero-verse {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ff6b35;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1rem;
    }

    /* البطاقات الفخمة */
    .custom-card {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    /* التبويبات الاحترافية */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #0b132b;
        padding: 10px;
        border-radius: 12px;
        border: 1px solid #3a506b;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #1c2541;
        color: #94a3b8;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 700;
        border: 1px solid #3a506b;
    }

    .stTabs [aria-selected="true"] {
        background: #ff6b35 !important;
        color: white !important;
        border-color: #ff6b35 !important;
    }

    .stButton>button {
        background: #ff6b35;
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي في المنتصف تماماً
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">« وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ »</div>
        <div class="hero-title">النظام التحليلي الذكي للأداء الدراسي</div>
        <div class="hero-subtitle">مشروع معرض العلوم — قياس وتنبؤ دقيق لعادات العقل والتحصيل الأكاديمي</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# التبويبات الرئيسية
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 لوحة التنبؤ بالمعدل", 
    "🧠 بطارية الطاقة والاستشفاء", 
    "⏰ الإيقاع الحيوي والذاكرة", 
    "🛠️ مختبر تحليل العقبات", 
    "📋 خطة المذاكرة الشخصية"
])

# لوحة التحكم الجانبية (مقاييس دقيقة من 15)
st.sidebar.markdown("### 🎛️ أدوات القياس والتحليل الحيوية")
st.sidebar.markdown("---")

sleep_hours = st.sidebar.slider("ساعات النوم اليومية", 3.0, 12.0, 7.5, 0.5)
sleep_quality = st.sidebar.slider("جودة الاستشفاء النومى (من 15)", 1, 15, 11)
sleep_consistency = st.sidebar.slider("انتظام أوقات النوم (من 15)", 1, 15, 12)
total_study = st.sidebar.slider("إجمالي ساعات التواجد الدراسي", 1.0, 12.0, 4.0, 0.5)
deep_focus = st.sidebar.slider("مدة التركيز النقي بدون مشتتات (من 15)", 0.5, 12.0, 4.0, 0.5)
stress_level = st.sidebar.slider("مستوى التوتر والضغط العصبي (من 15)", 1, 15, 5)
motivation_level = st.sidebar.slider("مستوى الدافعية والحماس (من 15)", 1, 15, 11)
hydration_level = st.sidebar.slider("مستوى ترطيب الجسم وشرب الماء (من 15)", 1, 15, 10)
environment_lighting = st.sidebar.slider("جودة الإضاءة والهدوء البيئي (من 15)", 1, 15, 12)

study_method = st.sidebar.selectbox("أسلوب دراستك ومعرفتك", ["التسجيل النشط والخرائط الذهنية", "حل التطبيقات والمسائل الرياضية", "القراءة التكرارية الصامتة"])
chronotype = st.sidebar.selectbox("ذروة نشاطك العصبي", ["الصبح بدري (نشاط الصباح الصافي)", "المساء والليل (تركيز متأخر وهادئ)", "مرن ومتوازن"])
phone_isolation = st.sidebar.selectbox("مكان هاتفك الخلوي أثناء الدراسة", ["مفصول تماماً في غرفة ثانية", "قريب بصامت", "في اليد وبجانب الكتاب"])

# معادلة حسابية دقيقة متقدمة تعطي نتائج احترافية
norm_sleep_q = sleep_quality / 15.0
norm_sleep_c = sleep_consistency / 15.0
norm_focus = deep_focus / 12.0
norm_stress = stress_level / 15.0
norm_motivation = motivation_level / 15.0
norm_hydration = hydration_level / 15.0
norm_env = environment_lighting / 15.0

base_calc = 46.0 \
            + (sleep_hours * 2.7) \
            + (norm_sleep_q * 15.0) \
            + (norm_sleep_c * 7.0) \
            + (norm_focus * 19.0) \
            + (norm_motivation * 9.0) \
            + (norm_hydration * 5.0) \
            + (norm_env * 6.0) \
            - (norm_stress * 11.0)

if study_method == "التسجيل النشط والخرائط الذهنية": 
    base_calc += 7.0
elif study_method == "حل التطبيقات والمسائل الرياضية": 
    base_calc += 8.5
else:
    base_calc -= 4.0

if phone_isolation == "مفصول تماماً في غرفة ثانية": 
    base_calc += 6.0
elif phone_isolation == "في اليد وبجانب الكتاب": 
    base_calc -= 10.0

predicted_grade = min(max(base_calc, 35.0), 99.8)
focus_efficiency = (deep_focus / total_study) * 100 if total_study > 0 else 0
accumulated_sleep_debt = max(0.0, (8.0 - sleep_hours) * 5.5)
mental_battery_index = min(100.0, max(10.0, (norm_sleep_q * 40) + (norm_motivation * 30) + (norm_hydration * 15) - (norm_stress * 25)))

# ميزات جديدة حسابية متقدمة
retention_window = "الفترة الصباحية (من 8 صباحاً لـ 11 صباحاً)" if "الصبح" in chronotype else "الفترة المسائية (من 6 مساءً لـ 9 مساءً)"
memory_fatigue = "منخفض ومستقر ✅" if deep_focus < 6 else "مرتفع ويحتاج استراحة ⚠️"


with tab1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 مؤشر التنبؤ الأكاديمي الدقيق")
        st.metric(label="المعدل الدراسي المتوقع بناءً على مقاييسك", value=f"{predicted_grade:.2f}%")
        
        if predicted_grade >= 90:
            st.success("🌟 **أداء ممتاز جداً:** نمطك العضوي والبيئي في أعلى مستويات التوازن والاستعداد.")
        elif predicted_grade >= 75:
            st.info("👍 **أداء مستقر وجيد:** تحصيلك الأكاديمي ممتاز، وقريب جداً من الوصول للقمة برفع التركيز الصافي.")
        else:
            st.warning("⚠️ **تنبيه تحليل الأداء:** هناك عوامل مثل التوتر أو قرب الهاتف تساهم في خفض كفاءة الاستيعاب.")
            
        st.markdown("---")
        st.subheader("📈 كفاءة التركيز الصافي (Focus Efficiency)")
        st.write(f"نسبة التركيز الخالي من المشتتات إلى الوقت الكلي: **{focus_efficiency:.1f}%**")
        st.progress(min(int(focus_efficiency), 100))

    with col2:
        st.subheader("⚖️ تأثير العوامل على المعدل")
        factors_df = pd.DataFrame({
            'المؤشر': ['التركيز الصافي', 'جودة النوم', 'الدافعية والحماس', 'إدارة التوتر', 'البيئة والماء'],
            'التأثير (%)': [32, 24, 18, 14, 12]
        })
        st.bar_chart(factors_df.set_index('المؤشر'))
    st.markdown('</div>', unsafe_allow_html=True)


with tab2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🧠 بطارية الطاقة الذهنية والاستشفاء العصبي")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="مؤشر شحن البطارية الذهنية", value=f"{mental_battery_index:.1f}%")
        st.progress(int(mental_battery_index))
    with c2:
        st.metric(label="عجز النوم المتراكم", value=f"{accumulated_sleep_debt:.1f} نقطة")
        st.write("أثر نقص النوم على الذاكرة قصيرة المدى.")
    with c3:
        st.metric(label="مستوى التوتر الحالي", value=f"{stress_level} / 15")
        st.write("مقياس الإرهاق العصبي المؤثر على الفهم.")
    
    st.markdown("---")
    # ميزات جديدة مضافة هنا
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.info(f"🧠 **مُقيّم إرهاق الذاكرة العاملة (ميزة 2):** {memory_fatigue}")
    with col_n2:
        st.success(f"⏰ **زمن الاستيعاب الأمثل (ميزة 1):** {retention_window}")
    st.markdown('</div>', unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("⏰ الإيقاع الحيوي والذاكرة طويلة المدى")
    st.write(f"بناءً على ذروة نشاطك المحددة في وقت: **{chronotype}**:")
    
    if "الصبح" in chronotype:
        st.success("🌅 **التوجيه الأمثل:** دراستك في وقت الصبح بدري تمنح دماغك قدرة هائلة على حفظ المعادلات واستيعاب العلوم الصعبة.")
    elif "المساء" in chronotype:
        st.warning("🌙 **التوجيه الأمثل:** نافذتك الذهبية تبدأ بعد العصر، احرص على عزل الهاتف تماماً لتستفيد من صفاء الذهن ليلاً.")
    else:
        st.info("🔄 **التوجيه الأمثل:** يمكنك توزيع مهامك الدراسية على فترات متوازنة حسب جدول يومك.")
        
    st.markdown("### 📚 جدول التكرار المتباعد لتثبيت المعلومات:")
    st.markdown("- **المحطة الأولى:** مراجعة سريعة بعد 24 ساعة من تلقي الدرس.")
    st.markdown("- **المحطة الثانية:** مراجعة تثبيت ثانية بعد 3 أيام.")
    st.markdown("- **المحطة الثالثة:** مراجعة استرجاع بعد 7 أيام.")
    st.markdown("- **المحطة الرابعة:** مراجعة ترسيخ نهائية قبل الامتحان بشهر.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab4:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🛠️ مختبر تحليل العقبات وحل المشكلات")
    user_problem = st.selectbox("ما هي المشكلة الأكاديمية التي تواجهك غالباً؟", [
        "أنسى المعلومات المعقدة فور دخولي قاعة الامتحان",
        "أشعر بتشتت حاد وفقدان القدرة على الاستمرار بالمذاكرة",
        "أدرس ساعات طويلة ولكن العلامات لا ترتفع بالمستوى المطلوب",
        "أشعر بخمول وكسل ذهني حاد أول ما أفتح الكتاب"
    ])
    
    if st.button("الحصول على التشخيص والعلاج الفوري"):
        st.markdown("### 💡 البروتوكول المقترح لحل المشكلة:")
        if "أنسى المعلومات" in user_problem:
            st.info("**الحل العلمي (ميزة 3 - استراتيجية الحفظ):** توقف عن القراءة الصامتة. اشرح الدرس بصوت عالٍ كأنك تشرحه لزميلك (الاسترجاع النشط).")
        elif "تشتت حاد" in user_problem:
            st.info("**الحل العلمي (ميزة 4 - الراحة النشطة):** طبق نظام 25 دقيقة تركيز نقي يليها 5 دقائق مشي خفيف أو إغماض عينين لاستعادة النشاط.")
        elif "ساعات طويلة ولكن العلامات" in user_problem:
            st.info("**الحل العلمي:** المشكلة في 'التركيز الصافي'. 3 ساعات بلا مشتتات تفوق 7 ساعات من الدراسة المشتتة.")
        else:
            st.info("**الحل العلمي:** الخمول ناتج عن نقص ترطيب الجسم. اشرب كوب ماء كبير وافتح شباك الغرفة لتتجدد الطاقة.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab5:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📋 خطة المذاكرة الشخصية وتقرير الجاهزية")
    st.write("ملخص جدولك اليومي لتكون جاهزاً لأي اختبار:")
    
    # ميزة 5: مؤشر جاهزية الامتحانات الأسبوعي
    exam_readiness = min(100, int((predicted_grade + mental_battery_index) / 2))
    
    st.markdown(f"""
    * **المعدل المتوقع بناءً على مقاييسك:** **{predicted_grade:.2f}%**
    * **مؤشر جاهزية الامتحانات (ميزة 5):** **{exam_readiness}%** (يعكس جاهزيتك الكلية لأي اختبار قادم)
    * **ساعات النوم المسجلة:** {sleep_hours} ساعات (بجودة {sleep_quality}/15)
    * **ساعات التركيز الصافي:** {deep_focus} ساعات صافية
    * **التوصية الخاصة لك:** ذروتك الحيوية في **{chronotype}**، اجعل المواد الصعبة في هذا الوقت بالتحديد لتضمن أعلى تحصيل.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Cognitive OS Pro — مشروع معرض العلوم المتقدم (الصف العاشر).")
