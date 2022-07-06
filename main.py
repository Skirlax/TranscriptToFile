from turtle import width
from youtube_transcript_api import YouTubeTranscriptApi
import tkinter as tk



class Main:
    def __init__(self) -> None:
        self.tkinter_window()


    def tkinter_window(self):
        root = tk.Tk()
        root.title("YouTube Transcript")
        root.geometry("500x500")
        root.resizable(False, False)
        label = tk.Label(root, text="Video URL")
        label.pack()
        input_box = tk.Entry(root)
        # set the width of the input box to 250
        input_box.config(width=250,justify="center")
        input_box.pack()
        result_label = tk.Label(root, text="")
        result_label.place(relx=0.5, rely=0.5, anchor="center")
        
        button = tk.Button(root, text="Get Transcript", command=lambda: self.get_transcript(input_box.get(), result_label, input_box))
        button.pack()
        

        root.mainloop()



    def get_transcript(self, url, result_label, input_box):
        if "t=" in url:
            url = url.split("v=")[1]
            video_id = url.split("&")[0]

        else:
            video_id = url.split("v=")[1]
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        phrases = [x["text"] for x in transcript]
        start_times = [x["start"] for x in transcript]
        durations = [x["duration"] for x in transcript]


        with open("transcript.txt", "w+", encoding='UTF-8') as file:
            title = f"Text\tStart Time\tDuration\n"
            file.write(title)
            file.write("-"*len(title))
            file.write("\n"*2)
            for element in zip(phrases, start_times, durations):
                file.write(str(element[0]) + "\t")
                file.write(str(element[1]) + "\t")
                file.write(str(element[2]) + "\n")
        result_label.config(text="Transcript saved to transcript.txt")
        input_box.delete(0, tk.END)




if __name__ == "__main__":
    Main()
            
