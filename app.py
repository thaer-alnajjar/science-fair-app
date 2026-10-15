import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة وتكوين العرض
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تصميم واجهة مستخدم بيضاء، نظيفة، وحيوية (Minimalist Light Mode with Soul)
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

    /* العنوان الرئيسي الفخم في المنتصف بخلفية بيضاء وبطاقة نظيفة وحيوية */
    .hero-container {
        background: #ffffff;
        padding: 30px;
        border-radius: 16px;
        border: 2px solid #ea580c;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 6px 25px rgba(234, 88, 12, 0.08);
    }

    .hero-verse {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ea580c;
        margin-bottom: 6px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.9rem;
        color: #1e293b;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        color: #64748b;
        font-size: 0.95rem;
    }

    /* بطاقات بيضاء نظيفة ومنظمة ذات مظهر حيوي */
    .clean-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
    }

    /* تنسيق التبويبات الفخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f1f5f9;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        color: #475569;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 700;
        border: 1px solid #e2e8f0;
    }

    .stTabs [aria-selected="true"] {
        background: #ea580c !important;
        color: white !important;
        border-color: #ea580c !important;
        box-shadow: 0 4px 12px rgba(234, 88, 12, 0.25);
    }

    .stButton>button {
        background: #ea580c;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        width: 100%;
        box-shadow: 0 4px 12px rgba(234, 88, 12, 0.2);
    }
    
    .stButton>button:hover {
        background: #c2410c;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي في المنتصف مع الإيموجيات الحية
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 النظام التحليلي الذكي للأداء الدراسي ⚡</div>
        <div class="hero-subtitle">معرض العلوم والابتكار — منصة قياس الأنماط المعرفية والبيئة العصبية السلوكية المتقدمة</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# التبويبات الرئيسية (مرتبة وحيوية)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 لوحة التنبؤ (من 500)", 
    "🔋 الطاقة والاستشفاء", 
    "🤖 المساعد والبرومبتات", 
    "⚖️ مختبر المحاكاة", 
    "❓ تحدي الاسترجاع", 
    "📋 خطة المذاكرة"
])

# لوحة التحكم الجانبية
st.sidebar.markdown("### 🎛️ لوحة القياسات الحيوية")
st.sidebar.markdown("---")

sleep_hours = st.sidebar.slider("🌙 ساعات النوم اليومية", 3.0, 12.0, 7.5, 0.5)
sleep_quality = st.sidebar.slider("✨ جودة الاستشفاء النومى (من 15)", 1, 15, 11)
sleep_consistency = st.sidebar.slider("📅 انتظام أوقات النوم (من 15)", 1, 15, 12)
total_study = st.sidebar.slider("⏱️ إجمالي ساعات التواجد الدراسي", 1.0, 12.0, 4.0, 0.5)
deep_focus = st.sidebar.slider("🎯 مدة التركيز النقي بدون مشتتات (من 15)", 0.5, 12.0, 4.0, 0.5)
stress_level = st.sidebar.slider("⚠️ مستوى التوتر والضغط العصبي (من 15)", 1, 15, 5)
motivation_level = st.sidebar.slider("🔥 مستوى الدافعية والحماس (من 15)", 1, 15, 11)
hydration_level = st.sidebar.slider("💧 مستوى ترطيب الجسم (من 15)", 1, 15, 10)
environment_lighting = st.sidebar.slider("💡 جودة الإضاءة والهدوء البيئي (من 15)", 1, 15, 12)

study_method = st.sidebar.selectbox("📚 أسلوب دراستك ومعرفتك", ["التسجيل النشط والخرائط الذهنية", "حل التطبيقات والمسائل الرياضية", "القراءة التكرارية الصامتة"])
chronotype = st.sidebar.selectbox("🌅 ذروة نشاطك العصبي", ["الصبح بدري (نشاط الصباح الصافي)", "المساء والليل (تركيز هادئ ومتأخر)", "مرن ومتوازن"])
phone_isolation = st.sidebar.selectbox("📵 مكان هاتفك الخلوي أثناء الدراسة", ["مفصول تماماً في غرفة ثانية", "قريب بصامت", "في اليد وبجانب الكتاب"])

# معادلة حساب المعدل المحكمة والدقيقة جداً (من 500 نقطة - ثابتة وصارمة)
nq = sleep_quality / 15.0
nc = sleep_consistency / 15.0
nf = deep_focus / 12.0
ns = stress_level / 15.0
nm = motivation_level / 15.0
nh = hydration_level / 15.0
ne = environment_lighting / 15.0

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

# حساب الميزة الفرعية الأولى: مؤشر استقرار النمط الأسبوعي
pattern_stability = "مستقر وثابت 📈" if (sleep_consistency >= 10 and stress_level <= 8) else "متذبذب ويحتاج انضباط 📉"


with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 مؤشر التنبؤ الأكاديمي الشامل (من 500)")
        st.metric(label="رصيد التحصيل المعرفي الإجمالي", value=f"{final_score_500:.1f} / 500 نقطة")
        st.write(f"النسبة المعيارية المكافئة: **{percentage_equivalent:.2f}%**")
        
        if final_score_500 >= 400:
            st.success("🌟 أداء استثنائي: توازن كامل في مقاييسك العصبية والبيئية يضعك في قمة الجاهزية الأكاديمية.")
        elif final_score_500 >= 320:
            st.info("👍 أداء مستقر: تحصيلك ممتاز وثابت، وموازنة بسيطة في التركيز تضمن لك العلامة الكاملة.")
        else:
            st.warning("⚠️ تنبيه: هناك تفاوت في مقاييس النوم أو التوتر يتطلب ضبطاً لرفع رصيدك المعرفي.")
            
        st.markdown("---")
        # الميزة الفرعية 1 مضمنة هنا
        st.subheader("📈 مؤشر استقرار النمط الأسبوعي (ميزة فرعية)")
        st.write(f"حالة اتساق العادات اليومية: **{pattern_stability}**")
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
        st.info(f"🧠 مُقيّم إرهاق الذاكرة العاملة الفرعي: {memory_fatigue}")
    with col_n2:
        # الميزة الفرعية 2 مضمنة هنا
        hydration_synergy = "ممتازة وتدعم اليقظة 💧" if hydration_level >= 10 else "تحتاج زيادة لدعم الخلايا ⚠️"
        st.success(f"💧 مؤشر استجابة الترطيب العصبي (ميزة فرعية): {hydration_synergy}")
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
            st.info(f"💡 تقرير الانتباه: التركيز النقي ({deep_focus} ساعة) من أصل ({total_study} ساعة) يوضح نسبة تشتت تقدر بـ {100 - focus_efficiency:.1f}%. التوصية الفرعية: ابعد الهاتف تماماً وطبق فترات الراحة القصيرة.")
        elif "2." in selected_prompt:
            st.info(f"💡 تقرير الاستشفاء: جودة نومك ({sleep_quality}/15) وساعاتك ({sleep_hours}) تعني عجز نوم بمقدار {accumulated_sleep_debt:.1f} نقطة. التوصية الفرعية: ثبت وقت الاستيقاظ الصبح بدري يومياً.")
        elif "3." in selected_prompt:
            st.info(f"💡 تقرير مقاومة التسويف: الدافعية ({motivation_level}/15) مع التوتر ({stress_level}/15) تتطلب البدء البسيط جداً (قاعدة الـ 5 دقائق الأولى دون ضغط).")
        else:
            st.info(f"💡 تقرير الذاكرة: الاعتماد على '{study_method}' مع بيئة إضاءة ({environment_lighting}/15) يحتم استخدام 'التكرار المتباعد' لتثبيت المعلومات نهائياً.")
            
    st.markdown("---")
    # الميزة الفرعية 3 مضمنة هنا
    st.subheader("⚡ مولد الأسئلة التكيفية السريعة (ميزة فرعية)")
    if st.button("توليد سؤال تكيفى فوري حسب البرومْت"):
        st.success("🧩 سؤال تفكيري مقترح: بناءً على اختيارك التحليلي، حاول كتابة تلخيص في سطرين للمفهوم الأكثر صعوبة الذي واجهته اليوم.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚖️ مختبر المحاكاة التنبؤي المتقدم")
    st.write("اختبر أثر تحسين بعض العادات على رصيدك الكلي من 500:")
    
    sim_sleep = st.slider("🌙 إضافة ساعات نوم إضافية مقترحة", 0.0, 3.0, 1.0, 0.5)
    sim_focus = st.slider("🎯 زيادة ساعات التركيز النقي المقترحة", 0.0, 4.0, 1.0, 0.5)
    
    simulated_score = min(500.0, final_score_500 + (sim_sleep * 15.0) + (sim_focus * 22.0))
    diff_score = simulated_score - final_score_500
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.metric(label="رصيدك الحالي", value=f"{final_score_500:.1f} / 500")
    with col_s2:
        st.metric(label="رصيدك المتوقع بعد التعديل", value=f"{simulated_score:.1f} / 500", delta=f"+{diff_score:.1f} نقطة")
    
    st.success("💡 رأي المحاكي الفرعي: الالتزام بهذه التعديلات الموازنة سيرفع رصيدك المعرفي بشكل ملموس ومستقر!")
    
    st.markdown("---")
    # الميزة الفرعية 4 مضمنة هنا
    lost_time_recovery = int((100 - focus_efficiency) * 0.4)
    st.info(f"⏳ حاسبة استرداد الوقت الضائع (ميزة فرعية): تحتاج حوالي **{lost_time_recovery} دقائق** من التركيز النقي الخالي من أي مشتتات لتعويض آثار التشتت السابق اليوم.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("❓ تحدي الاسترجاع الذاتي والتدريب النشط")
    st.write("تحدًّ نشط لتثبيت الفهم بناءً على نمط دراستك:")
    
    domain_choice = st.selectbox("اختر المجال للاختبار:", ["العلوم والرياضيات التطبيقية", "المواد الأدبية والنصوص", "الحفظ والمفاهيم العامة"])
    
    if st.button("بدء التحدي النشط"):
        if "العلوم" in domain_choice:
            st.warning("🧩 التحدي: اشرح بخطوات متسلسلة القانون أو القاعدة التي درستها اليوم وكيف تطبقها على مسألة جديدة دون النظر للمرجع.")
        elif "المواد الأدبية" in domain_choice:
            st.warning("🧩 التحدي: أعد صياغة القاعدة أو الفكرة الرئيسية بأسلوبك الخاص وبناء ثلاثة أمثلة جديدة كلياً.")
        else:
            st.warning("🧩 التحدي: ارسم خريطة ذهنية سريعة على ورقة فارغة لأهم 5 مفاهيم رئيسية حفظتها اليوم خلال 5 دقائق.")
            
    st.markdown("---")
    # الميزة الفرعية 5 مضمنة هنا
    st.success("🏆 مسجل مسار الانتصارات الذهنية (ميزة فرعية): لقد أكملت حتى الآن محطات التحدي الاسترجاعي بكفاءة عالية، استمر لتعزيز ثقتك قبل الامتحان!")
    st.markdown('</div>', unsafe_allow_html=True)


with tab6:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("📋 خطة المذاكرة الشخصية وتقرير الجاهزية الشامل")
    
    exam_readiness = min(100, int((percentage_equivalent + mental_battery_index) / 2))
    
    report_lines = [
        f"• **رصيدك التحليلي الإجمالي:** **{final_score_500:.1f} / 500 نقطة** (النسبة المعيارية: **{percentage_equivalent:.2f}%**)",
        f"• **مؤشر جاهزية الامتحانات الشامل:** **{exam_readiness}%**",
        f"• **ساعات النوم المسجلة:** {sleep_hours} ساعات (جودة الاستشفاء {sleep_quality}/15)",
        f"• **ساعات التركيز النقي:** {deep_focus} ساعات صافية خالية من المشتتات",
        f"• **التوصية الخاصة لك:** نظراً لأن ذروتك الحيوية في **{chronotype}**، احرص على استغلال وقت الصبح بدري للمادة الصعبة لتضمن أعلى حصيلة معرفية دون إرهاق."
    ]
    
    st.markdown("\n\n".join(report_lines))
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Cognitive OS Pro Deluxe — مشروع معرض العلوم المتقدم (الصف العاشر).")
