from pathlib import Path

from karawm.core import Karawm

if __name__ == "__main__":
    input_video_path = Path("resources/dog_vs_sam.mp4")
    output_video_path = Path("outputs/kara_karamark_removed.mp4")
    kara_wm = Karawm()
    kara_wm.run(input_video_path, output_video_path)
