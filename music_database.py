
"""
My Observer - Music Database
불안 수준별 음악 데이터베이스
"""

MUSIC_DATABASE = {
    'high_anxiety': {
        'level_range': (7, 10),
        'category': '매우 차분한 음악',
        'bpm_range': '60-80',
        'description': '불안이 심할 때 깊은 이완을 위한 음악',
        'playlists': {
            'calm_classical': {
                'name': '차분한 클래식',
                'mood': '평온, 명상적',
                'tracks': [
                    {
                        'title': 'Clair de Lune',
                        'artist': 'Claude Debussy',
                        'duration': '5:24',
                        'youtube': 'https://www.youtube.com/watch?v=CvFH_6DNRCY'
                    },
                    {
                        'title': 'Gymnopédie No.1',
                        'artist': 'Erik Satie',
                        'duration': '3:28',
                        'youtube': 'https://www.youtube.com/watch?v=S-Xm7s9eGxU'
                    },
                    {
                        'title': 'Nocturne Op.9 No.2',
                        'artist': 'Frédéric Chopin',
                        'duration': '4:30',
                        'youtube': 'https://www.youtube.com/watch?v=9E6b3swbnWg'
                    },
                    {
                        'title': 'The Swan',
                        'artist': 'Camille Saint-Saëns',
                        'duration': '3:00',
                        'youtube': 'https://www.youtube.com/watch?v=3qrKjywjo7Q'
                    },
                    {
                        'title': 'Spiegel im Spiegel',
                        'artist': 'Arvo Pärt',
                        'duration': '8:36',
                        'youtube': 'https://www.youtube.com/watch?v=TJ6Mzvh3XCc'
                    }
                ]
            },
            'ambient': {
                'name': '앰비언트/명상',
                'mood': '극도로 차분함',
                'tracks': [
                    {
                        'title': 'Weightless',
                        'artist': 'Marconi Union',
                        'duration': '8:09',
                        'youtube': 'https://www.youtube.com/watch?v=UfcAVejslrU'
                    },
                    {
                        'title': 'An Ending (Ascent)',
                        'artist': 'Brian Eno',
                        'duration': '4:24',
                        'youtube': 'https://www.youtube.com/watch?v=It4WxQ6dnn0'
                    },
                    {
                        'title': 'Sleep (Excerpt)',
                        'artist': 'Max Richter',
                        'duration': '8:00',
                        'youtube': 'https://www.youtube.com/watch?v=6btQmMglHs0'
                    },
                    {
                        'title': 'A Walk',
                        'artist': 'Tycho',
                        'duration': '4:54',
                        'youtube': 'https://www.youtube.com/watch?v=mehLx_Fjv_c'
                    },
                    {
                        'title': 'On The Nature Of Daylight',
                        'artist': 'Max Richter',
                        'duration': '6:07',
                        'youtube': 'https://www.youtube.com/watch?v=rVN1B-tUpgs'
                    }
                ]
            },
            'nature_sounds': {
                'name': '자연의 소리',
                'mood': '평화로움',
                'tracks': [
                    {
                        'title': 'Rain Sounds for Sleeping',
                        'artist': 'Nature Sounds',
                        'duration': '10:00',
                        'youtube': 'https://www.youtube.com/watch?v=q76bMs-NwRk'
                    },
                    {
                        'title': 'Ocean Waves',
                        'artist': 'Relaxing Sounds',
                        'duration': '8:00',
                        'youtube': 'https://www.youtube.com/watch?v=bn9F19Ce6Ik'
                    },
                    {
                        'title': 'Forest Sounds',
                        'artist': 'Nature Meditation',
                        'duration': '10:00',
                        'youtube': 'https://www.youtube.com/watch?v=eKFTSSKCzWA'
                    },
                    {
                        'title': 'Gentle Stream',
                        'artist': 'Calm Water',
                        'duration': '8:00',
                        'youtube': 'https://www.youtube.com/watch?v=szEfp07r5Hw'
                    },
                    {
                        'title': 'Peaceful Piano with Rain',
                        'artist': 'Relaxing Music',
                        'duration': '3:00',
                        'youtube': 'https://www.youtube.com/watch?v=EfEHQdMscfI'
                    }
                ]
            }
        }
    },
    
    'medium_anxiety': {
        'level_range': (4, 6),
        'category': '잔잔한 음악',
        'bpm_range': '80-100',
        'description': '중간 수준의 불안에 적합한 편안한 음악',
        'playlists': {
            'acoustic': {
                'name': '어쿠스틱/인디',
                'mood': '따뜻함, 편안함',
                'tracks': [
                    {
                        'title': 'Holocene',
                        'artist': 'Bon Iver',
                        'duration': '5:37',
                        'youtube': 'https://www.youtube.com/watch?v=TWcyIpul8OE'
                    },
                    {
                        'title': 'To Build a Home',
                        'artist': 'The Cinematic Orchestra',
                        'duration': '6:28',
                        'youtube': 'https://www.youtube.com/watch?v=oUFJJNQGwhk'
                    },
                    {
                        'title': 'Skinny Love',
                        'artist': 'Bon Iver',
                        'duration': '3:58',
                        'youtube': 'https://www.youtube.com/watch?v=ssdgFoHLwnk'
                    },
                    {
                        'title': 'Flume',
                        'artist': 'Bon Iver',
                        'duration': '3:21',
                        'youtube': 'https://www.youtube.com/watch?v=WJW_ldC7sUA'
                    },
                    {
                        'title': 'The Night We Met',
                        'artist': 'Lord Huron',
                        'duration': '3:28',
                        'youtube': 'https://www.youtube.com/watch?v=KtlgYxa6BMU'
                    }
                ]
            },
            'soft_piano': {
                'name': '부드러운 피아노',
                'mood': '차분함',
                'tracks': [
                    {
                        'title': 'River Flows in You',
                        'artist': 'Yiruma',
                        'duration': '3:50',
                        'youtube': 'https://www.youtube.com/watch?v=7maJOI3QMu0'
                    },
                    {
                        'title': "Comptine d'un autre été",
                        'artist': 'Yann Tiersen',
                        'duration': '2:17',
                        'youtube': 'https://www.youtube.com/watch?v=NvryolGa19A'
                    },
                    {
                        'title': 'Nuvole Bianche',
                        'artist': 'Ludovico Einaudi',
                        'duration': '5:57',
                        'youtube': 'https://www.youtube.com/watch?v=kcihcYEOeic'
                    },
                    {
                        'title': 'Kiss the Rain',
                        'artist': 'Yiruma',
                        'duration': '4:31',
                        'youtube': 'https://www.youtube.com/watch?v=imGaHkfchOE'
                    },
                    {
                        'title': 'Una Mattina',
                        'artist': 'Ludovico Einaudi',
                        'duration': '5:15',
                        'youtube': 'https://www.youtube.com/watch?v=6aRca016dH8'
                    }
                ]
            },
            'lofi': {
                'name': 'Lo-fi Hip Hop',
                'mood': '집중, 편안함',
                'tracks': [
                    {
                        'title': 'Snowman',
                        'artist': 'WYS',
                        'duration': '2:26',
                        'youtube': 'https://www.youtube.com/watch?v=Z6_aTHyk5dU'
                    },
                    {
                        'title': 'Let Go',
                        'artist': 'Idealism',
                        'duration': '2:11',
                        'youtube': 'https://www.youtube.com/watch?v=NhIpg70c8hE'
                    },
                    {
                        'title': 'Days with You',
                        'artist': 'Snøw',
                        'duration': '2:37',
                        'youtube': 'https://www.youtube.com/watch?v=I4oLvaVKXB4'
                    },
                    {
                        'title': 'Study Session',
                        'artist': 'Lofi Hip Hop',
                        'duration': '3:00',
                        'youtube': 'https://www.youtube.com/watch?v=jfKfPfyJRdk'
                    },
                    {
                        'title': 'Coffee',
                        'artist': 'Bearcubs',
                        'duration': '3:28',
                        'youtube': 'https://www.youtube.com/watch?v=CCVEYboLzjY'
                    }
                ]
            }
        }
    },
    
    'low_anxiety': {
        'level_range': (1, 3),
        'category': '편안한 음악',
        'bpm_range': '90-110',
        'description': '낮은 불안 수준에 적합한 밝고 편안한 음악',
        'playlists': {
            'jazz': {
                'name': '재즈',
                'mood': '여유로움',
                'tracks': [
                    {
                        'title': 'Fly Me to the Moon',
                        'artist': 'Frank Sinatra',
                        'duration': '2:28',
                        'youtube': 'https://www.youtube.com/watch?v=ZEcqHA7dbwM'
                    },
                    {
                        'title': 'Autumn Leaves',
                        'artist': 'Bill Evans',
                        'duration': '5:05',
                        'youtube': 'https://www.youtube.com/watch?v=r-Z8KuwI7Gc'
                    },
                    {
                        'title': 'Take Five',
                        'artist': 'Dave Brubeck',
                        'duration': '5:24',
                        'youtube': 'https://www.youtube.com/watch?v=vmDDOFXSgAs'
                    },
                    {
                        'title': 'Blue in Green',
                        'artist': 'Miles Davis',
                        'duration': '5:37',
                        'youtube': 'https://www.youtube.com/watch?v=PoPL7BExSQU'
                    },
                    {
                        'title': 'My Favorite Things',
                        'artist': 'John Coltrane',
                        'duration': '13:44',
                        'youtube': 'https://www.youtube.com/watch?v=qWG2dsXV5HI'
                    }
                ]
            },
            'bossa_nova': {
                'name': '보사노바',
                'mood': '경쾌함',
                'tracks': [
                    {
                        'title': 'The Girl from Ipanema',
                        'artist': 'Stan Getz & João Gilberto',
                        'duration': '5:26',
                        'youtube': 'https://www.youtube.com/watch?v=UJkxFhFRFDA'
                    },
                    {
                        'title': 'Chega de Saudade',
                        'artist': 'João Gilberto',
                        'duration': '2:23',
                        'youtube': 'https://www.youtube.com/watch?v=KJzwHKPDAlQ'
                    },
                    {
                        'title': 'Desafinado',
                        'artist': 'Antonio Carlos Jobim',
                        'duration': '4:04',
                        'youtube': 'https://www.youtube.com/watch?v=l5LjKcVr3rY'
                    },
                    {
                        'title': 'Corcovado',
                        'artist': 'Stan Getz',
                        'duration': '4:21',
                        'youtube': 'https://www.youtube.com/watch?v=0yTRshLKwNM'
                    },
                    {
                        'title': 'Água de Beber',
                        'artist': 'Antonio Carlos Jobim',
                        'duration': '2:34',
                        'youtube': 'https://www.youtube.com/watch?v=vfxMcRoIE00'
                    }
                ]
            },
            'chill_electronic': {
                'name': '칠 일렉트로닉',
                'mood': '현대적, 편안함',
                'tracks': [
                    {
                        'title': 'Sunset Lover',
                        'artist': 'Petit Biscuit',
                        'duration': '3:34',
                        'youtube': 'https://www.youtube.com/watch?v=wuCK-oiE3rM'
                    },
                    {
                        'title': 'Bloom',
                        'artist': 'ODESZA',
                        'duration': '5:51',
                        'youtube': 'https://www.youtube.com/watch?v=wuCK-oiE3rM'
                    },
                    {
                        'title': 'Something About You',
                        'artist': 'ODESZA',
                        'duration': '3:45',
                        'youtube': 'https://www.youtube.com/watch?v=YdV52CIVMuY'
                    },
                    {
                        'title': 'Feel It All Around',
                        'artist': 'Washed Out',
                        'duration': '4:39',
                        'youtube': 'https://www.youtube.com/watch?v=-DkslcOhKVo'
                    },
                    {
                        'title': 'Intro',
                        'artist': 'The xx',
                        'duration': '2:11',
                        'youtube': 'https://www.youtube.com/watch?v=3gxNW2Ulpwk'
                    }
                ]
            }
        }
    }
}
