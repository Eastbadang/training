# error

import glob
import tkinter

class Slideshow:
    def __init__(self, pattern="*.gif", delay=10000):

        root = tkinter.Tk()
        root.geometry("200x200")

        # this label will be used to display the image. Make
        # it automatically fill the whole window
        label = tkinter.Label(root)
        label.pack(side="top", fill="both", expand=True)

        self.current_image = None
        self.image_label = label
        self.root = root
        self.image_files = glob.glob(pattern)
        self.delay = delay # milliseconds

        # schedule the first image to appear as soon after the
        # the loop starts as possible.
        root.after(1, self.showImage)
        root.mainloop()


    def showImage(self):
        # display the next file
        file = self.image_files.pop(0)
        self.current_image = tkinter.PhotoImage(file=file)
        self.image_label.configure(image=self.current_image)

        # either reschedule to display the file,
        # or quit if there are no more files to display
        if len(self.image_files) > 0:
            self.root.after(self.delay, self.showImage)
        else:
            self.root.after(self.delay, self.root.quit)

    def quit(self):
        self.root.quit()


if __name__ == "__main__":
    app=Slideshow("images/*.gif", 1000)