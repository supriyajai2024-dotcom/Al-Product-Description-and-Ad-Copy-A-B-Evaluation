import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from io import BytesIO
BASE=Path(__file__).parent
ads=pd.read_csv(BASE/"data/ad_variants.csv")
resp_path=BASE/"data/survey_responses.csv"
responses=pd.read_csv(resp_path) if resp_path.exists() else pd.DataFrame(columns=["response_id","is_genuine","preferred_ad_id","clarity_1_5","trustworthiness_1_5","appeal_1_5","consideration_1_5","why_selected","age_18_30","valid"])
if len(responses):
 for c in ["clarity_1_5","trustworthiness_1_5","appeal_1_5","consideration_1_5"]: responses[c]=pd.to_numeric(responses[c],errors="coerce")
 genuine=responses[responses.get("is_genuine",pd.Series(dtype=str)).astype(str).str.lower().isin(["true","1","yes"]) & responses.get("valid",pd.Series(dtype=str)).astype(str).str.lower().isin(["true","1","yes"])] if len(responses) else responses
st.set_page_config(page_title="EcoSip Capstone",page_icon="💧",layout="wide")
st.sidebar.title("CAPSTONE 21")
page=st.sidebar.radio("Navigate",["Project Overview","Ad Copy Library","Prompt Style Comparison","Survey Results","Results Dashboard","Verification Report","Before-and-After Analysis","Export and Final Report"])
st.sidebar.caption("Fictional product • Survey status: AWAITING DATA" if len(genuine)==0 else f"Genuine valid responses: {len(genuine)}")
if page=="Project Overview":
 st.title("AI Ad Copy Evaluation"); st.warning("AWAITING SURVEY DATA — no real participants or results are included. No winning style is declared.")
 st.write("Research question: Which AI-written ad copy performs best with real readers, and why?")
 st.markdown("EcoSip Smart Bottle is fictional. Allowed facts: reusable bottle; everyday use; suitable for students and office workers; water-level markings.")
 st.metric("Ad variants",len(ads)); st.metric("Genuine valid responses",len(genuine)); st.info("Target: at least 20 genuine volunteers. See docs/survey_methodology.md.")
elif page=="Ad Copy Library":
 st.title(page); q=st.text_input("Search copy"); sty=st.multiselect("Prompt style",ads.prompt_style.unique(),default=list(ads.prompt_style.unique())); d=ads[ads.prompt_style.isin(sty)]; d=d[d.astype(str).apply(lambda x:x.str.contains(q,case=False).any(),axis=1)] if q else d; st.dataframe(d,use_container_width=True,hide_index=True)
elif page=="Prompt Style Comparison":
 st.title(page); st.write("Prompt templates and variants are available in docs/prompt_library.md and data/ad_variants.csv."); st.dataframe(ads.groupby('prompt_style').size().rename('variant count'),use_container_width=True)
elif page in ["Survey Results","Results Dashboard"]:
 st.title(page)
 if len(genuine)==0: st.warning("No genuine valid responses available. Analysis is a template; findings pending.")
 else:
  st.metric("Genuine valid responses",len(genuine)); votes=genuine.preferred_ad_id.value_counts().rename_axis('ad_id').reset_index(name='votes').merge(ads[['ad_id','prompt_style']],on='ad_id',how='left'); st.plotly_chart(px.bar(votes,x='ad_id',y='votes',color='prompt_style',title='Votes by ad'),use_container_width=True); st.plotly_chart(px.bar(votes.groupby('prompt_style',as_index=False).votes.sum(),x='prompt_style',y='votes',title='Votes by prompting style'),use_container_width=True)
  cols=['clarity_1_5','trustworthiness_1_5','appeal_1_5','consideration_1_5']; st.dataframe(genuine[cols].mean().rename('mean rating').to_frame()); st.write("Written feedback"); st.write(genuine.why_selected.dropna().tolist())
 st.caption("Descriptive results only; no significance claim. Report shortfall if fewer than 20 genuine responses.")
elif page=="Verification Report":
 st.title(page); st.markdown((BASE/'docs/verification_report.md').read_text())
elif page=="Before-and-After Analysis":
 st.title(page); st.markdown((BASE/'docs/before_after.md').read_text())
else:
 st.title(page); st.write("Download files and read the one-page summary. Current sample size: ",len(genuine)); st.download_button("Download ad variants CSV",(BASE/'data/ad_variants.csv').read_bytes(),"ad_variants.csv","text/csv"); st.download_button("Download workbook",(BASE/'eco_capstone.xlsx').read_bytes(),"eco_capstone.xlsx","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"); st.download_button("Download one-page PDF",(BASE/'summary.pdf').read_bytes(),"summary.pdf","application/pdf"); st.info("Google Forms/Sheets integration was not configured or tested.")
