from cog import BasePredictor, Input, Path
import ffmpeg

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        url: Path = Input(description="Your video url (needs to be a .mp4 or .something link)"),
        start: str = Input(description="Start time in hh:mm:ss"),
        end: str = Input(description="End time in hh:mm:ss"),
    ) -> Path:

        # Use ffmpeg to cut the video
        ffmpeg.input(url, ss=start, to=end).output("output.mp4").run()

        # Return the path to the cut video
        return Path(f"./output.mp4")
    