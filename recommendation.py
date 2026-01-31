
"""
My Observer - Recommendation System
Activity 및 음악 추천 함수 모음
"""

# ===== Activity 추천 함수 (Rule-based) =====
def recommend_activity(anxiety_level, weekday, time_period, available_time):
    """
    규칙 기반 Activity 추천
    """
    recommendation = {
        'activity': None,
        'duration': None,
        'reason': [],
        'expected_delta': None,
        'tips': []
    }
    
    breathing_avg_delta = 3.16
    other_avg_delta = 4.00
    
    # 시간 제약 우선
    if available_time < 5:
        recommendation['activity'] = 'Breathing'
        recommendation['duration'] = f'{available_time}분'
        recommendation['reason'].append('시간이 부족하지만 빠른 개입 가능')
        recommendation['expected_delta'] = breathing_avg_delta
        recommendation['tips'].append('1-2분만 해도 효과적입니다')
        return recommendation
    
    # 불안 수준별 판단
    if anxiety_level >= 7:
        if available_time >= 15:
            recommendation['activity'] = 'Other'
            recommendation['duration'] = f'15-{available_time}분'
            recommendation['reason'].append(f'불안 수준이 높음 (Level {anxiety_level})')
            recommendation['reason'].append('시간 여유가 있어 깊은 개입 권장')
            recommendation['expected_delta'] = other_avg_delta
            
            if weekday == 'Wednesday':
                recommendation['tips'].append('수요일은 스트레스가 높은 날입니다')
                recommendation['tips'].append('충분한 시간을 투자하세요')
            
            if time_period == 'Morning':
                recommendation['tips'].append('아침은 Activity 효과가 가장 좋은 시간대입니다')
        else:
            recommendation['activity'] = 'Breathing'
            recommendation['duration'] = '1-2분'
            recommendation['reason'].append(f'불안 수준이 높음 (Level {anxiety_level})')
            recommendation['reason'].append('시간이 부족하지만 빠른 개입으로 대응')
            recommendation['expected_delta'] = breathing_avg_delta
            recommendation['tips'].append('가능하면 나중에 Other 활동도 고려하세요')
    
    elif anxiety_level >= 4:
        if available_time >= 15:
            recommendation['activity'] = 'Other'
            recommendation['duration'] = f'10-15분'
            recommendation['reason'].append('중간 수준의 불안')
            recommendation['reason'].append('시간 여유가 있어 Other도 효과적')
            recommendation['expected_delta'] = other_avg_delta
        else:
            recommendation['activity'] = 'Breathing'
            recommendation['duration'] = '1-2분'
            recommendation['reason'].append('중간 수준의 불안')
            recommendation['reason'].append('Breathing으로 충분히 효과적')
            recommendation['expected_delta'] = breathing_avg_delta
    
    else:
        recommendation['activity'] = 'Breathing'
        recommendation['duration'] = '1분'
        recommendation['reason'].append('불안 수준이 낮음')
        recommendation['reason'].append('간단한 Breathing으로 충분')
        recommendation['expected_delta'] = breathing_avg_delta
    
    if weekday in ['Saturday', 'Sunday']:
        recommendation['tips'].append('주말은 Activity 효과가 더 좋습니다!')
    
    return recommendation


# ===== Activity 추천 함수 (Score-based) =====
def recommend_activity_score_based(anxiety_level, weekday, time_period, available_time):
    """
    점수 기반 Activity 추천
    """
    breathing_score = 0
    other_score = 0
    
    # 시간 요소 (40%)
    if available_time < 5:
        breathing_score += 40
    elif available_time < 10:
        breathing_score += 35
        other_score += 10
    elif available_time < 15:
        breathing_score += 25
        other_score += 25
    else:
        breathing_score += 15
        other_score += 40
    
    # 불안 수준 (30%)
    if anxiety_level >= 7:
        breathing_score += 20
        other_score += 30
    elif anxiety_level >= 4:
        breathing_score += 25
        other_score += 25
    else:
        breathing_score += 30
        other_score += 15
    
    # 시간대 (15%)
    if time_period == 'Morning':
        breathing_score += 10
        other_score += 10
    else:
        breathing_score += 8
        other_score += 8
    
    # 요일 (15%)
    if weekday == 'Saturday':
        breathing_score += 8
        other_score += 15
    elif weekday == 'Sunday':
        breathing_score += 8
        other_score += 12
    elif weekday == 'Wednesday':
        breathing_score += 5
        other_score += 10
    elif weekday == 'Thursday':
        breathing_score += 7
        other_score += 10
    else:
        breathing_score += 8
        other_score += 8
    
    # 결과 생성
    recommendation = {
        'breathing_score': breathing_score,
        'other_score': other_score,
        'activity': 'Breathing' if breathing_score > other_score else 'Other',
        'confidence': abs(breathing_score - other_score),
        'reason': [],
        'tips': []
    }
    
    if recommendation['activity'] == 'Breathing':
        recommendation['duration'] = '1-2분'
        recommendation['expected_delta'] = 3.16
        
        if available_time < 5:
            recommendation['reason'].append('시간이 부족하여 빠른 개입 필요')
        if anxiety_level < 7:
            recommendation['reason'].append('현재 불안 수준에 충분히 효과적')
    else:
        recommendation['duration'] = f'15-{min(available_time, 30)}분'
        recommendation['expected_delta'] = 4.00
        
        if anxiety_level >= 7:
            recommendation['reason'].append('불안 수준이 높아 깊은 개입 권장')
        if available_time >= 15:
            recommendation['reason'].append('시간 여유가 있어 효과적인 대응 가능')
        if weekday in ['Saturday', 'Sunday']:
            recommendation['reason'].append('주말은 효과가 더 좋습니다')
    
    if time_period == 'Morning':
        recommendation['tips'].append('아침은 Activity 효과가 가장 좋은 시간대입니다')
    if weekday == 'Wednesday' and anxiety_level >= 7:
        recommendation['tips'].append('수요일은 스트레스가 높은 날, 충분한 시간 투자를 권장합니다')
    
    return recommendation


# ===== 음악 추천 함수 =====
def recommend_music(anxiety_level, duration, music_database, preference=None):
    """
    불안 수준과 Duration에 맞는 음악 추천
    """
    # 카테고리 선택
    if anxiety_level >= 7:
        category_key = 'high_anxiety'
    elif anxiety_level >= 4:
        category_key = 'medium_anxiety'
    else:
        category_key = 'low_anxiety'
    
    category = music_database[category_key]
    
    # 곡 수 계산
    num_tracks = max(1, min(duration // 4, 10))
    
    # 플레이리스트 선택
    if preference and preference in category['playlists']:
        selected_playlists = [category['playlists'][preference]]
    else:
        selected_playlists = list(category['playlists'].values())
    
    # 곡 선택
    recommended_tracks = []
    playlist_names = []
    
    for playlist in selected_playlists:
        playlist_names.append(playlist['name'])
        tracks_needed = num_tracks // len(selected_playlists)
        if tracks_needed > 0:
            recommended_tracks.extend(playlist['tracks'][:tracks_needed])
    
    if len(recommended_tracks) < num_tracks and selected_playlists:
        remaining = num_tracks - len(recommended_tracks)
        recommended_tracks.extend(
            selected_playlists[0]['tracks'][
                len(recommended_tracks):len(recommended_tracks)+remaining
            ]
        )
    
    # 총 재생 시간 계산
    total_duration = 0
    for track in recommended_tracks[:num_tracks]:
        time_parts = track['duration'].split(':')
        total_duration += int(time_parts[0]) * 60 + int(time_parts[1])
    total_duration = total_duration // 60
    
    # 결과 생성
    recommendation = {
        'category': category['category'],
        'bpm_range': category['bpm_range'],
        'playlists': playlist_names,
        'tracks': recommended_tracks[:num_tracks],
        'total_duration': total_duration,
        'reason': [],
        'tips': []
    }
    
    recommendation['reason'].append(f"불안 수준 {anxiety_level}에 적합한 {category['category']}")
    recommendation['reason'].append(f"약 {duration}분 동안 들을 수 있는 {len(recommendation['tracks'])}곡 선정")
    
    if anxiety_level >= 7:
        recommendation['tips'].append('깊게 호흡하면서 음악을 들어보세요')
        recommendation['tips'].append('편안한 자세로 눈을 감고 듣는 것을 권장합니다')
    elif anxiety_level >= 4:
        recommendation['tips'].append('가벼운 스트레칭과 함께 들으면 좋습니다')
    else:
        recommendation['tips'].append('일상 활동을 하면서 배경음악으로 들어보세요')
    
    return recommendation


# ===== 통합 추천 함수 =====
def get_full_recommendation(anxiety_level, weekday, time_period, available_time,
                           music_database, recommendation_version='score', 
                           music_preference=None):
    """
    Activity와 음악 통합 추천
    """
    # Activity 추천
    if recommendation_version == 'rule':
        activity_rec = recommend_activity(
            anxiety_level, weekday, time_period, available_time
        )
    else:
        activity_rec = recommend_activity_score_based(
            anxiety_level, weekday, time_period, available_time
        )
    
    # 음악 추천 (Other일 때만)
    music_rec = None
    if activity_rec['activity'] == 'Other':
        music_rec = recommend_music(
            anxiety_level, available_time, music_database, preference=music_preference
        )
    
    # 통합 결과
    full_recommendation = {
        'input': {
            'anxiety_level': anxiety_level,
            'weekday': weekday,
            'time_period': time_period,
            'available_time': available_time
        },
        'activity': activity_rec,
        'music': music_rec
    }
    
    return full_recommendation
