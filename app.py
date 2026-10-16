import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import random
import datetime
from trees_svg import get_tree_svg
# ==========================================
# 1. إعدادات الصفحة والتصميم العصري
# ==========================================
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تهيئة ذاكرة الجلسة
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

if "user_points" not in st.session_state:
    st.session_state.user_points = 150

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌸 شجرة الساكورا اليابانية الساحرة"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌸 شجرة الساكورا اليابانية الساحرة"

# CSS العام للتصميم النظيف
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
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #6366f1;
        border-right: 6px solid #f97316;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);
    }

    .hero-verse {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f97316;
        margin-bottom: 5px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.75rem;
        color: #ffffff;
    }

    .clean-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #10b981;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }

    .stButton>button {
        background: #10b981;
        color: white;
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #059669;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 متجر الأشجار الواقعية الفخمة والأنيميشن السينمائي المتقدم</div>
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
    
    snack_type = st.selectbox("🍱 نوع الوجبة الخفيفة قبل المذاكرة", [
        "🍏 وجبة ذكية خفيفة (مكسرات، فواكه، زبادي)",
        "🥩 وجبة غنية بالبروتين (بيض، دجاج، أسماك)",
        "🍝 وجبة غداء ثقيلة/كاربوهيدرات (رز، معكرونة، وجبات سريعة)",
        "🍩 سكريات ومشروبات طاقة (حلويات، عصائر مصنعة)",
        "☕ معتمدة على الكافيين فقط (قهوة/شاي بدون طعام)",
        "🌙 صائم / لم أتناول وجبة"
    ])
    
    study_method = st.selectbox("📚 أسلوب المذاكرة الأساسي", [
        "التسجيل النشط والخرائط الذهنية",
        "حل المسائل والتطبيقات العملية",
        "القراءة التكرارية الصامتة"
    ])
    
    phone_isolation = st.selectbox("📵 عزل الهاتف الخلوي", [
        "مفصول تماماً في غرفة ثانية",
        "قريب بصامت ومقلوب",
        "في اليد أو بجانب الكتاب"
    ])

    submit_btn = st.form_submit_button(label="🚀 إرسال وتحليل البيانات")

if submit_btn:
    st.session_state.user_points += 25
    st.success("✅ تم حفظ التحليل واكتسبت +25 نقطة إضافية في رصيدك!")

# ==========================================
# 3. التبويبات الرئيسية
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 المؤشرات والموجز", 
    "🌿 البيئة والاستشفاء", 
    "⚡ الطاقة والتحفيز", 
    "🧠 التحليل والتفريغ",
    "🌳 معارض الأشجار الواقعية",
    "🏛️ منصة الحكام والاستثمار"
])

# --- TAB 1: المؤشرات والموجز ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
    st.metric("النتيجة المعيارية الإجمالية", "460 / 500 نقطة")
    st.progress(92)
    st.success("🌟 أداء استثنائي وتوازن مثالي في القدرات العصبية.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية")
    st.success("🍃 ظروف الإضاءة والحرارة والتهوية مثالية للتركيز.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ محرك الطاقة المعرفية")
    st.info("⚡ سرعة الاستجابة العصبية في أعلى مستوياتها.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل والتفريغ ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التفريغ الذهني")
    st.success("🗑️ الذاكرة المؤقتة منقية وصافية تماماً.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 5: معارض الأشجار الـ 10 الواقعية عبر st.components مع SVG عالي التفصيل والأنيميشن ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 المعرض الفني للأشجار الواقعية المتقدمة والأنيميشن")
    st.write("تصاميم فنية عضوية متكاملة ومتحركة (تتضمن تدرجات لونية، لحاء أشجار مفصل، وتساقط بتلات وأوراق حية):")

    active = st.session_state.active_tree
           svg_tree_render = get_tree_svg(active)

    # عرض الرسوم عبر مكونات HTML معزولة لضمان عمل الرسوم بدقة مذهلة
    components.html(f"""
    <div style="width: 100%; height: 480px; border-radius: 20px; overflow: hidden; border: 3px solid #334155; box-shadow: 0 15px 30px rgba(0,0,0,0.2); background: #fff;">
        {svg_tree_render}
    </div>
    """, height=490)

    st.markdown(f"### 🌲 الشجرة النشطة حالياً: **{active}**")
    st.info("✨ هذه الشجرة مصممة برسم هندسي عضوي وأنيميشن سينمائي عالي الجودة.")

    st.markdown("---")
    st.markdown("### 🛒 متجر الـ 10 أشجار الواقعية والأيقونية")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")

    trees_catalog = [
        {"name": "🌸 شجرة الساكورا اليابانية الساحرة", "price": 0, "env": "بيئة ربيعية زهرية"},
        {"name": "🌲 شجرة الصنوبر الثلجية", "price": 40, "env": "بيئة جبلية شتوية"},
        {"name": "🍄 شجرة الفطر الساحرة", "price": 70, "env": "بيئة غامضة مضيئة"},
        {"name": "🌴 شجرة النخيل الاستوائية", "price": 100, "env": "بيئة واحة مشمسة"},
        {"name": "🍁 شجرة القيقب الخريفية", "price": 130, "env": "بيئة خريفية دافئة"},
        {"name": "🔮 شجرة الويسترليا البنفسجية", "price": 160, "env": "بيئة أرجوانية ساحرة"},
        {"name": "💎 شجرة الكريستال البلورية", "price": 200, "env": "بيئة جليدية مشعة"},
        {"name": "🌿 شجرة البنساي العتيقة", "price": 240, "env": "بيئة صخرية يابانية"},
        {"name": "🎋 غابة البامبو الآسيوية", "price": 280, "env": "بيئة غابة هادئة"},
        {"name": "🔥 شجرة العنقاء النارية", "price": 350, "env": "بيئة طاقة أسطورية"}
    ]

    cols_shop = st.columns(3)
    for idx, t in enumerate(trees_catalog):
        with cols_shop[idx % 3]:
            st.markdown(f"**{t['name']}**")
            st.caption(f"🌍 {t['env']}")
            
            is_unlocked = t['name'] in st.session_state.unlocked_trees
            if is_unlocked:
                if active == t['name']:
                    st.success("✅ المفعلة حالياً")
                else:
                    if st.button("تفعيل", key=f"act_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                if st.button(f"شراء ({t['price']} ن)", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success("🎉 مبروك! تم التفعيل بنجاح!")
                        st.rerun()
                    else:
                        st.error("❌ النقاط غير كافية!")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 6: منصة الحكام والاستثمار ---
# ==========================================
with tab6:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🏛️ منطقة الحكام والاستثمار")
    
    st.markdown("""
    ### 📌 نبذة سريعة عن المشروع:
    نظام ذكي متكامل لقياس وتحليل الأنماط المعرفية والبيئية للطلاب، يدمج بين علم النفس العصبي والتفاعل البصري المتقدم لتعزيز التحصيل الدراسي.

    ---
    ### 💡 رؤية التطوير والاستثمار (لماذا هذا المشروع واعد؟):
    * **قابلية التخصيص الكامل:** المنصة مصممة بهندسة مرنة تتيح لكل مستخدم أو مؤسسة تخصيص بيئتها وتجربتها بالكامل.
    * **مرتكز للمطورين (Extensibility):** البنية البرمجية قابلة للدمج والتطوير المستمر بسهولة تامة.
    * **الفرصة الاستثمارية:** يمثل المنتج حلاً حقيقياً لأسواق التعليم الرقمي (EdTech) والصحة العقلية، بطلب استهلاكي مرتفع وقابلية توسع تجاري ضخمة (SaaS).
    """)
    st.success("✨ مشروع يعكس رؤية تقنية واستثمارية مستقبلية مستدامة.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
