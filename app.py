import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتقدم",
    page_icon="🎓",
    layout="wide"
)

# تصميم واجهة مستخدم فخمة ومرتبة (ألوان كحلي وبرتقالي هادئة - Navy & Warm Orange)
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
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #ff6b35;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 35px rgba(255, 107, 53, 0.25);
    }

    .hero-verse {
        font-size: 1.6rem;
        font-weight: 700;
        color: #ff6b35;
        margin-bottom: 8px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 2.1rem;
        color: #ffffff;
        margin-bottom: 6px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
    }

    /* البطاقات المخصصة */
    .custom-card {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    /* التبويبات */
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
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي في المنتصف
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">« وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ »</div>
        <div class="hero-title">النظام التحليلي الذكي للأداء الدراسي (Deluxe Edition)</div>
        <div class="hero-subtitle">معرض العلوم والابتكار — نموذج رياضي متقدم لقياس وتنبؤ التحصيل الأكاديمي بدقة استثنائية</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# التبويبات الرئيسية (شاملة الميزات الجديدة)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 لوحة التنبؤ (من 200)", 
    "🔋 بطارية الطاقة والاستشفاء", 
    "🤖 مكتبة الأوامر التحليلية الذكية", 
    "⚖️ مختبر محاكي السيناريوهات (ميزة 16)", 
    "❓ مولد الأسئلة والاختبارات (ميزة 17)", 
    "📋 خطة المذاكرة الشخصية"
])

# لوحة التحكم الجانبية (مقاييس دقيقة من 15 وموزعة بثبات)
st.sidebar.markdown("### 🎛️ أدوات القياس والتحليل الحيوية والدراسية")
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

# معادلة حساب المعدل الدقيقة جداً والمستقرة (من 200 نقطة)
# تم تصميمها لتكون موزعة بعقلانية وثبات بدون تقلبات مفاجئة مبالغ فيها
norm_sleep_q = sleep_quality / 15.0
norm_sleep_c = sleep_consistency / 15.0
norm_focus = deep_focus / 12.0
norm_stress = stress_level / 15.0
norm_motivation = motivation_level / 15.0
norm_hydration = hydration_level / 15.0
norm_env = environment_lighting / 15.0

# الحساب الأساسي من 200
score_200 = 85.0 # الحد الأدنى المستقر للنظام
score_200 += min(25.0, (sleep_hours / 12.0) * 25.0)
score_200 += norm_sleep_q * 22.0
score_200 += norm_sleep_c * 12.0
score_200 += norm_focus * 35.0
score_200 += norm_motivation * 18.0
score_200 += norm_hydration * 10.0
score_200 += norm_env * 12.0
score_200 += ((15 - stress_level) / 14.0) * 15.0  # تأثير التوتر العكسي المدروس

if study_method == "التسجيل النشط والخرائط الذهنية": 
    score_200 += 12.0
elif study_method == "حل التطبيقات والمسائل الرياضية": 
    score_200 += 14.0
else:
    score_200 += 4.0

if phone_isolation == "مفصول تماماً في غرفة ثانية": 
    score_200 += 10.0
elif phone_isolation == "في اليد وبجانب الكتاب": 
    score_200 -= 12.0

final_score_200 = min(max(score_200, 60.0), 200.0)
percentage_equivalent = (final_score_200 / 200.0) * 100
focus_efficiency = (deep_focus / total_study) * 100 if total_study > 0 else 0
accumulated_sleep_debt = max(0.0, (8.0 - sleep_hours) * 5.5)
mental_battery_index = min(100.0, max(10.0, (norm_sleep_q * 40) + (norm_motivation * 30) + (norm_hydration * 15) - (norm_stress * 25)))

retention_window = "الفترة الصباحية (الصبح بدري - صفاء ذهني عالي)" if "الصبح" in chronotype else "الفترة المسائية (تركيز هادئ ومتأخر)"
memory_fatigue = "منخفض ومستقر ✅" if deep_focus < 7 else "مرتفع ويحتاج استراحة قصيرة ⚠️"


with tab1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 مؤشر التنبؤ الأكاديمي الدقيق (من 200)")
        st.metric(label="مجموع نقاط التحصيل المعرفي", value=f"{final_score_200:.1f} / 200 نقطة")
        st.write(f"النسبة المئوية المعيارية المكافئة: **{percentage_equivalent:.2f}%**")
        
        if final_score_200 >= 160:
            st.success("🌟 **أداء استثنائي متوقع:** نظامك العصبي والبيئي في أعلى حالات الكفاءة والتوازن الدقيق.")
        elif final_score_200 >= 130:
            st.info("👍 **أداء متوازن ومستقر:** تحصيلك جيد جداً وثابت، ويمكنك الوصول للقمة برفع التركيز الصافي.")
        else:
            st.warning("⚠️ **تنبيه تحليل الأداء:** هناك عوامل (مثل التوتر أو قرب الهاتف) تؤثر بشكل مباشر وثابت على رصيدك المعرفي.")
            
        st.markdown("---")
        st.subheader("📈 كفاءة التركيز الصافي (Focus Efficiency)")
        st.write(f"نسبة الوقت الخالي من المشتتات إلى الوقت الكلي: **{focus_efficiency:.1f}%**")
        st.progress(min(int(focus_efficiency), 100))

    with col2:
        st.subheader("⚖️ تأثير العوامل على رصيدك")
        factors_df = pd.DataFrame({
            'المؤشر': ['التركيز الصافي', 'جودة النوم', 'الدافعية والحماس', 'إدارة التوتر', 'البيئة والماء'],
            'التأثير (%)': [32, 24, 18, 14, 12]
        })
        st.bar_chart(factors_df.set_index('المؤشر'))
    st.markdown('</div>', unsafe_allow_html=True)


with tab2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🔋 بطارية الطاقة الذهنية والاستشفاء العصبي")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="مؤشر شحن البطارية الذهنية", value=f"{mental_battery_index:.1f}%")
        st.progress(int(mental_battery_index))
    with c2:
        st.metric(label="عجز النوم المتراكم", value=f"{accumulated_sleep_debt:.1f} نقطة")
        st.write("أثر نقص النوم على الذاكرة قصيرة Mدى.")
    with c3:
        st.metric(label="مستوى التوتر الحالي", value=f"{stress_level} / 15")
        st.write("مقياس الإرهاق العصبي المؤثر على الفهم.")
    
    st.markdown("---")
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.info(f"🧠 **مُقيّم إرهاق الذاكرة العاملة:** {memory_fatigue}")
    with col_n2:
        st.success(f"⏰ **زمن الاستيعاب الأمثل:** {retention_window}")
    st.markdown('</div>', unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🤖 مكتبة الأوامر التحليلية الذكية (AI Prompts Library)")
    st.write("اختر أحد الأوامر التحليلية الجاهزة أدناه، وسيقوم النظام بتوليد تقرير استشاري عميق ومخصص لحالتك بناءً على مقاييسك الحالية:")
    
    selected_prompt = st.selectbox("اختر البرومْت التحليلي المطلوب:", [
        "1. محلل فجوة التركيز وانحراف الانتباه (Attention Gap Analyzer)",
        "2. خبير تخطيط الاستشفاء العصبي وعميق النوم (Sleep & Recovery Architect)",
        "3. مستشار التخلص الجذري من التسويف الدراسي (Anti-Procrastination Consultant)",
        "4. مهندس استراتيجيات الذاكرة طويلة المدى (Long-Term Memory Engineer)"
    ])
    
    if st.button("تنفيذ البرومْت وتوليد التقرير المعرفي"):
        st.markdown("### 📑 مخرجات التقرير التحليلي المخصص:")
        if "1." in selected_prompt:
            st.info(f"**تقرير فجوة الانتباه:** بناءً على ساعات تركيزك النقي ({deep_focus} ساعة) من أصل ({total_study} ساعة)، وجد النظام أن نسبة التشتت لديك تقدر بـ **{100 - focus_efficiency:.1f}%**. التوصية: فصل الهاتف تماماً واعتماد نظام الدقائق الخمس للراحة بين الجلسات.")
        elif "2." in selected_prompt:
            st.info(f"**تقرير الاستشفاء العصبي:** جودة نومك المسجلة ({sleep_quality}/15) مع ساعات النوم ({sleep_hours} ساعة) تعني أن عجز النوم لديك هو {accumulated_sleep_debt:.1f} نقطة. التوصية: تثبيت وقت الاستيقاظ الصبح بدري يومياً لضبط الساعة البيولوجية.")
        elif "3." in selected_prompt:
            st.info(f"**تقرير مكافحة التسويف:** مستوى الدافعية لديك ({motivation_level}/15) ومستوى التوتر ({stress_level}/15) يشيران إلى وجود مقاومة بدئية. التوصية: ابدأ بأصغر جزء ممكن من المادة لمدة 5 دقائق فقط دون ضغط.")
        else:
            st.info(f"**تقرير الذاكرة طويلة المدى:** استخدام أسلوب '{study_method}' مع بيئة إضاءة ({environment_lighting}/15) يتطلب تطبيق 'التكرار المتباعد' (اليوم الأول، الثالث، السابع، ثم الثلاثين) لضمان ترسيخ المعلومات بالذاكرة الدائمة.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab4:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("⚖️ مختبر محاكي السيناريوهات التنبؤي المتقدم (ميزة 16)")
    st.write("جرب كيف سيتغير رصيدك من 200 لو عدلت بعض العادات اليومية:")
    
    sim_extra_sleep = st.slider("إضافة ساعات نوم إضافية مقترحة", 0.0, 3.0, 1.0, 0.5)
    sim_extra_focus = st.slider("زيادة ساعات التركيز النقي المقترحة", 0.0, 4.0, 1.0, 0.5)
    
    # محاكاة محسنة
    simulated_score = min(200.0, final_score_200 + (sim_extra_sleep * 8.0) + (sim_extra_focus * 12.0))
    diff_score = simulated_score - final_score_200
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.metric(label="رصيدك الحالي", value=f"{final_score_200:.1f} / 200")
    with col_s2:
        st.metric(label="رصيدك المتوقع بعد التعديل المقترح", value=f"{simulated_score:.1f} / 200", delta=f"+{diff_score:.1f} نقطة")
    
    st.success(f"💡 **تحليل المحاكي:** لو التزمت بالنوم الزائد وزيادة التركيز النقي، سيرتفع معدلك المعياري وسينعكس إيجابياً على جاهزيتك الأكاديمية!")
    st.markdown('</div>', unsafe_allow_html=True)


with tab5:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("❓ مولد الأسئلة الاختبارية والاختبار الذاتي (ميزة 17)")
    st.write("بناءً على أسلوب دراستك ونمط تركيزك، يولد لك النظام أسئلة مراجعة وتحدٍ نشط لاختبار استيعابك الفعلي:")
    
    subject_choice = st.selectbox("اختر المجال الدراسي للاختبار:", ["الرياضيات والعلوم التطبيقية", "اللغات والعلوم الإنسانية", "الحفظ والمفاهيم العامة"])
    
    if st.button("توليد تحدي الاسترجاع النشط"):
        if "الرياضيات" in subject_choice:
            st.warning("🧩 **تحدي الاسترجاع:** اشرح بخطوات متسلسلة ودقيقة القانون الأساسي الذي درسته اليوم وكيف تطبيقه على مسألة معقدة دون النظر للكتاب.")
        elif "اللغات" in subject_choice:
            st.warning("🧩 **تحدي الاسترجاع:** أعد صياغة القاعدة أو القاعدة النحوية بأسلوبك الخاص وبناء ثلاثة أمثلة جديدة كلياً من إنشائك.")
        else:
            st.warning("🧩 **تحدي الاسترجاع:** اكتب خريطة ذهنية سريعة على ورقة فارغة لأهم 5 مفاهيم رئيسية حفظتها اليوم خلال الـ 10 دقائق القادمة.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab6:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📋 خطة المذاكرة الشخصية التلقائية وت تقرير الجاهزية")
    
    exam_readiness = min(100, int((percentage_equivalent + mental_battery_index) / 2))
    
    st.markdown(f"""
    * **مجموع رصيدك التحليلي المعرفي:** **{final_score_200:.1f} / 200 نقطة** (المكافئ المعياري: **{percentage_equivalent:.2f}%**)
    * **مؤشر جاهزية الامتحانات الشامل:** **{exam_readiness}%**
    * **ساعات النوم المسجلة:** {sleep_hours} ساعات (بجودة استشفاء {sleep_quality}/15)
    * **ساعات التركيز النقي:** {deep_focus} ساعات صافية خالية من المشتتات
    * **التوصية الخاصة لك:** نظراً لأن ذروتك الحيوية تكون في **{chronotype}**، احرص على استغلال وقت الصبح بدري للمادة الصعبة لتضمن أعلى حصيلة معرفية دون إرهاق.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Cognitive OS Pro Deluxe — مشروع معرض العلوم المتقدم (الصف العاشر).")
