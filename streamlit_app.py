import streamlit as st
import pandas as pd
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Quipli Intel Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- STYLING & SIDEBAR ---
with st.sidebar:
    st.title("Report Controls")
    st.markdown("**Period:** Nov 2025")
    st.markdown("**Source:** ML-Powered Call Analysis")
    
    st.divider()
    st.write("### Data Filters")
    region = st.selectbox("Region", ["Global (All)", "North America", "Europe", "APAC"])
    call_type = st.multiselect("Call Types", ["Sales", "Internal/Training"], default=["Sales", "Internal/Training"])
    
    st.info(f"Viewing data for: **{region}**")
    st.divider()
    st.caption("Point Rental Powered by Strive Software, Inc.")

# --- MAIN HEADER ---
st.title("🛡️ Quipli Competitive Intelligence Report")
st.markdown("### Executive Leadership Team Briefing")
st.markdown("---")

# --- EXECUTIVE SUMMARY METRICS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Calls Analyzed", value="~25,000")
with col2:
    st.metric(label="Substantive Quipli Calls", value="73", delta="0.29% of Total", delta_color="off")
with col3:
    st.metric(label="Verified Sales Calls", value="63", help="Excludes 10 internal/training calls")
with col4:
    st.markdown(
        """
        <div style="background-color:#d4edda; padding:10px; border-radius:5px; text-align:center;">
            <h4 style="color:#155724; margin:0;">VERDICT: LOW CONCERN</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown(" > *'Out of ~25,000 total calls, only 73 contain substantive Quipli discussions[cite: 7]. This does not indicate a significant competitive threat.'*")

# --- TABS FOR DETAILED SECTIONS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Funnel & Threat Analysis", "🧱 Deal Blockers", "⚔️ Battlecard & Positioning", "🚀 Recommendations"])

# --- TAB 1: FUNNEL & THREATS ---
with tab1:
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("Call Volume Funnel")
        # Data for Funnel [cite: 16-22]
        funnel_data = pd.DataFrame({
            'Stage': ["Total Calls", "Competitive Mentions", "Quipli Discussions", "Sales Calls"],
            'Count': [25000, 3229, 73, 63]
        })
        
        # Using Altair for Funnel visualization (Native Streamlit)
        c = alt.Chart(funnel_data).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Stage:N', sort=None),
            tooltip=['Stage', 'Count']
        ).properties(title="Conversion to Competitive Threat")
        
        st.altair_chart(c, use_container_width=True)
        st.caption("Only 0.29% of calls contain substantive Quipli discussions [cite: 14]")

    with col_right:
        st.subheader("Threat Level Distribution")
        # Data for Donut Chart [cite: 49]
        threat_data = pd.DataFrame({
            "Level": ["High Threat", "Medium Threat", "Low Threat"],
            "Count": [13, 40, 10]
        })
        
        # Using Altair for Donut/Pie Chart
        base = alt.Chart(threat_data).encode(theta=alt.Theta("Count", stack=True))
        pie = base.mark_arc(outerRadius=120).encode(
            color=alt.Color("Level"),
            order=alt.Order("Count", sort="descending"),
            tooltip=["Level", "Count"]
        )
        st.altair_chart(pie, use_container_width=True)
        st.caption("Only 20.6% of identified calls show a high competitive threat [cite: 57]")

    # Perception Keywords
    st.subheader("How Prospects Perceive Quipli")
    # Data [cite: 52-54]
    keywords_data = pd.DataFrame({
        "Keyword": ["Website", "Basic", "Simple", "Modern"],
        "Frequency": [17, 15, 10, 8]
    })
    st.bar_chart(keywords_data.set_index("Keyword"), color="#FF4B4B")
    st.markdown("**Key Insight:** Quipli is perceived as 'modern' and 'website-first'[cite: 58].")

# --- TAB 2: DEAL BLOCKERS ---
with tab2:
    st.subheader("Deal Blocker Analysis")
    st.markdown("Primary reasons cited by prospects in the 63 sales calls[cite: 80]:")
    
    # Data from Page 3 [cite: 91-107]
    blocker_data = pd.DataFrame({
        "Reason": ["Timing/Contract", "Price Objection", "Switching Cost", "Comparing Alternatives", "Missing Features"],
        "Count": [17, 14, 14, 10, 7]
    })
    
    # Simple Streamlit Bar Chart
    st.bar_chart(blocker_data.set_index("Reason"))
    
    with st.expander("See Detail Context"):
        st.write("""
        * **Timing:** Contract ends in Sept / Seasonal timing
        * **Price:** Monthly recurring costs / Setup fee friction
        * **Switching:** Data migration / Training concerns
        * **Alternatives:** Corporate mandate / Need to see options
        """)

# --- TAB 3: BATTLECARD ---
with tab3:
    st.subheader("Competitive Positioning")
    
    col_pos, col_neg = st.columns(2)
    
    with col_pos:
        st.success("✅ Where POR Wins")
        st.markdown("""
        * **Industry Experience:** 43 years & customer trust [cite: 62]
        * **Operational Depth:** Maintenance, work orders [cite: 63]
        * **Reporting:** ROI, utilization, unit-level financials [cite: 64]
        * **Scalability:** From Essentials to Elite [cite: 65]
        """)
        
    with col_neg:
        st.error("⚠️ Where We Need to Improve")
        st.markdown("""
        * **UX:** Online booking perceived as less modern than Quipli [cite: 70]
        * **Pricing:** Seen as more expensive for small operators [cite: 72]
        * **Onboarding:** Quipli seen as easier to start [cite: 73]
        """)
    
    st.divider()
    st.subheader("Attack & Defend Strategies")
    
    # Comparison table [cite: 79]
    strategy_data = {
        "Area": ["Operational Depth", "Reporting", "Business Focus", "Track Record", "Serialized Assets"],
        "Quipli Weakness": [
            "Limited maintenance/work order functionality",
            "Weak reporting and analytics capabilities",
            "Website-first, operations second approach",
            "Untested at scale, newer company",
            "Treats serialized equipment tracking as nice-to-have"
        ],
        "POR Counter-Position": [
            "POR has deep maintenance workflows built for real operations",
            "Advanced ROI and utilization reporting in Elite",
            "We're operations experts who also do online booking",
            "43 years of proven deployments across all sizes",
            "Core capability with deep asset management"
        ]
    }
    st.table(pd.DataFrame(strategy_data))

# --- TAB 4: RECOMMENDATIONS ---
with tab4:
    st.subheader("Strategic Recommendations")
    # [cite: 119-135]
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 1. Monitor, Don't Panic")
        st.caption("Impact: Low | Effort: Low")
        st.info("With only 0.29% of calls mentioning Quipli, this is not an urgent threat. Continue monitoring but do not over-invest.")

        st.markdown("### 3. Leverage Operational Depth")
        st.caption("Impact: High | Effort: Low")
        st.info("In competitive situations, emphasize maintenance, reporting, and operational features where Quipli is weak.")

    with c2:
        st.markdown("### 2. Strengthen Online Booking UX")
        st.caption("Impact: Medium | Effort: Medium")
        st.warning("When Quipli comes up, it's about their modern interface. Incremental improvements here neutralize their primary appeal.")

        st.markdown("### 4. Refresh Win/Loss Analysis")
        st.caption("Impact: High | Effort: Medium")
        st.warning("Pull fresh SFDC data to determine actual win/loss rates. Current data is stale.")

# --- FOOTER ---
st.divider()
st.caption("Confidential | Point of Rental Competitive Intelligence Report")