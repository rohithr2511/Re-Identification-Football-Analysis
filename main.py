#Import All the Required Libraries
from utils import read_video, save_video
from trackers import Tracker

def main():
    #Read Video
    video_frames = read_video("C:\\Users\\Rahul\\OneDrive\\Desktop\\footballprjct\\input_video\\15sec_input_720p.mp4")

    #Initialize Tracker
    tracker = Tracker("C:\\Users\\Rahul\\OneDrive\\Desktop\\footballprjct\\models\\best.pt")
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=False, stub_path='tracker_stubs/player_detection.pkl')

    #Draw Output
    #Draw Object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    #Save Video
    save_video(video_frames, 'output_videos/output.avi')


if __name__ == "__main__":
    main()