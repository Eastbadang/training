import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import comtypes.client
from PIL import Image


class PPTConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PPT 슬라이드 병합 도구 v1.2")
        self.root.geometry("500x280")
        self.root.resizable(False, False)

        self.ppt_path = tk.StringVar()
        self.save_path = tk.StringVar()
        self.setup_ui()

    def setup_ui(self):
        layout = {"padx": 15, "pady": 5}

        tk.Label(self.root, text="대상 PPT 파일:").pack(anchor="w", **layout)
        frame1 = tk.Frame(self.root)
        frame1.pack(fill="x", **layout)
        tk.Entry(frame1, textvariable=self.ppt_path).pack(side="left", fill="x", expand=True)
        tk.Button(frame1, text="찾기", command=self.browse_ppt).pack(side="right", padx=5)

        tk.Label(self.root, text="결과 이미지 저장 경로:").pack(anchor="w", **layout)
        frame2 = tk.Frame(self.root)
        frame2.pack(fill="x", **layout)
        tk.Entry(frame2, textvariable=self.save_path).pack(side="left", fill="x", expand=True)
        tk.Button(frame2, text="설정", command=self.browse_save_path).pack(side="right", padx=5)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progress.pack(fill="x", **layout)

        self.btn_run = tk.Button(self.root, text="이미지로 변환 및 병합 시작",
                                 bg="#2ecc71", fg="white", font=("malgun gothic", 10, "bold"),
                                 command=self.run_process)
        self.btn_run.pack(fill="x", padx=15, pady=20)

    def browse_ppt(self):
        """PPT 파일을 선택하면 파일명을 추출하여 저장 경로를 자동 설정"""
        file = filedialog.askopenfilename(filetypes=[("PowerPoint files", "*.pptx *.ppt")])
        if file:
            self.ppt_path.set(file)

            # 1. 파일명만 추출 (예: '보고서.pptx' -> '보고서')
            base_name = os.path.splitext(os.path.basename(file))[0]
            # 2. 원본 파일과 같은 폴더 경로 추출
            folder_path = os.path.dirname(file)
            # 3. '폴더/파일명.jpg' 형태로 기본 저장명 생성
            default_save = os.path.join(folder_path, f"{base_name}.jpg")

            # UI에 반영 (사용자가 원하면 '설정' 버튼으로 수정 가능)
            self.save_path.set(default_save)

    def browse_save_path(self):
        """사용자가 직접 저장 경로 및 파일명을 수정하고 싶을 때 실행"""
        # 현재 설정된 파일명을 기본값으로 다이얼로그 열기
        initial_file = os.path.basename(self.save_path.get()) if self.save_path.get() else "merged_result.jpg"

        file = filedialog.asksaveasfilename(
            initialfile=initial_file,
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")]
        )
        if file:
            self.save_path.set(file)

    def run_process(self):
        # ... (이전 run_process 로직과 동일) ...
        ppt = self.ppt_path.get()
        save = self.save_path.get()

        if not ppt or not save:
            messagebox.showwarning("경고", "파일 및 저장 경로를 모두 선택해주세요.")
            return

        self.btn_run.config(state="disabled")
        self.progress["value"] = 0

        powerpoint = None
        presentation = None
        image_paths = []

        try:
            temp_dir = os.path.join(os.environ["TEMP"], "ppt_conv_temp")
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            abs_ppt_path = os.path.abspath(ppt)
            # WithWindow=True로 설정 시 호환성이 더 좋을 수 있음
            presentation = powerpoint.Presentations.Open(abs_ppt_path, ReadOnly=True, WithWindow=False)

            slides_count = presentation.Slides.Count
            for i, slide in enumerate(presentation.Slides):
                img_path = os.path.join(temp_dir, f"slide_{i}.jpg")
                slide.Export(img_path, "JPG")
                image_paths.append(img_path)

                self.progress["value"] = ((i + 1) / slides_count) * 50
                self.root.update_idletasks()

            imgs = [Image.open(x) for x in image_paths]
            widths, heights = zip(*(i.size for i in imgs))

            new_im = Image.new('RGB', (max(widths), sum(heights)), (255, 255, 255))

            y_offset = 0
            for i, im in enumerate(imgs):
                new_im.paste(im, (0, y_offset))
                y_offset += im.size[1]
                im.close()
                self.progress["value"] = 50 + ((i + 1) / len(imgs)) * 50
                self.root.update_idletasks()

            new_im.save(save, quality=95)

            for p in image_paths:
                try:
                    os.remove(p)
                except:
                    pass

            messagebox.showinfo("완료", f"성공적으로 저장되었습니다!\n파일명: {os.path.basename(save)}")

        except Exception as e:
            messagebox.showerror("오류 발생", f"상세 내용: {str(e)}")
        finally:
            if presentation: presentation.Close()
            if powerpoint: powerpoint.Quit()
            self.btn_run.config(state="normal")
            self.progress["value"] = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = PPTConverterApp(root)
    root.mainloop()
