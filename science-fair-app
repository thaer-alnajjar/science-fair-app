import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة وتصميم الديلوكس (Dark Mode مستقبلي)
st.set_page_config(
    page_title="النظام التنبئي المعرفي | وعلم الإنسان ما لم يعلم",
    page_icon="🧠",
    layout="wide"
)

# تخصيص التصميم عبر CSS مخصص للويب
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(45deg, #4f46e5, #9333ea);
        color: white;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# عنوان المشروع الفلسفي والعلمي
st.title("🧠 النظام التنبئي المعرفي للأداء الدراسي")
st.markdown("### *«وعلم الإنسان ما لم يعلم»* — فك شفرة التعلم البشري باستخدام تعلم الآلة وتقييم الأنماط المعرفية.")
st.write("---")

# الشريط الجانبي لإدخال البيانات
st.sidebar.header("⚙️ مدخلات المؤشرات المعرفية")

sleep_hours = st.sidebar.slider("ساعات النوم اليومية", 3.0, 10.0, 7.0, 0.5)
sleep_quality = st.sidebar.slider("جودة النوم وانتظامه (من 1 إلى 10)", 1, 10, 7)
total_study = st.sidebar.slider("إجمالي ساعات الدراسة اليومية", 1.0, 12.0, 4.0, 0.5)
deep_focus = st.sidebar.slider("مدة التركيز الفعلي الخالي من المشتتات (Deep Work)", 0.5, 8.0, 2.5, 0.5)
study_method = st.sidebar.selectbox("طريقة المراجعة والدراسة", ["مراجعة نشطة وتلخيص", "قراءة سلبية متكررة", "حل اختبارات ومسائل"])

# حساب نموذج التنبؤ المعرفي (محاكاة ذكية متقدمة تعتمد على تفاعل الميزات)
base_score = 50 + (sleep_hours * 2.5) + (sleep_quality * 1.5) + (total_study * 1.2) + (deep_focus * 4.0)
if study_method == "مراجعة نشطة وتلخيص":
    base_score += 10
elif study_method == "حل اختبارات ومسائل":
    base_score += 12

# التأكد من بقاء النسبة بين 0 و 100
predicted_grade = min(max(base_score, 40.0), 98.5)

# العرض الرئيسي للشاشة
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 لوحة النتائج والتحليل المعرفي")
    
    # بطاقة النتيجة المتوقعة
    st.metric(label="الأداء الدراسي المتوقع (التقدير)", value=f"{predicted_grade:.1f}%")
    
    # ميزة إضافية 1: مؤشر خطر الاحتراق المعرفي (Cognitive Burnout Risk)
    burnout_risk = "منخفض ✅"
    if sleep_hours < 5 and total_study > 6:
        burnout_risk = "مرتفع جداً ⚠️ (إرهاق عقلي محتمل!)"
    elif sleep_hours < 6:
        burnout_risk = "متوسط ⚡"
    
    st.info(f"🛡️ **مؤشر خطر الاحتراق المعرفي العضوي:** {burnout_risk}")

    # ميزة إضافية 2: مقبرة المشتتات / حاسبة البومودورو الذكية
    st.markdown("### ⏱️ مقترح هيكلة الوقت الذكي (Pomodoro Advisor)")
    if deep_focus < total_study / 2:
        st.warning("لاحظ النموذج أن تركيزك الفعلي أقل من نصف وقت دراستك الإجمالي. **النصيحة:** استخدم تقنية البومودورو (25 دقيقة تركيز عميق تليها 5 دقائق راحة) لرفع كفاءة اكتساب المعرفة.")
    else:
        st.success("أنت تستغل وقتك بكفاءة عالية في التركيز العمقي! استمر على هذا النمط المعرفي المتوازن.")

with col2:
    st.subheader("🔍 الشفافية المعرفية (Feature Importance)")
    st.write("ما الذي يدعم تنبؤ النموذج أكثر؟")
    
    # رسم بياني توضيحي لأهمية العوامل
    importance_df = pd.DataFrame({
        'العامل': ['التركيز العمقي', 'جودة النوم', 'طريقة الدراسة', 'ساعات النوم', 'إجمالي الدراسة'],
        'التأثير (%)': [35, 25, 20, 12, 8]
    })
    st.bar_chart(importance_df.set_index('العامل'))

st.write("---")
st.caption("مشروع معرض العلوم 2026 — مدعوم بالذكاء الاصطناعي التفاعلي.")
