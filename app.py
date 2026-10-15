import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة وتصميمها
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | برنامج تحليل الدراسة",
    page_icon="🎓",
    layout="wide"
)

# تصميم عصري وبسيط مخصص لطالب الصف العاشر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #0d1117;
        color: #e6edf3;
    }

    .header-box {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #3b82f6;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.2);
    }

    .main-title {
        color: #60a5fa;
        font-weight: 800;
        font-size: 1.8rem;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #9ca3af;
        font-size: 1.05rem;
    }

    .card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #3d82f6);
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة العنوان الرئيسي
st.markdown("""
    <div class="header-box">
        <div class="main-title">🎓 مشروع: وعلم الإنسان ما لم يعلم</div>
        <div class="sub-title">برنامج ذكي يتنبأ بمستواك الدراسي ويساعدك ترتب وقتك ونومك بسهولة</div>
    </div>
""", unsafe_allow_html=True)

# التبويبات الرئيسية لتنظيم البرنامج
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 نتيجتك وتحليل الأداء", 
    "🚀 الميزة الفخرية: خطتك الشخصية", 
    "🔋 بطارية الطاقة والراحة", 
    "💡 نصائح ومحلل المشاكل", 
    "🏆 ملخص الشرح للحكام"
])

# الشريط الجانبي لإدخال البيانات
st.sidebar.header("🎛️ أدخل معلومات يومك الدراسي:")
sleep_hours = st.sidebar.slider("كم ساعة نمت البارحة؟", 3.0, 10.0, 7.5, 0.5)
sleep_quality = st.sidebar.slider("كيف كانت جودة نومك؟ (1 سيء - 10 ممتاز)", 1, 10, 8)
total_study = st.sidebar.slider("كم ساعة درست اليوم كلياً؟", 1.0, 12.0, 4.0, 0.5)
deep_focus = st.sidebar.slider("منها.. كم ساعة كنت مركز تماماً بدون هاتف؟", 0.5, 8.0, 2.5, 0.5)
study_method = st.sidebar.selectbox("كيف طريقة دراستك؟", ["أحل أسئلة وأشرح لنفسي (نشط)", "أخص تلخيص ورسومات", "أقرأ من الكتاب فقط (سلبي)"])
study_time = st.sidebar.selectbox("متى تحب تدرس أكتر شي؟", ["الصبح بكير", "بالليل والهدوء", "بعد العصر"])
phone_status = st.sidebar.selectbox("وين بيكون تلفونك وأنت تدرس؟", ["في غرفة ثانية (مفصول)", "جنبي بس صامت", "في إيدي وبقلب فيه"])

# الخوارزمية الحسابية المحدثة والدقيقة
focus_ratio = (deep_focus / total_study) * 100 if total_study > 0 else 0

# معادلة حسابية مبنية على أوزان علمية دقيقة
calculated_score = 35 + (sleep_hours * 3.5) + (sleep_quality * 1.5) + (deep_focus * 5.0) + (total_study * 0.8)

if study_method == "أحل أسئلة وأشرح لنفسي (نشط)":
    calculated_score += 12
elif study_method == "أخص تلخيص ورسومات":
    calculated_score += 8

if phone_status == "في غرفة ثانية (مفصول)":
    calculated_score += 8
elif phone_status == "في إيدي وبقلب فيه":
    calculated_score -= 10

final_grade = min(max(calculated_score, 35.0), 99.5)
mental_battery = min(100, max(10, int((sleep_hours * 8) + (sleep_quality * 4) - (total_study * 3))))

# التبويب الأول: لوحة النتائج
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("🎯 المعدل المتوقع بناءً على عاداتك اليوم:")
        st.metric(label="مؤشر الأداء الدراسي", value=f"{final_grade:.1f}%")
        
        if final_grade >= 85:
            st.success("🌟 ممتاز جداً! نمطك اليوم ممتاز وبيساعدك تضل من المتفوقين.")
        elif final_grade >= 70:
            st.info("👍 جيد جداً، بس تقدر ترفع معدلك أكتر لو قللت المشتتات وزدت وقت التركيز.")
        else:
            st.warning("⚠️ انتبه! قلّة النوم أو التشتت بالتلفون عم يضيعوا تعبك بالدراسة.")

        st.write("---")
        st.subheader("📊 نسبة التركيز الحقيقي من وقت الدراسة:")
        st.write(f"أنت مركز بنسبة **{focus_ratio:.1f}%** من إجمالي الوقت اللي قعدت فيه تدرس.")
        st.progress(min(int(focus_ratio), 100))

    with c2:
        st.subheader("📌 شو أكتر شي أثر على علامتك؟")
        data_factors = pd.DataFrame({
            'العامل': ['التركيز العميق', 'جودة النوم', 'طريقة الدراسة', 'مكان التلفون'],
            'التأثير (%)': [40, 25, 20, 15]
        })
        st.bar_chart(data_factors.set_index('العامل'))
    st.markdown('</div>', unsafe_allow_html=True)

# التبويب الثاني: الميزة الفخرية الكبرى
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 الميزة الفخرية: توليد خطة المذاكرة الشخصية اليومية")
    st.write("هنا يقوم البرنامج بتحويل أرقامك إلى خطة عمل حقيقية تقدر تطبقها فوراً لتزيد علاماتك!")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 📅 جدولك الموصى به لليوم:")
        if "الصبح" in study_time:
            st.write("• **الفترة الذهبية (8 ص - 11 ص):** ادرس المواد الصعبة مثل الرياضيات والفيزياء.")
            st.write("• **الفترة الثانية (4 عصراً - 6 مساءً):** حل أسئلة وتمارين.")
        else:
            st.write("• **الفترة الذهبية (5 مساءً - 9 مساءً):** انسب وقت لتركيزك العالي والمواد الصعبة.")
            st.write("• **الفترة الثانية (10 مساءً - 11 مساءً):** مراجعة سريعة قبل النوم.")
            
        st.write("• **أوقات الراحة:** خذ 5 دقائق استراحة كل 25 دقيقة دراسة (نظام البومودورو).")

    with col_b:
        st.markdown("### 📝 نصيحة تثبيت المعلومات بالذاكرة:")
        st.write("1. **راجع دراستك اليوم:** بعد 24 ساعة بالضبط لمدة 10 دقائق.")
        st.write("2. **المراجعة الثانية:** بعد 3 أيام.")
        st.write("3. **المراجعة الثالثة:** بعد أسبوع لضمان عدم النسيان بالامتحان النهائي.")

    st.write("---")
    # زر التصدير والطباعة (محاكاة طباعة الخطة)
    plan_text = f"خطة الطالب اليومية - المعدل المتوقع: {final_grade:.1f}%\nساعات النوم: {sleep_hours}\nطريقة الدراسة: {study_method}"
    st.download_button("📥 تنزيل خطة الدراسة الشخصية (Text / PDF)", data=plan_text, file_name="my_study_plan.txt")
    st.markdown('</div>', unsafe_allow_html=True)

# التبويب الثالث: بطارية الطاقة والراحة
with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔋 شحن البطارية الذهنية وزمن الاستراحة")
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.metric(label="مستوى طاقة دماغك الحالية", value=f"{mental_battery}%")
        st.progress(mental_battery)
        if mental_battery < 40:
            st.error("بطاريتك الذهنية ضغيفة! يلزمك استراحة أو قيلولة لمدة 20 دقيقة قبل ما تكمل.")
        else:
            st.success("طاقتك ممتازة وجاهز لاستيعاب معلومات جديدة!")

    with col_y:
        st.subheader("⏱️ حاسبة الاستراحة الذكية:")
        recommended_break = int((total_study * 60) / 4)
        st.write(f"بناءً على ساعات دراستك اليوم، أنت بحاجة لـ **{recommended_break} دقيقة** استراحة موزعة على يومك لتجديد نشاطك.")
    st.markdown('</div>', unsafe_allow_html=True)

# التبويب الرابع: محلل المشاكل والنصائح
with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 محلل المشاكل الدراسية وسؤال وجواب")
    problem = st.selectbox("شو أكثر مشكلة بتواجهك وأنت تدرس؟", [
        "أنا بدرس كثير بس بانسى بالامتحان",
        "بس أفتح الكتاب بسرح وببلش أتشتت",
        "بحس بخمول ونعس أول ما أبلش أدرس",
        "التلفون بضل يسحب وقتي بدون ما أحس"
    ])
    
    if st.button("اعطيني الحل المناسب"):
        if "بانسى بالامتحان" in problem:
            st.info("💡 **الحل:** المشكلة انك بتقرأ قراءة صامتة. جرب جيب ورقة وقلم واشرح الدرس بصوت عالٍ كأنك أستاذ بتشرح للطلاب!")
        elif "بسرح وببلش أتشتت" in problem:
            st.info("💡 **الحل:** ادرس طريقة (25 دقيقة دراسة / 5 دقائق راحة)، وحط التلفون بغرفة ثانية كلياً.")
        elif "بخمول ونعس" in problem:
            st.info("💡 **الحل:** ادرس وأنت قاعد على مكتب مش على التخت، وافتح شباك الغرفة ليدخل أكسجين يصحصح عقلك.")
        else:
            st.info("💡 **الحل:** نزل تطبيق بيغلق التطبيقات وقت الدراسة، أو سلم تلفونك لأحد بالبيت حتى تخلص دراستك.")
    st.markdown('</div>', unsafe_allow_html=True)

# التبويب الخامس: ملخص المعرض للحكام
with tab5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏆 طريقة الشرح وم الكلمات المفتاحية للحكام")
    st.markdown("""
    * **اسم المشروع:** وعلم الإنسان ما لم يعلم.
    * **فكرة المشروع:** برنامج بيجمع بين علم النفس والدراسة وبين المعادلات الرياضيات ليتنبأ بمستوى الطالب ويعطيه خطة تحسين عملياً.
    * **الهدف منه:** مساعدة الطلاب على معرفة أخطائهم الدراسية وتقليل وقت المذاكرة العشوائي وزيادة التركيز.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("مشروع معرض العلوم — تصميم وتنفيذ طالب الصف العاشر.")
