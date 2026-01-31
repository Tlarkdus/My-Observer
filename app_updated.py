
"""
My Observer - Streamlit Web App
불안 관리를 위한 Activity & 음악 추천 시스템
"""

import streamlit as st
from recommendation import get_full_recommendation
from music_database import MUSIC_DATABASE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 한글 폰트 설정
try:
    plt.rc('font', family='Malgun Gothic')  # Windows
except:
    try:
        plt.rc('font', family='AppleGothic')  # Mac
    except:
        pass
plt.rcParams['axes.unicode_minus'] = False

# ========== 데이터 로드 ==========
@st.cache_data
def load_data():
    """엑셀 데이터 로드"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'Do Not Predict, Just Observe.xlsx')
    
    try:
        data = pd.read_excel(data_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.set_index('Date').sort_index()
        data['delta'] = data['Before'] - data['After']
        
        # 이동평균
        data['Before_MA7'] = data['Before'].rolling(window=7, min_periods=1).mean()
        data['After_MA7'] = data['After'].rolling(window=7, min_periods=1).mean()
        data['Delta_MA7'] = data['delta'].rolling(window=7, min_periods=1).mean()
        
        # 시간 변수
        data['weekday'] = data.index.dayofweek
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        data['weekday_name'] = data['weekday'].apply(lambda x: weekday_names[x])
        data['hour'] = data.index.hour
        
        def get_time_period(hour):
            if 6 <= hour < 12:
                return 'Morning'
            elif 12 <= hour < 18:
                return 'Afternoon'
            elif 18 <= hour < 24:
                return 'Evening'
            else:
                return 'Night'
        
        data['time_period'] = data['hour'].apply(get_time_period)
        
        return data
    except:
        return None

# ========== 페이지 설정 ==========
st.set_page_config(
    page_title="My Observer",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 데이터 로드
data = load_data()

# ========== 메인 타이틀 ==========
st.title("🧘 My Observer")
st.subheader("Don't Predict, Just Observe")
st.markdown("---")

# ========== 사이드바 메뉴 ==========
st.sidebar.title("📋 Menu")
page = st.sidebar.radio(
    "페이지 선택",
    ["🏠 홈", "📊 데이터 분석", "🎯 추천 받기", "ℹ️ About"]
)

# ========== 페이지 1: 홈 ==========
if page == "🏠 홈":
    st.header("Welcome to My Observer! 👋")
    
    st.markdown("""
    ### 📖 프로젝트 소개
    
    **My Observer**는 불안 관리를 위한 데이터 기반 추천 시스템입니다.
    
    #### 🎯 주요 기능:
    
    1. **Activity 추천**
       - 현재 불안 수준, 요일, 시간대, 가용 시간을 고려한 맞춤 추천
       - Breathing (빠른 개입) vs Other (깊은 개입)
    
    2. **음악 추천**
       - Other Activity 선택 시 불안 수준에 맞는 음악 추천
       - YouTube 링크로 바로 재생 가능
       - 클래식, 앰비언트, 재즈, Lo-fi 등 다양한 장르
    
    3. **데이터 기반 의사결정**
       - 50개의 실제 데이터 분석 결과 반영
       - Phase 2 분석에서 도출한 인사이트 적용
    
    #### 💡 사용 방법:
    
    1. 왼쪽 사이드바에서 원하는 메뉴 선택
    2. **"📊 데이터 분석"**: Phase 2 분석 결과 확인
    3. **"🎯 추천 받기"**: Activity & 음악 추천
    
    ---
    
    ### 📊 프로젝트 배경
    
    **"Don't Predict, Just Observe"**
    
    이 프로젝트는 예측보다는 **관찰**에 집중합니다.
    - 2주간의 불안 데이터 수집 (50개 데이터)
    - 패턴 발견 및 인사이트 도출
    - 증거 기반 추천 시스템 구축
    
    """)
    
    if st.button("시작하기", type="primary", use_container_width=True):
        st.rerun()

# ========== 페이지 2: 데이터 분석 ==========
elif page == "📊 데이터 분석":
    st.header("📊 Phase 2: 데이터 분석 결과")
    
    if data is None:
        st.error("⚠️ 데이터를 불러올 수 없습니다. 데이터 파일 경로를 확인해주세요.")
    else:
        st.success(f"✅ 데이터 로드 완료! (총 {len(data)}개)")
        
        # 탭으로 구분
        tab1, tab2, tab3, tab4 = st.tabs(["📈 시계열 분석", "📊 효과 분석", "🕐 시간 패턴", "🔗 상관관계"])
        
        # ===== Tab 1: 시계열 분석 =====
        with tab1:
            st.subheader("2.1 Time Series Analysis")
            
            fig, axes = plt.subplots(1, 2, figsize=(16, 6))
            
            # 왼쪽: Before/After
            axes[0].plot(data.index, data['Before'], marker='o', markersize=3, 
                        color='black', linewidth=1, label='Before', alpha=0.7)
            axes[0].plot(data.index, data['After'], marker='o', markersize=3,
                        color='darkred', linewidth=1, label='After', alpha=0.7)
            axes[0].plot(data.index, data['Before_MA7'], color='gray', 
                        linewidth=2, linestyle='--', label='Before (7-day MA)')
            axes[0].plot(data.index, data['After_MA7'], color='tomato',
                        linewidth=2, linestyle='--', label='After (7-day MA)')
            axes[0].set_title('Anxiety Level Over Time', fontsize=14, weight='bold')
            axes[0].set_xlabel('Date')
            axes[0].set_ylabel('Anxiety Level (1-10)')
            axes[0].legend()
            axes[0].grid(alpha=0.3)
            axes[0].tick_params(axis='x', rotation=45)
            
            # 오른쪽: Delta
            mean_delta = data['delta'].mean()
            axes[1].plot(data.index, data['delta'], marker='o', markersize=3,
                        color='blue', linewidth=1, label='Delta', alpha=0.7)
            axes[1].plot(data.index, data['Delta_MA7'], color='cornflowerblue',
                        linewidth=2, linestyle='--', label='Delta (7-day MA)')
            axes[1].axhline(y=mean_delta, color='green', linestyle='-',
                           linewidth=2, label=f'Mean ({mean_delta:.2f})')
            axes[1].set_title('Improvement (Delta) Over Time', fontsize=14, weight='bold')
            axes[1].set_xlabel('Date')
            axes[1].set_ylabel('Delta (Before - After)')
            axes[1].legend()
            axes[1].grid(alpha=0.3)
            axes[1].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown("""
            **💡 주요 발견:**
            - Before는 5~9 사이 변동
            - After는 1~5로 확실히 낮음
            - 평균 Delta 3.28 (안정적인 효과)
            """)
        
        # ===== Tab 2: 효과 분석 =====
        with tab2:
            st.subheader("2.2 Effectiveness Analysis")
            
            activity_stats = data.groupby('Activity')['delta'].agg(['count', 'mean', 'std']).round(2)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            activities = ['Breathing', 'Other']
            stats = activity_stats.loc[activities]
            
            bars = ax.bar(stats.index, stats['mean'], yerr=stats['std'],
                         capsize=10, alpha=0.8, color=['steelblue', 'coral'],
                         edgecolor='black', linewidth=1.5)
            
            for i, (activity, row) in enumerate(stats.iterrows()):
                ax.text(i, row['mean'] + row['std'] + 0.3,
                       f"n={int(row['count'])}", ha='center', fontsize=11, weight='bold')
            
            ax.axhline(y=mean_delta, color='green', linestyle='--',
                      linewidth=2, label=f'Overall Mean ({mean_delta:.2f})')
            ax.set_title('Effectiveness by Activity', fontsize=14, weight='bold')
            ax.set_xlabel('Activity')
            ax.set_ylabel('Average Delta')
            ax.legend()
            ax.grid(axis='y', alpha=0.3)
            
            st.pyplot(fig)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Breathing 평균 효과", f"{stats.loc['Breathing', 'mean']:.2f}")
            with col2:
                st.metric("Other 평균 효과", f"{stats.loc['Other', 'mean']:.2f}")
            
            st.markdown("""
            **💡 주요 발견:**
            - Breathing: 짧고 안정적 (1.4분, Delta 3.16)
            - Other: 시간 걸리지만 효과 큼 (19.5분, Delta 4.00)
            - 두 Activity 모두 통계적으로 유의미 (p < 0.05)
            """)
        
        # ===== Tab 3: 시간 패턴 =====
        with tab3:
            st.subheader("2.3 Temporal Pattern Analysis")
            
            fig, axes = plt.subplots(1, 2, figsize=(16, 6))
            
            # 요일별
            weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            weekday_delta = data.groupby('weekday_name')['delta'].mean().reindex(weekday_order)
            
            axes[0].bar(weekday_order, weekday_delta, color='steelblue', alpha=0.8, edgecolor='black')
            axes[0].axhline(y=mean_delta, color='green', linestyle='--', linewidth=2)
            axes[0].set_title('Delta by Weekday', fontsize=14, weight='bold')
            axes[0].set_xlabel('Weekday')
            axes[0].set_ylabel('Average Delta')
            axes[0].tick_params(axis='x', rotation=45)
            axes[0].grid(axis='y', alpha=0.3)
            
            # 시간대별
            time_order = ['Morning', 'Afternoon', 'Evening']
            time_delta = data.groupby('time_period')['delta'].mean().reindex(time_order)
            
            axes[1].bar(time_order, time_delta, color='coral', alpha=0.8, edgecolor='black')
            axes[1].axhline(y=mean_delta, color='green', linestyle='--', linewidth=2)
            axes[1].set_title('Delta by Time Period', fontsize=14, weight='bold')
            axes[1].set_xlabel('Time Period')
            axes[1].set_ylabel('Average Delta')
            axes[1].grid(axis='y', alpha=0.3)
            
            plt.tight_layout()
            st.pyplot(fig)
            
            st.markdown("""
            **💡 주요 발견:**
            - 토요일 효과가 가장 좋음 (3.57)
            - 아침 시간대 효과가 가장 높음 (3.38)
            - 수요일은 불안 높지만 효과는 낮음
            """)
        
        # ===== Tab 4: 상관관계 =====
        with tab4:
            st.subheader("2.4 Duration vs Delta Correlation")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Activity별 색상
            colors = {'Breathing': 'steelblue', 'Other': 'coral', 'Physical': 'gray'}
            for activity in data['Activity'].unique():
                activity_data = data[data['Activity'] == activity]
                ax.scatter(activity_data['Duration(min)'], activity_data['delta'],
                          label=f'{activity} (n={len(activity_data)})',
                          color=colors.get(activity, 'gray'),
                          s=100, alpha=0.6, edgecolors='black')
            
            # 전체 추세선
            z = np.polyfit(data['Duration(min)'], data['delta'], 1)
            p = np.poly1d(z)
            x_line = np.linspace(data['Duration(min)'].min(), data['Duration(min)'].max(), 100)
            corr = data['Duration(min)'].corr(data['delta'])
            ax.plot(x_line, p(x_line), "r:", linewidth=2, label=f'Trend (r={corr:.3f})')
            
            ax.set_title('Duration vs Delta', fontsize=14, weight='bold')
            ax.set_xlabel('Duration (min)')
            ax.set_ylabel('Delta (Before - After)')
            ax.legend()
            ax.grid(alpha=0.3)
            
            st.pyplot(fig)
            
            st.markdown(f"""
            **💡 주요 발견:**
            - 전체 상관계수: {corr:.3f} (중간 정도 양의 상관)
            - Breathing: 짧아도 효과 일정
            - Other: 시간 투자할수록 효과 증가
            """)

# ========== 페이지 3: 추천 받기 ==========
elif page == "🎯 추천 받기":
    st.header("🎯 Activity & 음악 추천")
    
    st.markdown("현재 상태를 입력하면 가장 적합한 Activity와 음악을 추천해드립니다.")
    
    st.markdown("### 📝 현재 상태 입력")
    
    col1, col2 = st.columns(2)
    
    with col1:
        anxiety_level = st.slider("😰 현재 불안 수준", 1, 10, 5, help="1: 매우 낮음 ~ 10: 매우 높음")
        weekday = st.selectbox("📅 요일", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    
    with col2:
        time_period = st.selectbox("🕐 시간대", ["Morning", "Afternoon", "Evening"])
        available_time = st.slider("⏰ 사용 가능한 시간 (분)", 1, 60, 10)
    
    with st.expander("🎵 음악 선호도 (선택사항)"):
        music_pref = st.selectbox("선호하는 음악 장르",
            ["선호 없음", "차분한 클래식", "앰비언트/명상", "자연의 소리", 
             "어쿠스틱/인디", "부드러운 피아노", "Lo-fi Hip Hop",
             "재즈", "보사노바", "칠 일렉트로닉"])
        
        pref_mapping = {
            "선호 없음": None, "차분한 클래식": "calm_classical", "앰비언트/명상": "ambient",
            "자연의 소리": "nature_sounds", "어쿠스틱/인디": "acoustic", "부드러운 피아노": "soft_piano",
            "Lo-fi Hip Hop": "lofi", "재즈": "jazz", "보사노바": "bossa_nova", "칠 일렉트로닉": "chill_electronic"
        }
        music_preference = pref_mapping[music_pref]
    
    st.markdown("---")
    if st.button("🎯 추천 받기", type="primary", use_container_width=True):
        
        with st.spinner("추천을 생성하고 있습니다..."):
            recommendation = get_full_recommendation(
                anxiety_level=anxiety_level, weekday=weekday, time_period=time_period,
                available_time=available_time, music_database=MUSIC_DATABASE,
                recommendation_version='score', music_preference=music_preference
            )
        
        st.success("✅ 추천이 완료되었습니다!")
        
        st.markdown("---")
        st.markdown("## 🎯 Activity 추천")
        
        activity = recommendation['activity']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("추천 Activity", activity['activity'])
        with col2:
            st.metric("권장 시간", activity['duration'])
        with col3:
            st.metric("예상 효과", f"△ {activity['expected_delta']:.1f}")
        
        if 'breathing_score' in activity:
            st.markdown("### 📊 추천 점수")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Breathing", f"{activity['breathing_score']}점")
            with col2:
                st.metric("Other", f"{activity['other_score']}점")
            with col3:
                st.metric("확신도", f"{activity['confidence']}점 차이")
        
        st.markdown("### 💡 추천 이유")
        for reason in activity['reason']:
            st.markdown(f"- {reason}")
        
        if activity.get('tips'):
            st.markdown("### 💬 Tips")
            for tip in activity['tips']:
                st.info(tip)
        
        if recommendation['music']:
            st.markdown("---")
            st.markdown("## 🎵 음악 추천")
            
            music = recommendation['music']
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**카테고리:** {music['category']}")
                st.markdown(f"**BPM:** {music['bpm_range']}")
            with col2:
                st.markdown(f"**플레이리스트:** {', '.join(music['playlists'])}")
                st.markdown(f"**총 재생 시간:** 약 {music['total_duration']}분")
            
            st.markdown("### 🎧 추천 곡")
            
            for i, track in enumerate(music['tracks'], 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{i}. {track['title']}** - {track['artist']}")
                        st.caption(f"⏱️ {track['duration']}")
                    with col2:
                        st.link_button("▶️ 재생", track['youtube'], use_container_width=True)
                    st.markdown("")
            
            if music.get('tips'):
                st.markdown("### 💬 음악 듣기 Tips")
                for tip in music['tips']:
                    st.info(tip)
        else:
            st.markdown("---")
            st.info("ℹ️ Breathing 활동에는 음악 추천이 제공되지 않습니다. 짧은 시간 집중적으로 호흡에만 집중해보세요!")

# ========== 페이지 4: About ==========
elif page == "ℹ️ About":
    st.header("ℹ️ About This Project")
    
    st.markdown("""
    ### 📊 프로젝트 구조
    
    #### Phase 1: Data Foundation
    - 데이터 수집 및 검증
    - 기본 전처리 및 시각화
    
    #### Phase 2: EDA & Insight
    - **2.1 Time Series Analysis**: 시간에 따른 불안 변화 패턴
    - **2.2 Effectiveness Analysis**: Activity 효과 통계 검증
    - **2.3 Temporal Pattern Analysis**: 요일/시간대별 패턴
    - **2.4 Correlation Analysis**: Duration과 효과의 관계
    
    #### Phase 3: Application/Implementation
    - **3.1 Activity Recommendation**: 규칙/점수 기반 추천
    - **3.2 Music Database**: 불안 수준별 음악 큐레이션
    - **3.3 Music Recommendation**: 맞춤 음악 추천
    - **3.4 Streamlit App**: 웹 앱 구현
    
    ---
    
    ### 📈 주요 발견 (Phase 2)
    
    **Activity 효과:**
    - Breathing: 평균 Delta 3.16 (1-2분, 빠른 개입)
    - Other: 평균 Delta 4.00 (15분+, 깊은 개입)
    
    **시간 패턴:**
    - 수요일/목요일: 불안 가장 높음
    - 토요일: Activity 효과 가장 좋음
    - 아침: 불안 높지만 효과도 가장 좋음
    
    **Duration 상관관계:**
    - 전체: r=0.47 (중간 양의 상관)
    - Breathing: r=0.25 (약한 상관)
    - Other: r=0.63 (중간~강한 상관)
    
    ---
    
    ### 🛠️ 기술 스택
    
    - **데이터 분석**: Python, Pandas, NumPy
    - **시각화**: Matplotlib
    - **통계**: SciPy
    - **웹 앱**: Streamlit
    - **음악**: YouTube (링크 기반)
    
    ---
    
    ### 👤 Contact
    
    **프로젝트명:** My Observer  
    **컨셉:** Don't Predict, Just Observe  
    **기간:** 2026.01 (2주)  
    **데이터:** 50개 관찰 데이터  
    
    """)
    
    st.markdown("---")
    st.markdown("##### Made with ❤️ using Streamlit")
