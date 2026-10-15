import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تصميم واجهة مستخدم نظيفة، مرتبة، وبدون زحمة (UI/UX Clean & Minimalist Navy/Orange)
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

    /* العنوان الرئيسي المرن في المنتصف */
    .hero-container {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 100%);
        padding: 28px;
        border-radius: 16px;
        border: 2px solid #ff6b35;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.2);
    }

    .hero-verse {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ff6b35;
        margin-bottom: 6px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.8rem;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    /* بطاقات نظيفة ومنظمة بعيدة عن الكركبة */
    .clean-card {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* تنسيق التبويبات الفخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b132b;
        padding: 8px;
        border-radius: 10px;
        border: 1px solid #3a506b;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #1c2541;
        color: #94a3b8;
        border-radius: 6px;
        padding: 8px 16px;
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
        border-radius: 8px;
        padding: 8px 16px;
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
        <div class="hero-title">النظام التحليلي الذكي للأداء الدراسي</div>
        <div class="hero-subtitle">معرض العلوم والابتكار — منصة مقاييس وعمليات عصبية سلوكية دقيقة ومنظمة</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# التبويبات الرئيسية (مرتبة ومنظمة بدون زحمة)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 لوحة التنبؤ الشامل (من 500)", 
    "🔋 بطارية الطاقة والاستشفاء", 
    "🤖 المساعد التحليلي والبرومبتات", 
    "⚖️ مختبر المحاكاة التنبؤي", 
    "❓ تحدي الاسترجاع الذاتي", 
    "📋 خطة المذاكرة الشخصية"
])

# لوحة التحكم الجانبية (منظمة وواضحة - مقاييس من 15)
st.sidebar.markdown("### 🎛️ لوحة القياسات الحيوية والدراسية")
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

# معادلة حساب المعدل المحكمة والدقيقة جداً (من 500 نقطة - ثابتة وصارمة)
nq = sleep_quality / 15.0
nc = sleep_consistency / 15.0
nf = deep_focus / 12.0
ns = stress_level / 15.0
nm = motivation_level / 15.0
nh = hydration_level / 15.0
ne = environment_lighting / 15.0

# قاعدة أساسية من 180 نقطة، ويجب موازنة كل العوامل للوصول للحد الأقصى (500)
score_500 = 180.0  
score_500 += (sleep_hours / 12.0) * 60.0
score_500 += nq * 55.0
score_500 += nc * 30.0
score_500 += nf * 85.0
score_500 += nm * 40.0
score_500 += nh * 25.0
score_500 += ne * 30.0
score_500 += ((15 - stress_level) / 14.0) * 35.0

if study_method == "التسجيل النشط والخرائط الذهنية": 
    score_500 += 30.0
elif study_method == "حل التطبيقات والمسائل الرياضية": 
    score_500 += 35.0
else:
    score_500 += 10.0

if phone_isolation == "مفصول تماماً في غرفة ثانية": 
    score_500 += 25.0
elif phone_isolation == "في اليد وبجانب الكتاب": 
    score_500 -= 30.0

final_score_500 = min(max(score_500, 120.0), 500.0)
percentage_equivalent = (final_score_500 / 500.0) * 100
focus_efficiency = (deep_focus / total_study) * 100 if total_study > 0 else 0
accumulated_sleep_debt = max(0.0, (8.0 - sleep_hours) * 5.5)
mental_battery_index = min(100.0, max(10.0, (nq * 40) + (nm * 30) + (nh * 15) - (ns * 25)))

retention_window = "الفترة الصباحية (الصبح بدري - صفاء ذهني عالي)" if "الصبح" in chronotype else "الفترة المسائية (تركيز هادئ ومتأخر)"
memory_fatigue = "منخفض ومستقر ✅" if deep_focus < 7 else "مرتفع ويحتاج استراحة قصيرة ⚠️"


with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 مؤشر التنبؤ الأكاديمي الشامل (من 500)")
        st.metric(label="رصيد التحصيل المعرفي الإجمالي", value=f"{final_score_500:.1f} / 500 نقطة")
        st.write(f"النسبة المعيارية المكافئة: **{percentage_equivalent:.2f}%**")
        
        if final_score_500 >= 400:
            st.success("🌟 **أداء استثنائي:** توازن كامل في مقاييسك العصبية والبيئية يضعك في قمة الجاهزية.")
        elif final_score_500 >= 320:
            st.info("👍 **أداء مستقر:** تحصيلك ممتاز وثابت، وموازنة بسيطة في التركيز تضمن لك العلامة الكاملة.")
        else:
            st.warning("⚠️ **تنبيه:** هناك تفاوت في مقاييس النوم أو التوتر يتطلب ضبطاً لرفع رصيدك المعرفي.")
            
        st.markdown("---")
        st.subheader("📈 مؤشر استقرار وثبات المؤشرات (Stability Index)")
        st.write("يقيس مدى توازن المدخلات وعدم تأثر النتيجة بالتقلبات العشوائية.")
        st.progress(min(int(percentage_equivalent), 100))

    with col2:
        st.subheader("⚖️ الأوزان النسبية للعوامل")
        factors_df = pd.DataFrame({
            'المؤشر': ['التركيز الصافي', 'جودة النوم', 'الدافعية', 'التوتر', 'البيئة والماء'],
            'التأثير (%)': [32, 24, 18, 14, 12]
        })
        st.bar_chart(factors_df.set_index('المؤشر'))
    st.markdown('</div>', unsafe_allow_html=True)


with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🔋 بطارية الطاقة الذهنية والاستشفاء العصبي")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="مؤشر شحن البطارية", value=f"{mental_battery_index:.1f}%")
        st.progress(int(mental_battery_index))
    with c2:
        st.metric(label="عجز النوم المتراكم", value=f"{accumulated_sleep_debt:.1f} نقطة")
        st.write("أثر نقص النوم على الذاكرة العاملة.")
    with c3:
        st.metric(label="مستوى التوتر", value=f"{stress_level} / 15")
        st.write("مقياس الإرهاق العصبي المؤثر.")
    
    st.markdown("---")
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.info(f"🧠 **مُقيّم إرهاق الذاكرة العاملة الفرعي:** {memory_fatigue}")
    with col_n2:
        st.success(f"⏰ **نافذة الاستيعاب الأمثل الفرعية:** {retention_window}")
    st.markdown('</div>', unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🤖 المساعد التحليلي والبرومبتات الذكية المتعددة")
    st.write("اختر أمراً تحليلياً لتوليد تقرير استشاري دقيق مخصص حسب مقاييسك الحالية:")
    
    selected_prompt = st.selectbox("اختر البرومْت التحليلي المطلوب:", [
        "1. تحليل فجوة الانتباه ومقاومة التشتت الخارجي",
        "2. استراتيجية استشفاء الدماغ وتثبيت ساعات النوم",
        "3. تفكيك التسويف الدراسي ومعالجة الخمول المعرفي",
        "4. هندسة وتثبيت الذاكرة بعيدة المدى والتكرار"
    ])
    
    if st.button("تنفيذ البرومْت وتوليد التقرير المخصص"):
        st.markdown("### 📑 مخرجات التقرير المخصص:")
        if "1." in selected_prompt:
            st.info(f"**تقرير الانتباه:** التركيز النقي ({deep_focus} ساعة) من أصل ({total_study} ساعة) يوضح نسبة تشتت تقدر بـ **{100 - focus_efficiency:.1f}%**. التوصية الفرعية: ابعد الهاتف تماماً وطبق فترات الراحة القصيرة.")
        elif "2." in selected_prompt:
            st.info(f"**تقرير الاستشفاء:** جودة نومك ({sleep_quality}/15) وساعاتك ({sleep_hours}) تعني عجز نوم بمقدار {accumulated_sleep_debt:.1f} نقطة. التوصية الفرعية: ثبت وقت الاستيقاظ الصبح بدري يومياً.")
        elif "3." in selected_prompt:
            st.info(f"**تقرير مقاومة التسويف:** الدافعية ({motivation_level}/15) مع التوتر ({stress_level}/
