import streamlit as st
import matplotlib.pyplot as plt

# 제목
st.title("E-Factor 연도별 폐기물 감소율 비교")
st.subheader("Compare Waste Reduction Over Time: Organic Solvent vs Supercritical CO₂")

# 📸 이미지 표시 (파일명 정확히 Reality.jpg여야 함)
st.image("Reality.jpg", caption="Real-world impact of waste reduction", use_column_width=True)

# 연도 설정
years = [2000, 2010, 2020]

# 슬라이더로 E-factor 입력 받기
st.sidebar.header("Set E-Factors for Each Year")

e_organic = []
e_scCO2 = []

for year in years:
    e_org = st.sidebar.slider(f"유기용매 E-Factor ({year})", min_value=1, max_value=50, value=25 - (years.index(year) * 5))
    e_sc = st.sidebar.slider(f"초임계 CO₂ E-Factor ({year})", min_value=0, max_value=50, value=15 - (years.index(year) * 6))
    e_organic.append(e_org)
    e_scCO2.append(e_sc)

# 폐기물 감소 비율 계산
reduction_ratios = [((eo - esc) / eo) * 100 if eo != 0 else 0 for eo, esc in zip(e_organic, e_scCO2)]

# 그래프 시각화
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(years, reduction_ratios, marker='o', color='mediumseagreen', linewidth=2)
ax.set_title('Waste Reduction Over Time (scCO₂ vs Organic Solvent)', fontsize=12)
ax.set_xlabel('Year')
ax.set_ylabel('Waste Reduction Rate (%)')
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', alpha=0.6)

for x, y in zip(years, reduction_ratios):
    ax.text(x, y + 2, f'{y:.1f}%', ha='center', fontsize=9)

# 그래프 출력
st.pyplot(fig)
