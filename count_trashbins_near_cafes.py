
from tqdm import tqdm
from haversine import haversine, Unit
import pandas as pd

def count_trashbins_near_cafes(cafe_coords, trashbin_coords, radius=300):
    """
    각 카페 근방 300m 내에 있는 쓰레기통의 개수를 계산합니다.
    
    Parameters:
    cafe_coords (DataFrame): 카페 좌표 데이터프레임
    trashbin_coords (DataFrame): 쓰레기통 좌표 데이터프레임
    radius (float): 탐색 반경 (단위: m), 기본값 300m
    
    Returns:
    list: 각 카페 근방의 쓰레기통 개수
    """
    trashbin_count = []
    
    # 각 카페마다 300m 반경 내의 쓰레기통 개수를 계산
    for idx, cafe_row in tqdm(cafe_coords.iterrows(), total=cafe_coords.shape[0], desc="Processing cafes"):
        cafe_location = (cafe_row['Latitude'], cafe_row['Longitude'])
        count = 0
        
        # 모든 쓰레기통과의 거리를 일일이 계산
        for _, trash_row in trashbin_coords.iterrows():
            trash_location = (trash_row['Latitude'], trash_row['Longitude'])
            distance = haversine(cafe_location, trash_location, unit=Unit.METERS)
            
            # 300m 이내의 쓰레기통만 카운트
            if distance <= radius:
                count += 1
        
        trashbin_count.append(count)
    
    return trashbin_count
