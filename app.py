import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة بنمط سطح المكتب
st.set_page_config(
    page_title="Cognitive OS | وعلم الإنسان ما لم يعلم",
    page_icon="💠",
    layout="wide"
)

# تصميم واجهة مستخدم فاخرة تحاكي أنظمة التشغيل الحديثة (Windows / Desktop OS Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #05070b;
        color: #f1f5f9;
    }

    /* محاكاة شريط نظام التشغيل العلوي (OS Window Header) */
    .os-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        padding: 16px 24px;
        border-radius: 14px 14px 0 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }

    .os-title {
        font-weight: 900;
        font-size: 1.4rem;
        background: linear-gradient(90deg, #60a5fa, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* تصميم البطاقات الزجاجية (Glassmorphic Cards) */
    .os-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    /* تخصيص التبويبات لتشبه نوافذ النظام */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b0f17;
        padding: 10px;
        border-radius: 12px;
        border: 1px solid #1e293b;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #111827;
        color: #94a3b8;
        border-radius: 8px;
        padding: 10px 22px;
        font-weight: 700;
        border: 1px solid #1f2937;
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white !important;
        border-color: #60a5fa !important;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# واجهة الهيدر التي تشبه نظام التشغيل
st.markdown("""
    <div class="os-header">
        <div class="os-title">⚡ النظام التحليلي المعرفي العالي (Cognitive OS v2.5)</div>
        <div style="color: #94a3b8; font-size: 0.9rem;">«وعلم الإنسان ما لم يعلم» — بيئة الأبحاث العصبية السلوكية</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# تقسيم المنصة إلى تبويبات نظام التشغيل
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 لوحة القيادة المركزية", 
    "🧠 ماتريكس الكفاءة العصبية", 
    "⏰ الإيقاع الحيوي والذاكرة", 
    "🛠️ مختبر تحليل العقبات", 
    "📋 منصة عرض الحكام الرسمية"
])

# الشريط الجانبي المحاكي للوحة التحكم (Control Panel)
st.sidebar.markdown("### 🎛️ لوحة تحكم المتغيرات العضوية")
st.sidebar.markdown("---")
sleep_hours = st.sidebar.slider("ساعات النوم اليومية", 3.0, 10.0, 7.5, 0.5)
sleep_quality = st.sidebar.slider("جودة الاستشفاء النومى (1-10)", 1, 10, 8)
total_study = st.sidebar.slider("إجمالي ساعات التواجد الدراسي", 1.0, 12.0, 4.0, 0.5)
deep_focus = st.sidebar.slider("مدة التركيز النقي (Deep Work)", 0.5, 8.0, 3.0, 0.5)
study_method = st.sidebar.selectbox("أسلوب معالجة وتثبيت المعرفة", ["التسجيل النشط والخرائط العصبية", "حل التطبيقات والمسائل الرياضية", "القراءة التكرارية السلبية"])
chronotype = st.sidebar.selectbox("الذروة الحيوية للإيقاع العصبي", ["صباحي مبكر (كفاءة الفجر)", "مسائي عميق (تركيز الليل)", "مرن / متوازن"])
environment_noise = st.sidebar.selectbox("مستوى العزل البيئي والمشتتات", ["هادئ ومفصول عن الأجهزة", "متوسط (ضوضاء خلفية خفيفة)", "مرتفع (تنبيهات ومشتتات محيطة)"])

# خوارزمية الحساب المعرفي الدقيقة
base_score = 42 + (sleep_hours * 3.1) + (sleep_quality * 1.7) + (total_study * 0.7) + (deep_focus * 4.4)
if study_method == "التسجيل النشط والخرائط العصبية": 
    base_score += 11
elif study_method == "حل التطبيقات والمسائل الرياضية": 
    base_score += 13

if environment_noise == "هادئ ومفصول عن الأجهزة": 
    base_score += 7
elif environment_noise == "مرتفع (تنبيهات ومشتتات محيطة)": 
    base_score -= 9

predicted_grade = min(max(base_score, 35.0), 99.8)
ffr_ratio = (deep_focus / total_study) * 100 if total_study > 0 else 0
sleep_debt = max(0, (7.5 - sleep_hours) * 6)

cognitive_load = min(100, (total_study * 7.5) - (deep_focus * 4.5))
neuro_balance = min(100, max(0, (sleep_quality * 6.5) + (sleep_hours * 4.2) - (sleep_debt * 0.4)))


with tab1:
    st.markdown('<div class="os-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 الماتريكس التنبؤية لتحصيل المعرفة")
        st.metric(label="مؤشر الكفاءة الأكاديمية المتوقع", value=f"{predicted_grade:.1f}%")
        
        if sleep_hours < 5:
            st.error("⚠️ **تنبيه حرج للنظام العضوي:** نقص النوم المتراكم يضعف شبكات الذاكرة العاملة وكفاءة اتخاذ القرار البشري بنسبة تصل إلى 45%.")
        elif ffr_ratio > 65 and sleep_quality >= 7:
            st.success("✨ **حالة التدفق الذهني القصوى (Flow State):** توازن مثالي بين جودة الاستشفاء العصبي وعمق التركيز.")
        else:
            st.info("⚖️ **حالة استقرار تشغيلي:** الأداء ضمن المدى الطبيعي مع فرصة حقيقية للرفع عبر ترشيد وقت التركيز النقي.")
            
        st.markdown("---")
        st.subheader("📈 مؤشر التركيز الفعلي النقي (FFR Index)")
        st.write(f"نسبة التركيز الخالي من المشتتات إلى الإجمالي: **{ffr_ratio:.1f}%**")
        st.progress(min(int(ffr_ratio), 100))

    with col2:
        st.subheader("⚖️ الأوزان النسبية للمتغيرات")
        importance_df = pd.DataFrame({
            'المتغير': ['التركيز النقي', 'جودة النوم', 'طريقة المعالجة', 'العزل البيئي'],
            'التأثير (%)': [39, 26, 21, 14]
        })
        st.bar_chart(importance_df.set_index('المتغير'))
    st.markdown('</div>', unsafe_allow_html=True)


with tab2:
    st.markdown('<div class="os-card">', unsafe_allow_html=True)
    st.subheader("🧠 نظام تشخيص الإرهاق والديون النومية التراكمية")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="عجز الاستشفاء المتراكم", value=f"{sleep_debt:.1f} نقطة")
        st.write("مقياس انخفاض طاقة شبكات الدماغ العليا.")
    with c2:
        st.metric(label="مؤشر الحمل المعرفي", value=f"{cognitive_load:.1f}%")
        st.write("معدل استهلاك طاقة الذاكرة المؤقتة.")
    with c3:
        st.metric(label="التوازن العصبي-الجسدي", value=f"{neuro_balance:.1f}%")
        st.write("كفاءة طاقة الجسد والعقل الكلية.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="os-card">', unsafe_allow_html=True)
    st.subheader("⏰ مطابق الإيقاع البيولوجي وجدولة التكرار الذكي")
    st.write(f"بناءً على ذروة إيقاعك العصبي المحددة كـ **{chronotype}**:")
    
    if "صباحي" in chronotype:
        st.success("🌅 **التوجيه الأمثل:** خصص الفترة الصباحية (من 8:00 إلى 12:00) لمهام التفكير المعقد واستيعاب العلوم الصعبة، حيث تكون قمة كفاءة الذاكرة العاملة.")
    elif "مسائي" in chronotype:
        st.warning("🌙 **التوجيه الأمثل:** نافذتك الذهبية تبدأ بعد الساعة 6 مساءً، مع ضرورة تجنب الشاشات الساطعة قبل النوم للحفاظ على كفاءة الاستشفاء.")
    else:
        st.info("🔄 **التوجيه الأمثل:** توزيع المهام على فترتين متوازنتين (بعد العصر وقبل منتصف الليل).")
        
    st.markdown("### 📚 جدول التكرار المتباعد الموصى به لتثبيت الذاكرة الطويلة:")
    st.markdown("- **المحطة الأولى:** مراجعة أولية بعد 24 ساعة من تلقي المعرفة.")
    st.markdown("- **المحطة الثانية:** مراجعة تثبيت بعد 3 أيام.")
    st.markdown("- **المحطة الثالثة:** مراجعة استرجاع بعد 7 أيام.")
    st.markdown("- **المحطة الرابعة:** مراجعة ترسيخ نهائية بعد 30 يوماً.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab4:
    st.markdown('<div class="os-card">', unsafe_allow_html=True)
    st.subheader("🛠️ مختبر تحليل العقبات والعلاج السلوكي")
    user_hurdle = st.selectbox("حدد التحدي المعرفي الذي تواجهه حالياً:", [
        "أعاني من نسيان المعلومات المعقدة بعد فترة وجيزة",
        "أواجه تشتتاً حاداً وفقدانًا للقدرة على الاستمرار بالجلوس",
        "أقضي ساعات طويلة جداً بالدراسة ولكن النتائج ضعيفة",
        "أشعر بخمول وكسل ذهني حاد فور الشروع في القراءة"
    ])
    
    if st.button("تشغيل البروتوكول العلاجي المعرفي"):
        st.markdown("### 💡 التوجيه التحليلي الموصى به من النظام:")
        if "نسيان المعلومات" in user_hurdle:
            st.info("**التوجيه:** توقف عن القراءة السلبية الصامتة. طبق تقنية 'الاسترجاع النشط'؛ اشرح المفهوم لنفسك بصوت عالٍ كأنك تلقي محاضرة علمية، فهذا يحفز مسارات الذاكرة بعمق.")
        elif "تشتت حاد" in user_hurdle:
            st.info("**التوجيه:** طبق نظام العزل المكاني (ضع الهاتف في غرفة أخرى)، وقسّم وقتك إلى جلسات تركيز مكثفة مدتها 25 دقيقة تليها راحة استشفاء قصيرة.")
        elif "ساعات طويلة جداً" in user_hurdle:
            
