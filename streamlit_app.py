import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Quipli Intel Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- STYLING & SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python_icon_notext.svg/115px-Python_icon_notext.svg.png", width=50) # Placeholder for Logo
    st.title("Report Controls")
    st.markdown("**Period:** Nov 2025")
    st.markdown("**Source:** ML-Powered Call Analysis")
    
    # Interactive Filter Simulation
    st.divider()
    st.write("### Data Filters")
    region = st.selectbox("Region", ["Global (All)", "North America", "Europe", "APAC"])
    call_type = st.multiselect("Call Types", ["Sales", "Internal/Training"], default=["Sales", "Internal/Training"])
    
    st.info(f"Viewing data for: **{region}**")
    st.divider()
    st.caption("Point Rental Powered by Strive Software, Inc. [cite: 1]")

# --- MAIN HEADER ---
st.title("🛡️ Quipli Competitive Intelligence Report")
st.markdown("### Executive Leadership Team Briefing")
st.markdown("---")

# --- EXECUTIVE SUMMARY METRICS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Calls Analyzed", value="~25,000", delta=None)
with col2:
    st.metric(label="Substantive Quipli Calls", value="73", delta="0.29% of Total", delta_color="off")
with col3:
    st.metric(label="Verified Sales Calls", value="63", help="Excludes 10 internal/training calls")
with col4:
    # Custom HTML for the "Low Concern" badge
    st.markdown(
        """
        <div style="background-color:#d4edda; padding:10px; border-radius:5px; text-align:center;">
            <h4 style="color:#155724; margin:0;">VERDICT: LOW CONCERN</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown(" > *'Out of ~25,000 total calls, only 73 contain substantive Quipli discussions. This does not indicate a significant competitive threat.'* [cite: 7, 9]")

# --- TABS FOR DETAILED SECTIONS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Funnel & Threat Analysis", "🧱 Deal Blockers", "⚔️ Battlecard & Positioning", "🚀 Recommendations"])

# --- TAB 1: FUNNEL & THREATS ---
with tab1:
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("Call Volume Funnel")
        # Data for Funnel
        funnel_data = dict(
            number=[25000, 3229, 73, 63],
            stage=["Total Calls", "Competitive Mentions", "Quipli Discussions", "Sales Calls"]
        )
        fig_funnel = px.funnel(funnel_data, x='number', y='stage', title="Conversion to Competitive Threat")
        fig_funnel.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig_funnel, use_container_width=True)
        st.caption("Only 0.29% of calls contain substantive Quipli discussions ")

    with col_right:
        st.subheader("Threat Level Distribution (63 Sales Calls)")
        # Data for Donut Chart
        threat_data = pd.DataFrame({
            "Level": ["High Threat", "Medium Threat", "Low Threat"],
            "Count": [13, 40, 10],
            "Description": [
                "Prospect actively comparing/leaning toward Quipli",
                "Quipli mentioned but prospect open to POR",
                "Quipli dismissed or POR clearly preferred"
            ]
        })
        
        fig_donut = px.pie(
            threat_data, 
            values='Count', 
            names='Level', 
            title='Assessed Threat Level', 
            hole=0.4,
            color='Level',
            color_discrete_map={"High Threat": "#dc3545", "Medium Threat": "#ffc107", "Low Threat": "#28a745"},
            hover_data=['Description']
        )
        st.plotly_chart(fig_donut, use_container_width=True)
        st.caption("Only 20.6% of identified calls show a high competitive threat ")

    # Perception Keywords
    st.subheader("How Prospects Perceive Quipli")
    keywords = {"Website": 17, "Basic": 15, "Simple": 10, "Modern": 8} # Approximated from visual bar chart
    fig_bar = px.bar(
        x=list(keywords.values()), 
        y=list(keywords.keys()), 
        orientation='h', 
        title="Common Keywords in Prospect Statements",
        labels={'x': 'Frequency', 'y': 'Keyword'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("**Key Insight:** Quipli is perceived as 'modern' and 'website-first' - their core appeal but also their limitation. [cite: 58]")

# --- TAB 2: DEAL BLOCKERS ---
with tab2:
    st.subheader("Deal Blocker Analysis")
    st.markdown("Primary reasons cited by prospects in the 63 sales calls:")
    
    # Data from Page 3
    blocker_data = pd.DataFrame({
        "Reason": ["Timing/Contract", "Price Objection", "Switching Cost", "Comparing Alternatives", "Missing Features"],
        "Count": [17, 14, 14, 10, 7],
        "Details": [
            "Contract ends in Sept / Seasonal timing",
            "Monthly recurring costs / Setup fee friction",
            "Data migration / Training",
            "Corporate mandate / Need to see options",
            "Custom B2B pricing / Multi-location UI"
        ]
    })
    
    fig_blockers = px.bar(
        blocker_data, 
        x="Count", 
        y="Reason", 
        orientation='h', 
        text="Count", 
        hover_data=["Details"],
        color="Count",
        color_continuous_scale="Blues"
    )
    fig_blockers.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_blockers, use_container_width=True)
    
    with st.expander("See Raw Data for Blockers"):
        st.dataframe(blocker_data)

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
        * **Inventory:** Serialized asset tracking [cite: 66]
        """)
        
    with col_neg:
        st.error("⚠️ Where We Need to Improve")
        st.markdown("""
        * **UX:** Online booking perceived as less modern than Quipli [cite: 70]
        * **Pricing:** Seen as more expensive for small operators [cite: 72]
        * **Onboarding:** Quipli seen as easier to start [cite: 73]
        * **Fees:** Setup fee is a friction point [cite: 77]
        """)
    
    st.divider()
    st.subheader("Attack & Defend Strategies")
    
    # Creating a comparison table
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
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 1. Monitor, Don't Panic")
        st.caption("Impact: Low | Effort: Low")
        st.info("With only 0.29% of calls mentioning Quipli, this is not an urgent threat. Continue monitoring but do not over-invest. [cite: 123]")

        st.markdown("### 3. Leverage Operational Depth")
        st.caption("Impact: High | Effort: Low")
        st.info("In competitive situations, emphasize maintenance, reporting, and operational features where Quipli is weak. [cite: 131]")

    with c2:
        st.markdown("### 2. Strengthen Online Booking UX")
        st.caption("Impact: Medium | Effort: Medium")
        st.warning("When Quipli comes up, it's about their modern interface. Incremental improvements here neutralize their primary appeal. [cite: 128]")

        st.markdown("### 4. Refresh Win/Loss Analysis")
        st.caption("Impact: High | Effort: Medium")
        st.warning("Pull fresh SFDC data to determine actual win/loss rates. Current data is stale. [cite: 135]")

# --- FOOTER ---
st.divider()
st.caption("Confidential | Point of Rental Competitive Intelligence Report | Based on Document 'quipli-intel-dashboard.pdf'")