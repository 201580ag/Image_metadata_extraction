from PIL import Image
from PIL.ExifTags import TAGS

TAGS_KOR = {
    "ImageWidth": "이미지 너비",
    "ImageLength": "이미지 높이",
    "GPSInfo": "GPS 정보",
    "ResolutionUnit": "해상도 단위",
    "ExifOffset": "Exif 오프셋",
    "Make": "카메라 제조사",
    "Model": "카메라 모델",
    "Software": "소프트웨어",
    "Orientation": "방향",
    "DateTime": "날짜 및 시간",
    "YCbCrPositioning": "YCbCr 위치",
    "XResolution": "X 해상도",
    "YResolution": "Y 해상도",
    "ExifVersion": "Exif 버전",
    "ShutterSpeedValue": "셔터 스피드 값",
    "ApertureValue": "조리개 값",
    "DateTimeOriginal": "원본 촬영 날짜 및 시간",
    "DateTimeDigitized": "디지털 변환 날짜 및 시간",
    "BrightnessValue": "밝기 값",
    "MaxApertureValue": "최대 조리개 값",
    "MeteringMode": "측광 모드",
    "ColorSpace": "색 공간",
    "Flash": "플래시",
    "FocalLength": "초점 거리",
    "ExifImageWidth": "Exif 이미지 너비",
    "ExifImageHeight": "Exif 이미지 높이",
    "DigitalZoomRatio": "디지털 줌 비율",
    "FocalLengthIn35mmFilm": "35mm 필름 환산 초점 거리",
    "SceneCaptureType": "씬 캡처 타입",
    "OffsetTime": "오프셋 시간",
    "OffsetTimeOriginal": "원본 오프셋 시간",
    "SubsecTime": "하위 초 시간",
    "SubsecTimeOriginal": "원본 하위 초 시간",
    "SubsecTimeDigitized": "디지털 변환 하위 초 시간",
    "ExposureTime": "노출 시간",
    "FNumber": "조리개 값",
    "ImageUniqueID": "이미지 고유 ID",
    "ExposureProgram": "노출 프로그램",
    "ISOSpeedRatings": "ISO 속도 등급",
    "ExposureMode": "노출 모드",
    "WhiteBalance": "화이트 밸런스",
}

def get_image_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()

        if exif_data is not None:
            metadata = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                tag_name_kor = TAGS_KOR.get(tag_name, tag_name)
                metadata[tag_name_kor] = value

            return metadata
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def print_image_metadata(image_path):
    metadata = get_image_metadata(image_path)

    if metadata:
        print("Image metadata:")
        for tag, value in metadata.items():
            print(f"{tag}: {value}")
    else:
        print("The image contains no metadata.")

if __name__ == "__main__":
    while True:
        image_path = input("Enter image file path (termination: q):")

        if image_path.lower() == "q":
            break

        try:
            print_image_metadata(image_path)
        except FileNotFoundError:
            print("Error: File not found.")
        except Image.UnidentifiedImageError:
            print("Error: Invalid image file format.")
