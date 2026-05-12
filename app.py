import html

import joblib
import pandas as pd
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="NeuroSleep Insight",
    page_icon="N",
    layout="wide",
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("sleep_quality_model.pkl")


model = load_model()

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
        :root {
            --bg-0: #040711;
            --bg-1: #07111f;
            --bg-2: #111827;
            --card: rgba(9, 18, 34, 0.78);
            --card-strong: rgba(12, 24, 44, 0.92);
            --line: rgba(132, 204, 255, 0.18);
            --line-strong: rgba(125, 249, 232, 0.36);
            --text: #eef7ff;
            --muted: #9fb3c8;
            --cyan: #6ee7f9;
            --teal: #5eead4;
            --violet: #a78bfa;
            --green: #86efac;
            --amber: #facc15;
            --rose: #fb7185;
        }

        .stApp {
            background:
                linear-gradient(135deg, rgba(4, 7, 17, 0.98) 0%, rgba(7, 17, 31, 0.98) 42%, rgba(20, 12, 38, 0.98) 100%),
                linear-gradient(90deg, rgba(110, 231, 249, 0.12), rgba(134, 239, 172, 0.08));
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: rgba(4, 7, 17, 0.12);
        }

        [data-testid="stToolbar"] {
            right: 1rem;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, h4, p, label, span {
            letter-spacing: 0;
        }

        h1, h2, h3 {
            color: var(--text);
        }

        .hero {
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(110, 231, 249, 0.22);
            border-radius: 26px;
            padding: 2.4rem;
            margin-bottom: 1.4rem;
            background:
                linear-gradient(135deg, rgba(14, 36, 59, 0.92), rgba(35, 22, 62, 0.82)),
                linear-gradient(90deg, rgba(94, 234, 212, 0.13), rgba(167, 139, 250, 0.12));
            box-shadow: 0 24px 70px rgba(0, 0, 0, 0.38);
        }

        .hero:after {
            content: "";
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(110, 231, 249, 0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(94, 234, 212, 0.07) 1px, transparent 1px);
            background-size: 34px 34px;
            opacity: 0.55;
            pointer-events: none;
        }

        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 880px;
        }

        .kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.42rem 0.74rem;
            border-radius: 999px;
            color: var(--cyan);
            border: 1px solid rgba(110, 231, 249, 0.22);
            background: rgba(6, 15, 28, 0.72);
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .kicker-dot {
            width: 0.55rem;
            height: 0.55rem;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--teal), var(--violet));
            box-shadow: 0 0 18px rgba(94, 234, 212, 0.75);
        }

        .hero-title {
            font-size: clamp(2.3rem, 5vw, 4.4rem);
            line-height: 1;
            font-weight: 850;
            margin: 0 0 0.7rem 0;
            color: #f8fbff;
        }

        .hero-subtitle {
            font-size: clamp(1.08rem, 2.2vw, 1.5rem);
            color: var(--teal);
            font-weight: 700;
            margin-bottom: 0.9rem;
        }

        .hero-description {
            color: #c8d7e8;
            font-size: 1rem;
            line-height: 1.75;
            max-width: 820px;
            margin-bottom: 1.25rem;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
        }

        .chip {
            border: 1px solid rgba(255, 255, 255, 0.12);
            background: rgba(255, 255, 255, 0.055);
            border-radius: 999px;
            padding: 0.5rem 0.75rem;
            color: #dbeafe;
            font-size: 0.85rem;
        }

        .section-heading {
            margin: 1rem 0 0.75rem 0;
        }

        .section-heading h2 {
            margin: 0;
            font-size: 1.45rem;
        }

        .section-heading p {
            margin: 0.35rem 0 0 0;
            color: var(--muted);
            line-height: 1.6;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid rgba(110, 231, 249, 0.16);
            border-radius: 20px;
            background: rgba(8, 18, 33, 0.74);
            box-shadow: 0 18px 46px rgba(0, 0, 0, 0.28);
            padding: 0.6rem;
        }

        .input-card-title {
            color: #f8fbff;
            font-size: 1rem;
            font-weight: 800;
            margin: 0.25rem 0 0.15rem 0;
        }

        .input-card-note {
            color: var(--muted);
            font-size: 0.88rem;
            margin-bottom: 1rem;
        }

        [data-testid="stWidgetLabel"] p {
            color: #d8e7f7;
            font-weight: 650;
        }

        .stNumberInput input,
        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: rgba(2, 8, 23, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.22);
            color: var(--text);
            border-radius: 12px;
        }

        .stSlider [data-baseweb="slider"] {
            padding-top: 0.4rem;
        }

        div.stButton > button:first-child {
            border: 0;
            border-radius: 14px;
            padding: 0.8rem 1.1rem;
            background: linear-gradient(135deg, var(--cyan), var(--teal));
            color: #04111f;
            font-weight: 850;
            box-shadow: 0 14px 36px rgba(45, 212, 191, 0.22);
        }

        div.stButton > button:first-child:hover {
            color: #020617;
            border: 0;
            transform: translateY(-1px);
            box-shadow: 0 18px 42px rgba(110, 231, 249, 0.28);
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.55rem;
            padding: 0.45rem;
            border-radius: 18px;
            background: rgba(8, 18, 33, 0.68);
            border: 1px solid rgba(110, 231, 249, 0.13);
        }

        .stTabs [data-baseweb="tab"] {
            height: 2.8rem;
            border-radius: 13px;
            color: #a9bdd4;
            font-weight: 750;
            padding: 0 1rem;
        }

        .stTabs [aria-selected="true"] {
            background: rgba(110, 231, 249, 0.13);
            color: #f8fbff;
        }

        .result-grid,
        .insight-grid,
        .scale-grid,
        .risk-grid,
        .recommendation-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }

        .insight-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        .scale-grid {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }

        .risk-grid {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }

        .recommendation-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        .metric-card,
        .insight-card,
        .about-card,
        .quality-meter,
        .gauge-card,
        .risk-score-card,
        .recommendation-card,
        .empty-state {
            border: 1px solid rgba(110, 231, 249, 0.15);
            border-radius: 20px;
            background: rgba(8, 18, 33, 0.76);
            box-shadow: 0 18px 46px rgba(0, 0, 0, 0.24);
        }

        .metric-card {
            padding: 1rem;
            min-height: 142px;
        }

        .metric-label {
            color: var(--muted);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 0.55rem;
        }

        .metric-value {
            color: #f8fbff;
            font-size: 1.45rem;
            line-height: 1.2;
            font-weight: 850;
            margin-bottom: 0.55rem;
        }

        .metric-copy {
            color: #b6c7d9;
            font-size: 0.88rem;
            line-height: 1.5;
        }

        .accent-high {
            border-top: 3px solid var(--green);
        }

        .accent-moderate {
            border-top: 3px solid var(--amber);
        }

        .accent-low {
            border-top: 3px solid var(--rose);
        }

        .quality-meter {
            padding: 1.05rem 1.1rem;
            margin: 1rem 0 1.25rem 0;
        }

        .gauge-card {
            padding: 1.35rem;
            margin: 1.1rem 0;
            display: grid;
            grid-template-columns: minmax(190px, 250px) 1fr;
            gap: 1.4rem;
            align-items: center;
            background:
                radial-gradient(circle at 18% 20%, rgba(110, 231, 249, 0.15), transparent 28%),
                linear-gradient(135deg, rgba(8, 18, 33, 0.88), rgba(23, 15, 43, 0.86));
        }

        .gauge-ring {
            width: min(100%, 230px);
            aspect-ratio: 1;
            border-radius: 999px;
            display: grid;
            place-items: center;
            margin: 0 auto;
            background:
                radial-gradient(circle, rgba(6, 13, 27, 0.98) 0 58%, transparent 59%),
                conic-gradient(var(--gauge-color) var(--gauge-angle), rgba(148, 163, 184, 0.18) 0);
            box-shadow:
                inset 0 0 28px rgba(255, 255, 255, 0.04),
                0 0 34px rgba(94, 234, 212, 0.16);
        }

        .gauge-score {
            text-align: center;
        }

        .gauge-number {
            display: block;
            font-size: 2.5rem;
            line-height: 1;
            color: #f8fbff;
            font-weight: 900;
        }

        .gauge-total {
            display: block;
            color: var(--muted);
            font-size: 0.88rem;
            margin-top: 0.2rem;
        }

        .gauge-copy h3 {
            color: #f8fbff;
            font-size: 1.35rem;
            margin: 0 0 0.55rem 0;
        }

        .gauge-copy p {
            color: #bfd0e3;
            line-height: 1.65;
            margin: 0;
        }

        .risk-score-card,
        .recommendation-card {
            padding: 1rem;
        }

        .risk-value {
            font-size: 1.24rem;
            color: #f8fbff;
            font-weight: 850;
            line-height: 1.25;
            margin-bottom: 0.45rem;
        }

        .risk-label,
        .recommendation-label {
            color: var(--muted);
            font-size: 0.76rem;
            font-weight: 850;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }

        .risk-copy,
        .recommendation-copy {
            color: #b8c8dc;
            font-size: 0.88rem;
            line-height: 1.55;
        }

        .risk-band {
            display: inline-flex;
            align-items: center;
            margin-top: 0.7rem;
            border-radius: 999px;
            padding: 0.32rem 0.6rem;
            color: #eaf6ff;
            background: rgba(110, 231, 249, 0.1);
            border: 1px solid rgba(110, 231, 249, 0.18);
            font-size: 0.78rem;
            font-weight: 800;
        }

        .meter-top,
        .meter-scale {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
        }

        .meter-top {
            color: #eaf6ff;
            font-weight: 800;
            margin-bottom: 0.7rem;
        }

        .meter-scale {
            color: var(--muted);
            font-size: 0.8rem;
            margin-top: 0.55rem;
        }

        .meter-shell {
            height: 0.9rem;
            border-radius: 999px;
            background: rgba(148, 163, 184, 0.16);
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        .meter-fill {
            height: 100%;
            border-radius: 999px;
            transition: width 0.45s ease;
        }

        .meter-fill.high {
            background: linear-gradient(90deg, var(--teal), var(--green));
        }

        .meter-fill.moderate {
            background: linear-gradient(90deg, var(--amber), var(--teal));
        }

        .meter-fill.low {
            background: linear-gradient(90deg, var(--rose), var(--amber));
        }

        .insight-card,
        .about-card,
        .empty-state {
            padding: 1.25rem;
        }

        .insight-card h3,
        .about-card h3 {
            color: #f8fbff;
            font-size: 1.02rem;
            margin: 0 0 0.55rem 0;
        }

        .insight-card p,
        .about-card p,
        .empty-state p {
            color: #bfd0e3;
            line-height: 1.65;
            margin: 0;
        }

        .callout {
            border-left: 4px solid var(--teal);
            background: rgba(94, 234, 212, 0.08);
            border-radius: 16px;
            padding: 1rem 1.1rem;
            color: #d8f9f4;
            margin: 1rem 0;
        }

        .credit-card {
            border: 1px solid rgba(167, 139, 250, 0.24);
            border-radius: 18px;
            background: rgba(28, 20, 48, 0.72);
            padding: 1rem 1.1rem;
            margin-top: 1rem;
            color: #e9ddff;
            font-weight: 750;
        }

        @media (max-width: 900px) {
            .hero {
                padding: 1.55rem;
            }

            .result-grid,
            .insight-grid,
            .scale-grid,
            .risk-grid,
            .recommendation-grid,
            .gauge-card {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helper Functions
# -----------------------------
def interpret_sleep_quality(score):
    if score >= 8:
        return {
            "level": "High Sleep Quality",
            "performance": "High Performance Readiness",
            "fatigue": "Low Fatigue Risk",
            "attention": "Strong Attention Potential",
            "message": "The predicted sleep profile suggests strong recovery, better alertness, and a higher readiness for sustained cognitive work.",
            "brain": "Higher sleep quality is associated with more stable brain-state transitions, stronger memory consolidation, and more efficient communication between brain regions during rest.",
        }
    if score >= 6:
        return {
            "level": "Moderate Sleep Quality",
            "performance": "Moderate Performance Readiness",
            "fatigue": "Moderate Fatigue Risk",
            "attention": "Average Attention Potential",
            "message": "The predicted sleep profile indicates fair recovery, but stress, low activity, or short sleep may still reduce focus and productivity consistency.",
            "brain": "Moderate sleep quality can support basic recovery, while irregular sleep patterns may still weaken attention networks and reduce brain-network efficiency.",
        }
    return {
        "level": "Low Sleep Quality",
        "performance": "Low Performance Readiness",
        "fatigue": "High Fatigue Risk",
        "attention": "Reduced Attention Potential",
        "message": "The predicted sleep profile suggests elevated fatigue risk, reduced alertness, and lower readiness for sustained performance.",
        "brain": "Lower sleep quality may disrupt memory consolidation, circadian balance, and functional connectivity across regions involved in attention and executive control.",
    }


def score_band(score):
    if score >= 8:
        return "high"
    if score >= 6:
        return "moderate"
    return "low"


def styled_container():
    try:
        return st.container(border=True)
    except TypeError:
        return st.container()


def render_section_heading(title, body):
    st.markdown(
        f"""
        <div class="section-heading">
            <h2>{html.escape(title)}</h2>
            <p>{html.escape(body)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_result_cards(prediction, insight):
    band = score_band(prediction)
    meter_width = max(0, min(100, prediction * 10))
    cards = [
        (
            "Predicted Sleep Quality",
            f"{prediction:.2f} / 10",
            insight["level"],
        ),
        (
            "Performance Readiness",
            insight["performance"],
            "Estimated readiness for focused academic or professional work.",
        ),
        (
            "Fatigue Risk",
            insight["fatigue"],
            "Risk band inferred from the predicted sleep quality score.",
        ),
        (
            "Attention Level",
            insight["attention"],
            "Expected attention potential based on the current sleep profile.",
        ),
    ]
    card_markup = "".join(
        f"""
        <div class="metric-card accent-{band}">
            <div class="metric-label">{html.escape(label)}</div>
            <div class="metric-value">{html.escape(value)}</div>
            <div class="metric-copy">{html.escape(copy)}</div>
        </div>
        """
        for label, value, copy in cards
    )
    st.markdown(
        f"""
        <div class="result-grid">
            {card_markup}
        </div>
        <div class="quality-meter">
            <div class="meter-top">
                <span>Sleep Quality Meter</span>
                <span>{prediction:.2f} / 10</span>
            </div>
            <div class="meter-shell">
                <div class="meter-fill {band}" style="width: {meter_width:.0f}%;"></div>
            </div>
            <div class="meter-scale">
                <span>Recovery concern</span>
                <span>Stable readiness</span>
            </div>
        </div>
        <div class="callout">{html.escape(insight["message"])}</div>
        """,
        unsafe_allow_html=True,
    )


def render_sleep_quality_gauge(prediction, insight):
    band = score_band(prediction)
    gauge_angle = max(0, min(360, prediction * 36))
    gauge_color = {
        "high": "#86efac",
        "moderate": "#facc15",
        "low": "#fb7185",
    }[band]

    st.markdown(
        f"""
        <div class="gauge-card">
            <div class="gauge-ring" style="--gauge-angle: {gauge_angle:.0f}deg; --gauge-color: {gauge_color};">
                <div class="gauge-score">
                    <span class="gauge-number">{prediction:.1f}</span>
                    <span class="gauge-total">out of 10</span>
                </div>
            </div>
            <div class="gauge-copy">
                <h3>Sleep Quality Gauge</h3>
                <p>
                    {html.escape(insight["level"])} indicates the estimated recovery
                    quality from the current lifestyle and health profile. The gauge
                    provides a quick visual view of predicted sleep stability and
                    performance readiness.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def recovery_status(score):
    if score >= 8:
        return (
            "Restorative Recovery",
            "Sleep pattern suggests strong recovery support and stable daytime readiness.",
        )
    if score >= 6:
        return (
            "Partial Recovery",
            "Sleep pattern suggests usable recovery with some risk of focus fluctuation.",
        )
    return (
        "Recovery Strain",
        "Sleep pattern suggests reduced recovery and higher vulnerability to fatigue.",
    )


def render_performance_risk_score(prediction, insight):
    band = score_band(prediction)
    risk_load = max(0, min(100, round((10 - prediction) * 10)))
    recovery, recovery_copy = recovery_status(prediction)
    cards = [
        (
            "Fatigue Risk",
            insight["fatigue"],
            "Estimated fatigue exposure based on the predicted sleep-quality band.",
        ),
        (
            "Focus Level",
            insight["attention"],
            "Expected ability to sustain attention during study, work, and decision tasks.",
        ),
        (
            "Productivity Readiness",
            insight["performance"],
            "Estimated readiness for consistent cognitive and academic performance.",
        ),
        (
            "Recovery Status",
            recovery,
            recovery_copy,
        ),
    ]
    cards_markup = "".join(
        f"""
        <div class="risk-score-card accent-{band}">
            <div class="risk-label">{html.escape(label)}</div>
            <div class="risk-value">{html.escape(value)}</div>
            <div class="risk-copy">{html.escape(copy)}</div>
        </div>
        """
        for label, value, copy in cards
    )

    st.markdown(
        f"""
        <div class="section-heading">
            <h2>Performance Risk Score</h2>
            <p>Composite risk load: {risk_load}/100. Lower values indicate stronger recovery and readiness.</p>
        </div>
        <div class="risk-grid">
            {cards_markup}
        </div>
        <div class="risk-band">Risk band: {html.escape(band.title())}</div>
        """,
        unsafe_allow_html=True,
    )


def build_recommendations(prediction, user_inputs):
    recommendations = []

    if prediction < 6:
        recommendations.append(
            (
                "Recovery priority",
                "The predicted score is low. Prioritize consistent sleep timing, reduced evening stimulation, and recovery-focused routines before demanding cognitive work.",
            )
        )
    elif prediction < 8:
        recommendations.append(
            (
                "Stabilize sleep quality",
                "The predicted score is moderate. Small improvements in sleep duration, stress control, and daily activity may help move readiness into a stronger range.",
            )
        )
    else:
        recommendations.append(
            (
                "Maintain protective habits",
                "The predicted score is high. Continue the current sleep-supportive pattern and monitor stress or workload changes that could reduce recovery.",
            )
        )

    if user_inputs["sleep_duration"] < 7:
        recommendations.append(
            (
                "Low sleep duration",
                "Increase sleep opportunity toward 7-9 hours where possible. Short sleep can reduce attention stability and memory consolidation.",
            )
        )

    if user_inputs["stress_level"] >= 7:
        recommendations.append(
            (
                "High stress level",
                "Add a short pre-sleep downshift routine such as breathing, journaling, quiet reading, or reduced screen exposure before bed.",
            )
        )

    if user_inputs["physical_activity"] < 50:
        recommendations.append(
            (
                "Low physical activity",
                "Gradually increase daytime movement. Moderate activity is often associated with better sleep regulation and improved fatigue control.",
            )
        )

    if user_inputs["daily_steps"] < 6000:
        recommendations.append(
            (
                "Low daily steps",
                "Aim for more consistent walking or light movement across the day. Higher step counts may support circadian rhythm and recovery quality.",
            )
        )

    if user_inputs["heart_rate"] >= 85:
        recommendations.append(
            (
                "High heart rate",
                "Monitor workload, hydration, stress, and recovery patterns. If elevated resting heart rate persists, consider appropriate health guidance.",
            )
        )

    if user_inputs["sleep_disorder"] != "None":
        recommendations.append(
            (
                "Sleep disorder status",
                "Account for the selected sleep disorder when interpreting results. Persistent symptoms may require structured sleep assessment or clinical support.",
            )
        )

    return recommendations


def render_personalized_recommendations(prediction, user_inputs):
    recommendations = build_recommendations(prediction, user_inputs)
    cards_markup = "".join(
        f"""
        <div class="recommendation-card">
            <div class="recommendation-label">{html.escape(label)}</div>
            <div class="recommendation-copy">{html.escape(copy)}</div>
        </div>
        """
        for label, copy in recommendations
    )
    st.markdown(
        f"""
        <div class="section-heading">
            <h2>Personalized Recommendations</h2>
            <p>Guidance generated from the prediction result and the lifestyle indicators entered above.</p>
        </div>
        <div class="recommendation-grid">
            {cards_markup}
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <section class="hero">
        <div class="hero-content">
            <div class="kicker"><span class="kicker-dot"></span> Sleep neuroscience plus machine learning</div>
            <div class="hero-title">NeuroSleep Insight</div>
            <div class="hero-subtitle">Sleep Quality and Performance Prediction System</div>
            <p class="hero-description">
                NeuroSleep Insight predicts sleep quality from lifestyle and health-related features,
                then interprets the result through neuroscience concepts linked to attention,
                fatigue, productivity, functional connectivity, and dynamic brain-state stability.
            </p>
            <div class="chip-row">
                <span class="chip">Sleep pattern analysis</span>
                <span class="chip">Performance readiness</span>
                <span class="chip">Brain-network interpretation</span>
                <span class="chip">AI-assisted decision support</span>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Prediction",
        "Performance Insight",
        "Neuroscience Insight",
        "About Project",
    ]
)

# -----------------------------
# Prediction Tab
# -----------------------------
with tab1:
    render_section_heading(
        "Sleep Quality Prediction",
        "Enter the selected lifestyle and health indicators used by the trained model.",
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with styled_container():
            st.markdown(
                """
                <div class="input-card-title">Personal and Sleep Profile</div>
                <div class="input-card-note">Demographic, occupational, and sleep-duration factors.</div>
                """,
                unsafe_allow_html=True,
            )
            age = st.number_input("Age", min_value=10, max_value=100, value=25)
            gender = st.selectbox("Gender", ["Female", "Male"])
            occupation = st.selectbox(
                "Occupation",
                [
                    "Accountant",
                    "Doctor",
                    "Engineer",
                    "Lawyer",
                    "Manager",
                    "Nurse",
                    "Sales Representative",
                    "Salesperson",
                    "Scientist",
                    "Software Engineer",
                    "Teacher",
                ],
            )
            sleep_duration = st.number_input(
                "Sleep Duration (hours)",
                min_value=0.0,
                max_value=12.0,
                value=7.0,
                step=0.1,
            )
            stress_level = st.slider("Stress Level", min_value=1, max_value=10, value=5)

    with col2:
        with styled_container():
            st.markdown(
                """
                <div class="input-card-title">Lifestyle and Health Signals</div>
                <div class="input-card-note">Activity, cardiovascular, BMI, and sleep-disorder indicators.</div>
                """,
                unsafe_allow_html=True,
            )
            physical_activity = st.slider(
                "Physical Activity Level",
                min_value=0,
                max_value=100,
                value=50,
            )
            daily_steps = st.number_input(
                "Daily Steps",
                min_value=0,
                max_value=30000,
                value=7000,
                step=500,
            )
            heart_rate = st.number_input(
                "Heart Rate",
                min_value=40,
                max_value=150,
                value=75,
            )
            bmi_category = st.selectbox(
                "BMI Category",
                ["Normal", "Normal Weight", "Obese", "Overweight"],
            )
            sleep_disorder = st.selectbox(
                "Sleep Disorder",
                ["None", "Insomnia", "Sleep Apnea"],
            )

    input_data = pd.DataFrame(
        [
            {
                "Sleep_Duration": sleep_duration,
                "Stress_Level": stress_level,
                "Physical_Activity_Level": physical_activity,
                "Daily_Steps": daily_steps,
                "Heart_Rate": heart_rate,
                "Age": age,
                "Gender": gender,
                "BMI_Category": bmi_category,
                "Sleep_Disorder": sleep_disorder,
                "Occupation": occupation,
            }
        ]
    )

    button_col, _ = st.columns([1.1, 2.9])
    with button_col:
        predict_clicked = st.button(
            "Run Sleep Quality Prediction",
            use_container_width=True,
        )

    if predict_clicked:
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(10, prediction))
        insight = interpret_sleep_quality(prediction)

        st.session_state["prediction"] = prediction
        st.session_state["insight"] = insight
        st.session_state["user_inputs"] = {
            "sleep_duration": sleep_duration,
            "stress_level": stress_level,
            "physical_activity": physical_activity,
            "daily_steps": daily_steps,
            "heart_rate": heart_rate,
            "sleep_disorder": sleep_disorder,
        }

    if "prediction" in st.session_state:
        render_sleep_quality_gauge(
            st.session_state["prediction"],
            st.session_state["insight"],
        )
        render_result_cards(st.session_state["prediction"], st.session_state["insight"])
        render_performance_risk_score(
            st.session_state["prediction"],
            st.session_state["insight"],
        )
        if "user_inputs" in st.session_state:
            render_personalized_recommendations(
                st.session_state["prediction"],
                st.session_state["user_inputs"],
            )

# -----------------------------
# Performance Insight Tab
# -----------------------------
with tab2:
    render_section_heading(
        "Performance Insight",
        "The predicted score is translated into readiness, fatigue, and attention indicators.",
    )

    if "prediction" not in st.session_state:
        st.markdown(
            """
            <div class="empty-state">
                <p>Run a prediction first to view performance readiness, fatigue risk, and attention-level interpretation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        prediction = st.session_state["prediction"]
        insight = st.session_state["insight"]
        render_sleep_quality_gauge(prediction, insight)
        render_result_cards(prediction, insight)
        render_performance_risk_score(prediction, insight)
        if "user_inputs" in st.session_state:
            render_personalized_recommendations(
                prediction,
                st.session_state["user_inputs"],
            )

        st.markdown(
            """
            <div class="scale-grid">
                <div class="insight-card">
                    <h3>8.0 - 10.0</h3>
                    <p>High readiness: stronger recovery, lower fatigue burden, and better potential for sustained attention.</p>
                </div>
                <div class="insight-card">
                    <h3>6.0 - 7.9</h3>
                    <p>Moderate readiness: usable recovery with possible attention fluctuation under stress or workload.</p>
                </div>
                <div class="insight-card">
                    <h3>Below 6.0</h3>
                    <p>Lower readiness: higher fatigue risk and reduced reliability for prolonged cognitive performance.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# Neuroscience Insight Tab
# -----------------------------
with tab3:
    render_section_heading(
        "Neuroscience Insight",
        "A research-friendly interpretation layer connecting sleep quality with brain-network function.",
    )

    if "prediction" in st.session_state:
        st.markdown(
            f"""
            <div class="callout">
                Personalized brain-based interpretation: {html.escape(st.session_state["insight"]["brain"])}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="insight-grid">
            <div class="insight-card">
                <h3>Brain-State Stability</h3>
                <p>
                    Sleep supports transitions between neural states that regulate recovery,
                    alertness, and cognitive control. Better sleep quality may indicate more
                    stable overnight recovery and stronger daytime regulation.
                </p>
            </div>
            <div class="insight-card">
                <h3>Functional Connectivity</h3>
                <p>
                    Functional connectivity describes how brain regions coordinate activity.
                    Sleep disruption may reduce efficient communication among attention,
                    memory, and executive-control networks.
                </p>
            </div>
            <div class="insight-card">
                <h3>Memory and Attention</h3>
                <p>
                    Quality sleep contributes to memory consolidation and attentional control.
                    Lower sleep quality may make concentration less stable during learning,
                    problem solving, and demanding daily tasks.
                </p>
            </div>
            <div class="insight-card">
                <h3>Performance Implication</h3>
                <p>
                    The performance prediction is not a diagnosis. It is an academic
                    interpretation of how lifestyle-based sleep indicators may relate to
                    fatigue, productivity, and cognitive readiness.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# About Project Tab
# -----------------------------
with tab4:
    render_section_heading(
        "About Project",
        "Sleep pattern analysis and performance prediction with a neuroscience interpretation layer.",
    )

    st.markdown(
        """
        <div class="about-card">
            <p>
                NeuroSleep Insight was developed as part of an undergraduate Computer Science research project on sleep pattern analysis and performance prediction. The system combines lifestyle-based sleep data, machine learning, and neuroscience interpretation to predict sleep quality and explain how sleep may influence attention, fatigue, productivity, and brain-network function.
            </p>
            <br>
            <p>
                The machine learning component predicts sleep quality from selected lifestyle and health-related features, while the neuroscience section provides an explanatory layer based on concepts from fMRI functional connectivity and dynamic brain-state analysis.
            </p>
        </div>
        <div class="credit-card">
            Developed by Chibuikem Madugba<br>
            Research and innovation reference: Computer Oracle Inc.
        </div>
        """,
        unsafe_allow_html=True,
    )
