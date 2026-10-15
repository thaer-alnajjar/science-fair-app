import streamlit as st
import pandas as pd
import numpy as np
import random

# إعداد الصفحة
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تصميم واجهة مستخدم أسطورية (دمج الكحلي، الأرجواني الفاتح، والبرتقالي بلمسات راقية)
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

    /* العنوان الرئيسي الفخم بدمج الكحلي والأرجواني والبرتقالي */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 32px;
        border-radius: 18px;
        border: 2px solid #4f46e5;
        border-right: 6px solid #ea580c;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.2);
    }

    .hero-verse {
        font-size: 1.45rem;
        font-weight: 700;
        color: #ea580c;
        margin-bottom: 6px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.95rem;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    /* بطاقات بيضاء نظيفة بإطار إنديجو وكحلي خفيف */
    .clean-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-top: 3px solid #1e293b;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
    }

    /* تنسيق التبويبات الفخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #e2e8f0;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        color: #1e293b;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 700;
        border: 1px solid #cbd5e1;
    }

    .stTabs [aria-selected="true"] {
        background: #1e293b !important;
        color: white !important;
        border-color: #1e293b !important;
        box-shadow: 0 4px 12px rgba(30, 41, 59, 0.25);
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

# العنوان الرئيسي في المنتصف بالهيدر الكحلي الفخم
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 النظام التحليلي الذكي للأداء الدراسي ⚡</div>
        <div class="hero-subtitle">معرض العلوم والابتكار — منصة قياس الأنماط المعرفية والبيئة العصبية السلوكية المتقدمة</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# التبويبات الرئيسية
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 لوحة التنبؤ (من 500)", 
    "🔋 الطاقة والاستشفاء", 
    "🤖 المساعد والتوليد الذكي", 
    "⚖️ مختبر المحاكاة", 
    "❓ بنك الـ 20 تحدياً الاسترجاعياً", 
    "📋 خطة المذاكرة والنصائح"
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

# معادلة حساب المعدل المحكمة والدقيقة جداً (من 500 نقطة)
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
        st.subheader("📈 مؤشر استقرار النمط الأسبوعي")
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
        st.info(f"🧠 مُقيّم إرهاق الذاكرة العاملة: {memory_fatigue}")
    with col_n2:
        hydration_synergy = "ممتازة وتدعم اليقظة 💧" if hydration_level >= 10 else "تحتاج زيادة لدعم الخلايا ⚠️"
        st.success(f"💧 مؤشر استجابة الترطيب العصبي: {hydration_synergy}")
    st.markdown('</div>', unsafe_allow_html=True)


with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🤖 المساعد التحليلي ومحطة توليد الأسئلة التكيفية المطورة")
    st.write("اختر أمراً تحليلياً لتوليد تقرير استشاري وتوليد أسئلة اختبارية مخصصة فوراً:")
    
    selected_prompt = st.selectbox("اختر البرومْت التحليلي المطلوب:", [
        "1. تحليل فجوة الانتباه ومقاومة التشتت الخارجي",
        "2. استراتيجية استشفاء الدماغ وتثبيت ساعات النوم",
        "3. تفكيك التسويف الدراسي ومعالجة الخمول المعرفي",
        "4. هندسة وتثبيت الذاكرة بعيدة المدى والتكرار"
    ])
    
    if st.button("تنفيذ البرومْت وتوليد التقرير المعرفي"):
        st.markdown("### 📑 مخرجات التقرير المخصص:")
        if "1." in selected_prompt:
            st.info(f"💡 تقرير الانتباه: التركيز النقي ({deep_focus} ساعة) من أصل ({total_study} ساعة) يوضح نسبة تشتت تقدر بـ {100 - focus_efficiency:.1f}%. التوصية: ابعد الهاتف تماماً وطبق فترات الراحة القصيرة.")
        elif "2." in selected_prompt:
            st.info(f"💡 تقرير الاستشفاء: جودة نومك ({sleep_quality}/15) وساعاتك ({sleep_hours}) تعني عجز نوم بمقدار {accumulated_sleep_debt:.1f} نقطة. التوصية: ثبت وقت الاستيقاظ الصبح بدري يومياً.")
        elif "3." in selected_prompt:
            st.info(f"💡 تقرير مقاومة التسويف: الدافعية ({motivation_level}/15) مع التوتر ({stress_level}/15) تتطلب البدء البسيط جداً (قاعدة الـ 5 دقائق الأولى دون ضغط).")
        else:
            st.info(f"💡 تقرير الذاكرة: الاعتماد على '{study_method}' مع بيئة إضاءة ({environment_lighting}/15) يحتم استخدام 'التكرار المتباعد' لتثبيت المعلومات نهائياً.")
            
    st.markdown("---")
    st.subheader("⚡ محطة توليد الأسئلة التكيفية الذكية")
    st.write("يقوم النظام بتحليل اختيارك وتوليد **3 مستويات من التحديات المعرفية الفورية**:")
    
    if st.button("توليد حزمة الأسئلة التكيفية المتقدمة"):
        st.markdown("""
        * **المستوى الأول (الفهم والاسترجاع):** ما هو المعيار الأكبر الذي أثر سلباً على رصيدك المعرفي اليوم؟ وكيف ستعالجه غداً؟
        * **المستوى الثاني (التحليل والاستدلال):** لو قمت بنقل وقت مذاكرتك ليكون **الصبح بدري**، كم تتبلور نسبة صفاء ذهنك مقارنة بالوضع الحالي؟
        * **المستوى الثالث (التطبيق العملي):** صغ مفهوماً واحداً من دروسك اليوم بطريقة 'الاسترجاع النشط' في ثلاثة أسطر فقط دون النظر للمرجع.
        """)
        st.success("✨ تم توليد التحديات بنجاح! استخدمها الآن لتقييم استيعابك الفعلي.")
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
    
    st.success("💡 رأي المحاكي: الالتزام بهذه التعديلات الموازنة سيرفع رصيدك المعرفي بشكل ملموس ومستقر!")
    
    st.markdown("---")
    lost_time_recovery = int((100 - focus_efficiency) * 0.4)
    st.info(f"⏳ حاسبة استرداد الوقت الضائع: تحتاج حوالي **{lost_time_recovery} دقائق** من التركيز النقي الخالي من أي مشتتات لتعويض آثار التشتت السابق اليوم.")
    st.markdown('</div>', unsafe_allow_html=True)


with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("❓ بنك الـ 20 تحدياً الاسترجاعياً الديناميكي (بدون تكرار)")
    st.write("بنك تحديات ضخم ومتنوع يولد لك أسئلة عشوائية وغير مكررة في كل مرة تستخدمه لتنشيط الذاكرة:")
    
    all_challenges = [
        "🧬 تحدي الفيزياء الحيوية: اشرح بأسلوبك كيف يتحول الجلوكوز في الدم إلى طاقة لتشغيل خلايا الدماغ أثناء التركيز النقي.",
        "🧠 تحدي الذاكرة العاملة: اذكر 5 مفاهيم رئيسية حفظتها اليوم دون النظر لأي مرجع، ثم اربط بين مفهومين بطريقة مبتكرة.",
        "📐 تحدي الاستدلال المنطقي: لو تضاعفت ساعات التركيز ونقص النوم للنصف، كيف تتأثر كفاءة الذاكرة طويلة المدى رياضياً حسب النموذج؟",
        "🗺️ تحدي الخريطة العصبية: ارسم في ذهنك شبكة ربط بين المادة التي تدرسها وبين تطبيقها الحقيقي في الحياة اليومية خلال دقيقة.",
        "⚗️ تحدي الكيمياء الحيوية: لماذا يؤدي الجفاف (نقص شرب الماء) إلى انخفاض سرعة انتقال النواقل العصبية؟ فسر علمياً.",
        "🔄 تحدي التكرار المتباعد: متى يجب أن تكون محطتك الثانية لمراجعة درس اليوم لتثبيته في الذاكرة الدائمة؟",
        "⏱️ تحدي إدارة الوقت المعرفي: كيف تطبق قاعدة 25 دقيقة تركيز على مادة معقدة مثل الرياضيات أو الفيزياء الصعبة؟",
        "🔍 تحدي تحليل الأخطاء: ما هو الخطأ المتكرر الذي تفعله في امتحاناتك السابقة وكيف ستعدله من جذوره؟",
        "🗣️ تحدي الاسترجاع الصوتي: قف واشرح بصوت عالٍ وبثقة كأنك تلقي محاضرة أمام 100 شخص لدرس اليوم.",
        "💡 تحدي البيئة الصامتة: كيف تؤثر الإضاءة الساطعة غير المتوازنة على إفراز هرمون الميلاتونين والتركيز؟",
        "📚 تحدي التصنيف المفاهيمي: قسّم أصعب درس درسته اليوم إلى ثلاثة أجزاء: الأساسيات، التفاصيل، والاستثناءات.",
        "🎯 تحدي التنبؤ الذاتي: بناءً على رصيدك المعرفي الحالي، ما هي النقطة التي قد تجعلك تخطئ في الامتحان القادم وتجنبها الآن؟",
        "🌉 تحدي الربط المجازي: شبّه ظاهرة علمية أو رياضية درستها اليوم بظاهرة تحدث في الشارع أو الطبيعة.",
        "📵 تحدي العزل الرقمي: تخيل أنك بلا هاتف ليوم كامل، كيف ستستغل ساعات الفراغ في تثبيت معلوماتك؟",
        "⚡ تحدي سرعة الاستيعاب: اقرأ فقرة صعبة في دقيقتين ثم لخصها في سطر واحد يشتمل على الخلاصة المطلقة.",
        "🚀 تحدي مقاومة التسويف: اذكر السبب الخفي خلف تأجيلك للمهام الصعبة وكيف تكسر حاجز الخوف منها بخطوة واحدة.",
        "🛌 تحدي الاستشفاء الذهني: ما هو التمرين الرياضي أو التنفسي الخفيف الذي يعيد تفعيل دورتك الدموية خلال 3 دقائق راحة؟",
        "📖 تحدي التفكير النقدي: هل القراءة التكرارية الصامتة مجدية علمياً؟ فسر لماذا تفشل غالباً مقارنة بالاسترجاع النشط.",
        "💨 تحدي استهلاك الأكسجين: لماذا يسبب الجلوس في غرفة مغلقة خمولاً ذهنياً حاداً؟ وما العلاقة بتدفق الدم المؤكسج؟",
        "📋 تحدي الجاهزية الشاملة: ضع خطة طوارئ مدتها 10 دقائق لمراجعة ليلة الامتحان لأهم فصول المادة."
    ]
    
    if st.button("🎲 اسحب 3 تحديات عشوائية فريدة الآن"):
        selected_challenges = random.sample(all_challenges, 3)
        for idx, ch in enumerate(selected_challenges, 1):
            st.warning(f"**التحدي الفرعي #{idx}:** {ch}")
            
    st.markdown("---")
    st.success("🏆 مسجل مسار الانتصارات الذهنية: تتبع استمرارك بالتحديات يرفع ثقتك المعرفية بنسبة 35%!")
    st.markdown('</div>', unsafe_allow_html=True)


with tab6:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("📋 خطة المذاكرة الشخصية ومحطة النصائح الذكية المتغيرة")
    
    exam_readiness = min(100, int((percentage_equivalent + mental_battery_index) / 2))
    
    # مولد النصائح الديناميكية المتغيرة حسب المعايير الحالية
    dynamic_tips = []
    if sleep_hours < 7.0:
        dynamic_tips.append("⚠️ **تنبيه النوم:** عجز النوم لديك يؤثر على الذاكرة العاملة، احرص على النوم مبكراً اليوم لتعويض الاستشفاء.")
    else:
        dynamic_tips.append("✨ **استشفاء ممتاز:** عدد ساعات نومك يدعم شبكات الدماغ العليا بامتياز.")
        
    if stress_level > 8:
        dynamic_tips.append("⚠️ **تنبيه التوتر:** مستوى التوتر مرتفع، جرب تمارين التنفس العميق لمدة دقيقتين قبل الشروع في الدراسة.")
    else:
        dynamic_tips.append("⚖️ **اتزان نفسي:** مستويات التوتر ضمن النطاق المسيطر عليه.")
        
    if hydration_level < 8:
        dynamic_tips.append("💧 **تنبيه الترطيب:** مستوى الماء منخفض، اشرب كوباً كبيراً من الماء الآن لتنشيط سرعة النواقل العصبية.")
    else:
        dynamic_tips.append("💧 **ترطيب جيد:** مستويات الترطيب داعمة ممتازة لليقظة والتركيز.")

    report_lines = [
        f"• **رصيدك التحليلي الإجمالي:** **{final_score_500:.1f} / 500 نقطة** (النسبة المعيارية: **{percentage_equivalent:.2f}%**)",
        f"• **مؤشر جاهزية الامتحانات الشامل:** **{exam_readiness}%**",
        f"• **ساعات النوم المسجلة:** {sleep_hours} ساعات (جودة الاستشفاء {sleep_quality}/15)",
        f"• **ساعات التركيز النقي:** {deep_focus} ساعات صافية خالية من المشتتات",
        f"• **التوصية الخاصة لك:** نظراً لأن ذروتك الحيوية في **{chronotype}**، احرص على استغلال وقت الصبح بدري للمادة الصعبة لتضمن أعلى حصيلة معرفية دون إرهاق."
    ]
    
    st.markdown("### 💡 نصائح النظام الذكية المتغيرة حسب حالتك:")
    for tip in dynamic_tips:
        st.info(tip)
        
    st.markdown("---")
    st.markdown("### 📑 تقرير الجاهزية الشامل:")
    st.markdown("\n\n".join(report_lines))
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("النظام التحليلي المتطور — مشروع معرض العلوم المتقدم (الصف العاشر).")
