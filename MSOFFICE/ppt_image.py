import os
import comtypes.client
from PIL import Image
import time


def ppt_to_images(ppt_path, output_folder):
    # 1. 출력 폴더를 절대 경로로 생성 (중요)
    abs_output_folder = os.path.abspath(output_folder)
    if not os.path.exists(abs_output_folder):
        os.makedirs(abs_output_folder)

    powerpoint = None
    presentation = None

    try:
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        # 비활성화 상태에서 작업 (속도 향상 및 간섭 방지)
        powerpoint.Visible = 1

        abs_ppt_path = os.path.abspath(ppt_path)
        presentation = powerpoint.Presentations.Open(abs_ppt_path, ReadOnly=True, WithWindow=False)

        image_paths = []
        for i, slide in enumerate(presentation.Slides):
            # 슬라이드 번호를 포함한 파일명 설정 (절대 경로 사용)
            image_name = f"slide_{i + 1}.jpg"
            image_path = os.path.join(abs_output_folder, image_name)

            # Export 메서드 실행 (에러 방지를 위해 절대 경로 전달)
            slide.Export(image_path, "JPG")

            # 파일이 생성될 때까지 아주 잠깐 대기 (I/O 지연 방지)
            timeout = 5
            while not os.path.exists(image_path) and timeout > 0:
                time.sleep(0.1)
                timeout -= 1

            image_paths.append(image_path)
            print(f"슬라이드 {i + 1} 변환 완료")

        return image_paths

    finally:
        if presentation:
            presentation.Close()
        if powerpoint:
            powerpoint.Quit()


def merge_images_vertically(image_paths, output_name="final_result.jpg"):
    if not image_paths:
        print("변환된 이미지가 없습니다.")
        return

    images = [Image.open(x) for x in image_paths]
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    total_height = sum(heights)

    new_im = Image.new('RGB', (max_width, total_height), (255, 255, 255))

    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]
        im.close()  # 리소스 해제

    new_im.save(output_name)
    print(f"\n[성공] 모든 슬라이드가 병합되었습니다: {os.path.abspath(output_name)}")


if __name__ == "__main__":
    # 파일명이 실제 파일과 일치하는지 확인하세요.
    target_ppt = "발표자료_디자인_보완자료_20260506.pptx"
    output_dir = "temp_slides"

    if not os.path.exists(target_ppt):
        print(f"오류: {target_ppt} 파일을 찾을 수 없습니다.")
    else:
        try:
            print("슬라이드 추출 시작...")
            imgs = ppt_to_images(target_ppt, output_dir)

            print("이미지 병합 시작...")
            merge_images_vertically(imgs)
        except Exception as e:
            print(f"\n최종 오류 발생: {e}")
