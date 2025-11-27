import streamlit as st
import pandas as pd
import altair as alt
import time  # To simulate AI "thinking" time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Quipli Intel Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- HELPER: MOCK LLM ENGINE ---
def mock_llm_response(prompt):
    """
    Simulates an LLM RAG (Retrieval Augmented Generation) response 
    by looking for keywords in the user's prompt.
    """
    prompt_lower = prompt.lower()
    
    # Knowledge Base (Simulated RAG)
    if "calls" in prompt_lower and "total" in prompt_lower:
        return "Based on the dataset, we analyzed a total of **~25,000 calls**. Out of these, 3,229 had competitive mentions, but only **73** contained substantive discussions about Quipli."
    
    elif "threat" in prompt_lower or "concern" in prompt_lower:
        return "The overall verdict is **LOW CONCERN**. Only 0.29% of total calls mentioned Quipli significantly. The threat level breakdown is:\n- High Threat: 13 calls (20.6%)\n- Medium Threat: 40 calls (63.5%)\n- Low Threat: 10 calls (15.9%)"
    
    elif "weakness" in prompt_lower or "improve" in prompt_lower:
        return "Prospects perceive Quipli as having a more modern 'website-first' interface. We need to improve in these areas:\n1. Online Booking UX\n2. Pricing perception for small operators\n3. Onboarding simplicity"
    
    elif "win" in prompt_lower or "strength" in prompt_lower:
        return "We win against Quipli in **Operational Depth**. Our key strengths are:\n- 43 years of industry experience\n- Advanced ROI & Utilization reporting\n- Deep maintenance and work order workflows"
    
    elif "price" in prompt_lower or "cost" in prompt_lower:
        return "Price is a known friction point. 14 calls identified 'Price Objection' as a deal blocker, specifically regarding monthly recurring costs and setup fees during slow seasons."
    
    elif "summary" in prompt_lower or "executive" in prompt_lower:
        return "Here is the Executive Summary:\n\n**Verdict:** Low Concern.\n**Key Stat:** Only 73 calls (0.29%) out of 25k contained real Quipli discussions.\n**Action:** Monitor the situation, but do not over-invest. Focus on improving Online Booking UX to neutralize their main advantage."
    
    else:
        return "I can answer questions about call volume, threat levels, Quipli's weaknesses, or our winning strategies. Try asking: *'What is the threat level?'* or *'Why do we lose deals?'*"

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

st.markdown(" > *'Out of ~25,000 total calls, only 73 contain substantive Quipli discussions. This does not indicate a significant competitive threat.'*")

# --- TABS FOR DETAILED SECTIONS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Funnel & Threat Analysis", 
    "🧱 Deal Blockers", 
    "⚔️ Battlecard & Positioning", 
    "🚀 Recommendations",
    "💬 Chat with Data (Demo)"  # <--- NEW TAB
])

# --- TAB 1: FUNNEL & THREATS ---
with tab1:
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("Call Volume Funnel")
        # Data for Funnel
        funnel_data = pd.DataFrame({
            'Stage': ["Total Calls", "Competitive Mentions", "Quipli Discussions", "Sales Calls"],
            'Count': [25000, 3229, 73, 63]
        })
        
        c = alt.Chart(funnel_data).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Stage:N', sort=None),
            tooltip=['Stage', 'Count']
        ).properties(title="Conversion to Competitive Threat")
        
        st.altair_chart(c, use_container_width=True)
        st.caption("Only 0.29% of calls contain substantive Quipli discussions")

    with col_right:
        st.subheader("Threat Level Distribution")
        # Data for Donut Chart
        threat_data = pd.DataFrame({
            "Level": ["High Threat", "Medium Threat", "Low Threat"],
            "Count": [13, 40, 10]
        })
        
        base = alt.Chart(threat_data).encode(theta=alt.Theta("Count", stack=True))
        pie = base.mark_arc(outerRadius=120).encode(
            color=alt.Color("Level"),
            order=alt.Order("Count", sort="descending"),
            tooltip=["Level", "Count"]
        )
        st.altair_chart(pie, use_container_width=True)
        st.caption("Only 20.6% of identified calls show a high competitive threat")

    # Perception Keywords
    st.subheader("How Prospects Perceive Quipli")
    keywords_data = pd.DataFrame({
        "Keyword": ["Website", "Basic", "Simple", "Modern"],
        "Frequency": [17, 15, 10, 8]
    })
    st.bar_chart(keywords_data.set_index("Keyword"), color="#FF4B4B")
    st.markdown("**Key Insight:** Quipli is perceived as 'modern' and 'website-first'.")

# --- TAB 2: DEAL BLOCKERS ---
with tab2:
    st.subheader("Deal Blocker Analysis")
    st.markdown("Primary reasons cited by prospects in the 63 sales calls:")
    
    blocker_data = pd.DataFrame({
        "Reason": ["Timing/Contract", "Price Objection", "Switching Cost", "Comparing Alternatives", "Missing Features"],
        "Count": [17, 14, 14, 10, 7]
    })
    
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
        * **Industry Experience:** 43 years & customer trust
        * **Operational Depth:** Maintenance, work orders
        * **Reporting:** ROI, utilization, unit-level financials
        * **Scalability:** From Essentials to Elite
        """)
        
    with col_neg:
        st.error("⚠️ Where We Need to Improve")
        st.markdown("""
        * **UX:** Online booking perceived as less modern than Quipli
        * **Pricing:** Seen as more expensive for small operators
        * **Onboarding:** Quipli seen as easier to start
        """)
    
    st.divider()
    st.subheader("Attack & Defend Strategies")
    
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

# --- TAB 5: CHAT WITH DATA (NEW) ---
with tab5:
    st.subheader("💬 AI Analyst (Demo)")
    st.markdown("Ask questions about the competitive report. *Try asking: 'What is the threat level?' or 'How many calls were analyzed?'*")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add a welcome message
        st.session_state.messages.append({"role": "assistant", "content": "Hello! I have analyzed the Quipli Intelligence Report. What would you like to know?"})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask a question about the data..."):
        # 1. Display user message
        st.chat_message("user").markdown(prompt)
        # 2. Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 3. Generate response (Simulated)
        with st.chat_message("assistant"):
            with st.spinner("Analyzing report data..."):
                time.sleep(1) # Simulate delay
                response = mock_llm_response(prompt)
                st.markdown(response)
        
        # 4. Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- FOOTER ---
st.divider()
st.caption("Confidential | Point of Rental Competitive Intelligence Report | AI Demo Mode Active")